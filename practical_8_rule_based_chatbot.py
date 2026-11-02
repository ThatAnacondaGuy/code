def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower().strip()

        if "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Bot: I am fine! How about you?")

        elif "your name" in user:
            print("Bot: I am Python Chatbot.")

        elif "what is ai" in user:
            print("Bot: AI stands for Artificial Intelligence.")

        elif "python" in user:
            print("Bot: Python is a programming language.")

        elif "thank" in user:
            print("Bot: You're welcome!")

        elif "bye" in user or "exit" in user:
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I didn't understand that.")


chatbot()
