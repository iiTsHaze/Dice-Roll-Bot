import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if message == '!roll':
        return str(random.randint(0, 100))
