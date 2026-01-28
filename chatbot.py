print("Chatbot: Hello! Type 'exit' to end the chat.")
name=""
while True:
    user = input("You: ").lower()
    if user == "exit":
        print("chatbot: Googbye👋")
        break
    elif "my name is" in user:
        name=user.replace("my name is", "").strip()
        print(f"chatbot: Nice to meet you, {name}!")
    elif user == "help":
        print("Chatbot: I can respond to: hi, hello, how are you, who are you, bye, help, exit, and your name.")
    elif "hi" in user or "hello" in user:
        print("chatbot: Hello😊")
    elif "who are you" in user:
        print("chatbot: I'm your personal assistant")
    elif "how are you" in user:
        print("chatbot: I'm fine thanks for asking!")
    elif "bye" in user:
        print("chatbot: Take care! 👋")
    else:
        print("chatbot: sorry, i don't understand that.")




