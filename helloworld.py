print("Chatbot:Hello! i am a simple chatbot.")
print("Type 'bye' to end the chat.\n")
while True:
    user_input = input("You:").lower()
    if user_input == "hello" or user_input == "hi" or user_input == "heyy":
        print("chatbot:hello how can i help you?")
    elif "your name" in user_input:
     print("chatbot: my name is simplebot.")
    elif "how are you" in user_input:
     print("Chatbot: i am fine. Thank you for asking!")
    elif "time" in user_input:
       import datetime
       current_time = datetime.datetime.now().strftime("%H:%M:%S")
       print("Chatbot: Currenrt time is",current_time)
    elif "help" in user_input:
     print("Chatbot: You can ask me about greetings, my name,or the time.")
    elif user_input == "bye":
     print("chatbot: goodbye! have a nice day.")
     break
    else:
     print("chatbot:sorry, i don't understand that.")
