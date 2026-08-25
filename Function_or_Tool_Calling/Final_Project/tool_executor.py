import json
from tools import available_tools


def execute_tool(tool_call):
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name not in available_tools:
        return f"Unknown tool: {function_name}"

    function = available_tools[function_name]

    return function(**arguments)