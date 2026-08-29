from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os
import json

from RAG.loader import load_document
from RAG.chunker import split_into_chunks
from RAG.embeddings import create_embedding

from Tools.registry import available_tools
from Agent.agent import Agent


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

def save_conversation(conversation, filename = "conversations.json"):
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(conversation, file, indent=4)



document = load_document("document.txt")

chunks = split_into_chunks(document)

chunk_embeddings = []

for index, chunk in enumerate(chunks, start=1):
    embedding = create_embedding(chunk, client)

    chunk_embeddings.append({
        "chunk_id": index,
        "text": chunk,
        "embedding": embedding
    })

conversations = []
questions_count = 0

agent = Agent(client=client, tools=available_tools, chunk_embeddings=chunk_embeddings)

while True:
    try:
        query = input("\nEnter your query (or type exit): ").strip()


        if not query:
            print("\nQuery is invalid")
            continue

        if query.lower() == "exit":
            break

        agent_response = agent.parse_agent_response(agent.ask_agent(query, conversations))

        valid_response = agent.validate_agent_response(agent_response)

        if valid_response["action"] == "error":
            print(valid_response["text"])
            continue

        agent_action = valid_response["action"]
        agent_source = valid_response["source"]

        questions_count+=1

        if agent_action == "retrieve" and agent_source == "rag":

            answer = agent.generate_rag_answer(query, conversations)

            conversations.append({
                f"Question {questions_count}": query,
                f"Answer {questions_count}": answer
            })

            print("\nAnswer:")
            print(answer)

        elif agent_action == "calculate" and agent_source == "tool":

            expression = valid_response["text"]

            answer = agent.execute_tool(query, "calculate", expression)

            conversations.append({
                f"Question {questions_count}": query,
                "Expression": expression,
                f"Answer {questions_count}": answer
            })

            print(f"\nAnswer: {answer}")

        elif agent_action == "memory" and agent_source == "conversation":

            answer = valid_response["text"]

            conversations.append({
                f"Question {questions_count}" : query,
                f"Answer {questions_count}" : answer
            })

            print(f"\nAnswer: {answer}")
    except RateLimitError:
        print("\nError: API quota exceeded. Please try again later.")
        continue
    except Exception as e:
        print(f"\nError: {e}")
        continue

save_conversation(conversations)