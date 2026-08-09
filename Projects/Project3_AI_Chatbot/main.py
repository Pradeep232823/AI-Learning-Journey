import helpers
import chatbot
import responses
import random
import history
from datetime import datetime

GOODBYE_INPUTS = ["bye", "goodbye", "see you", "exit"]

COMMANDS_DATA = {
    "help": "Show available commands",
    "history": "Show conversation history",
    "clear": "Clear current conversation",
    "save": "Save conversation",
    "exit": "Exit chatbot"
}

SAVE_INPUTS = ["save", "save chat", "save conversation"]

def main():
    print()
    print("==== Welcome to AI Chatbot ====")
    now = datetime.now()
    session_start = now.strftime("%H:%M:%S")

    history.add_history([session_start,"Session Started"])
    while True:

        user_message = helpers.get_user_input("Hello sir/mam please start conversation or type exit to quit: ")
        normalized_message = user_message.lower()
        if normalized_message == "clear":
            is_cleared = history.clear_history(session_start)
            if is_cleared:
                print()
                print("History Cleared Successfully..")
            else:
                print()
                print("No current session history found.")

            continue

        if normalized_message == "help":
            print()
            print(f"{'Command':<12} {'Description':<30}")
            print("===========================================")
            for command, description in COMMANDS_DATA.items():
                print(f"{command:<9} {':':<2} {description:<30}")
            continue
        
        if normalized_message in GOODBYE_INPUTS:
            print()
            print(random.choice(responses.GOODBYE_RESPONSES))
            print()
            print("Thanks for using AI Chatbot..")
            print()
            break

        if normalized_message in SAVE_INPUTS:
            is_saved = history.save_chat(session_start)
            if is_saved:
                print()
                print("Chat saved successfully..")
            else:
                print()
                print("Unable to save the chat. Please try again..")
            continue

        if normalized_message == "history":
            date = helpers.validate_date("Enter the date to view history: ")
            history.show_history(date)
            continue

        response = chatbot.process_message(normalized_message)
        print()
        print(response)

        history.add_history([user_message, response])

    now = datetime.now()
    session_close = now.strftime("%H:%M:%S")

    history.add_history([session_close,"Session Closed"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nProgram interrupted by user..")
        now = datetime.now()
        session_close = now.strftime("%H:%M:%S")
        history.add_history([session_close,"Session Closed"])
        print()
    except Exception as e:
        print()
        print(f"\nSomething went wrong: {e}")
        print()