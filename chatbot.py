
def chatbot():
    print("🤖 Welcome to Simple Chatbot! (Type 'exit' to quit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
        elif user_input == "exit":
            print("Bot: Session ended. See you next time!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
