import json
from RAG.retriever import search_chunks
from RAG.generator import generate_answer


class Agent:

    def __init__(self, client, tools, chunk_embeddings):
        self.client = client
        self.tools = tools
        self.chunk_embeddings = chunk_embeddings

    def ask_agent(self, task, conversations):
        prompt = f"""
You are a routing agent.

User task:
{task}

Available tools:
{self.tools}

Previous Conversations:
{conversations}

Choose one source: RAG, TOOL, or MEMORY.

1. RAG
Use for questions requiring information from the document.

Return:
{{
    "action": "retrieve",
    "source": "rag",
    "text": ""
}}

2. TOOL
Use for any mathematical calculation.

Normalize the expression with spaces around operators:
+  -  *  /

Examples:
23+2 → "23 + 2"
what is 25 plus 4 → "25 + 4"
100 divided by 5 → "100 / 5"

If the task is a follow-up calculation such as:
"add 5", "+ 5", "subtract 3", "* 2", "multiply by 2", "divide by 4"

use the most recent successful numeric calculation result
from Previous Conversations as the first operand.

Example:
Previous result: 40.0
User: * 2

Return:
{{
    "action": "calculate",
    "source": "tool",
    "text": "40.0 * 2"
}}

3. MEMORY
Use when the requested information already exists in Previous Conversations.

Return the relevant previous answer/result in "text".

Example:
Previous result: 75.0
User: what was the result

Return:
{{
    "action": "memory",
    "source": "conversation",
    "text": "75.0"
}}

Rules:
- Check Previous Conversations first for follow-up questions.
- Use TOOL for calculations.
- Use RAG for document information.
- Use MEMORY for existing conversation information.
- For follow-up calculations, always use the latest successful numeric result.
- Normalize every tool expression.
- Never return an invalid or incomplete mathematical expression.
- Do not calculate the result yourself.
- Return ONLY valid JSON.
- Do not use markdown or code fences.
"""

        response = self.client.chat.completions.create(
            model="gemini-flash-lite-latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    def parse_agent_response(self, response):
        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return {
                "action": "error",
                "source": "none",
                "text": response
            }

    def validate_agent_response(self, response):
        if not isinstance(response, dict):
            return {
                "action": "error",
                "source": "none",
                "text": "not valid dictionary"
            }

        if "action" not in response:
            return {
                "action": "error",
                "source": "none",
                "text": "not valid keys"
            }

        if "source" not in response:
            return {
                "action": "error",
                "source": "none",
                "text": "not valid keys"
            }

        if "text" not in response:
            return {
                "action": "error",
                "source": "none",
                "text": "not valid keys"
            }

        if not isinstance(response["action"], str):
            return {
                "action": "error",
                "source": "none",
                "text": "action must be a string"
            }

        if not isinstance(response["source"], str):
            return {
                "action": "error",
                "source": "none",
                "text": "source must be a string"
            }

        if not isinstance(response["text"], str):
            return {
                "action": "error",
                "source": "none",
                "text": "text must be a string"
            }

        action = response["action"].strip().lower()
        source = response["source"].strip().lower()

        if (
            (action == "retrieve" and source == "rag")
            or
            (action == "calculate" and source == "tool")
            or
            (action == "memory" and source == "conversation")
        ):
            return {
                "action": action,
                "source": source,
                "text": response["text"]
            }

        return {
            "action": "error",
            "source": "none",
            "text": "not valid combination"
        }

    def generate_tool_answer(self, query, tool_name, expression, result):
        prompt = f"""
    User query:
    {query}

    Tool used:
    {tool_name}

    Expression:
    {expression}

    Result:
    {result}

    Use only the provided tool result to answer the user.
    Do not perform another calculation.
    Do not change the result.
    Return a concise final answer.
    """
        
        
        response = self.client.chat.completions.create(
            model="gemini-flash-lite-latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    def generate_rag_answer(self, query, conversations):

        results = search_chunks(query, self.chunk_embeddings, client=self.client)

        return generate_answer(query, results, conversations, client=self.client)

    def execute_tool(self, query, tool_name, expression):
        function = self.tools[tool_name]

        result = function(expression=expression)

        return self.generate_tool_answer(query, tool_name, expression, result)