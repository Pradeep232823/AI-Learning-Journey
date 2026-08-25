tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform basic arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number."
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number."
                    },
                    "operation": {
                        "type": "string",
                        "description": "The arithmetic operation: add, subtract, multiply, or divide."
                    }
                },
                "required": ["a", "b", "operation"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "temp_conversion",
            "description": "Perform the temperature conversion according to query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "temp": {
                        "type": "number",
                        "description": "The temperature in celsius or fahrenheit."
                    },
                    "conversion": {
                        "type": "string",
                        "description": "The conversion type: celsius to fahrenheit or fahrenheit to celsius"
                    }
                },
                "required": ["temp", "conversion"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_datetime",
            "description": "Generate date and time according to input",
            "parameters": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "The input type: date, time or date and time."
                    }
                },
                "required": ["input"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_words",
            "description": "Count words in the given text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Text given to count number of words in it."
                    }
                },
                "required": ["text"]
            }
        }
    }
]
