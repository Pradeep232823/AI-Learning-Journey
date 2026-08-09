import responses
import random

def process_message(message):
    greeting = ["hi", "hello", "hey"]
    help_inputs = ["what can you do"]
    python_inputs = ["python", "what is python", "tell me about python" ]
    fastapi_inputs = ["fastapi", "what is fastapi", "tell me about fastapi" ]

    if message in greeting:
        return random.choice(responses.GREETING_RESPONSES)
    elif message in help_inputs:
        return random.choice(responses.HELP_RESPONSES)
    elif message in python_inputs:
        return random.choice(responses.PYTHON_RESPONSES)
    elif message in fastapi_inputs:
        return random.choice(responses.FASTAPI_RESPONSES)
    else:
        return random.choice(responses.UNKNOWN_RESPONSES)