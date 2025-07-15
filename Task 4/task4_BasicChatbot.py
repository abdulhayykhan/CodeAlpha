def chatbot_response(user_input):
    user_input = user_input.lower()

    # Predefined responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm just a bot, but I'm doing fine! 😄"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple Python chatbot created by you!"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I don't understand that. 🤖"

def main():
    print("💬 Welcome to the Python Chatbot!")
    print("Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit"]:
            break

# Run the chatbot
main()
