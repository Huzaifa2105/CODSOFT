def chat_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello!!!,how can i assist you?"
    elif "what is your name" in user_input:
        return "I am a chatbot , to assist and help you here"
    elif "how are you" in user_input:
        return "I am Good , how about you"
    elif "help" in user_input:
        return "sure! how can i help you"
    elif "bye" in user_input:
        return "bye bye"
    else:
        return "I am sorry, I didn't get you properly"
while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("bot : Goodbye , see you soon!")
        break
    response = chat_response(user_input)
    print("bot:",response)