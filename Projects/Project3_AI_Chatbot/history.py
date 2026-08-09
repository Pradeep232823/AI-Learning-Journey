from datetime import datetime

def add_history(session):

    user_message = session[0]
    response = session[1]

    now = datetime.now()
    date = now.strftime("%Y_%m_%d")
    path = f"chats/{date}_chat.txt"

    time = now.strftime("%H:%M:%S")

    with open(path,"a",encoding="utf-8") as file:

        if response in ["Session Started", "Session Closed"]:
            file.write(f"[{user_message}] {response}\n\n")
            return
        
        file.write(f"[{time}]\n")
        file.write(f"User: {user_message}\n")
        file.write(f"Bot: {response}\n\n")

def show_history(date):
    try:
        path = f"chats/{date}_chat.txt"

        with open(path,"r",encoding="utf-8") as file:
            content = file.read()

        print()
        print(f"History of: {date}")
        print()
        print(content)
        
    except FileNotFoundError:
        print()
        print(f"No history found for {date}.")


def clear_history(session_start):
    try:
        now = datetime.now()
        date = now.strftime("%Y_%m_%d")
        path = f"chats/{date}_chat.txt"

        is_cleared = False

        with open(path,"r",encoding="utf-8") as file:
            content_lines = file.read().split("\n")

            session_start = f"[{session_start}] Session Started"

            for index, line in enumerate(content_lines):
                if session_start == line:
                    if index + 2 >= len(content_lines) or not content_lines[index + 2]:
                        is_cleared = False
                        break
                    content_lines = content_lines[:index + 1]
                    content_lines.append("\n")
                    is_cleared = True
                    break
        if is_cleared:
            with open(path,"w",encoding="utf-8") as file:
                file.write("\n".join(content_lines))
        return is_cleared

    except FileNotFoundError:
        print(f"No history found for {date}")
        return False

def save_chat(session_start):
    try:
        now = datetime.now()
        date = now.strftime("%Y_%m_%d")
        fetch_path = f"chats/{date}_chat.txt"
        session_time = session_start.replace(":","_")
        save_path = f"chats/saved/{date}_{session_time}.txt"

        with open(fetch_path, "r", encoding="utf-8") as file:
            content = file.read()
        content_lines = content.split("\n")

        start_line = f"[{session_start}] Session Started"
        session_chat = []

        for index, line in enumerate(content_lines):
        
            if line == start_line:
                session_chat = content_lines[index:]
                break
        if session_chat:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write("\n".join(session_chat))

            return True
        return False

    except FileNotFoundError:
        print()
        print("File not found..")
        return False