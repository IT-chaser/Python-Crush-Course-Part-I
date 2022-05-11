def send_messages(messages_list):
    sent_messages = []
    for message in messages_list:
        print(message.title())
    while messages_list:
        sending_message = messages_list.pop()
        sent_messages.append(sending_message)
    print(f"send message: {messages_list}")
    print(f"sent mesages list: {sent_messages}")
messages = ['hello world!', 'nice to meet you!', 'thank you!', 'welcome!']
send_messages(messages)
