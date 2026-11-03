def send_messages(messages, sent_messages):
    """Print each message and move it to the sent list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)
 
 
texts = ['Hello!', 'How are you?', 'See you tomorrow.']
sent_messages = []
 
send_messages(texts, sent_messages)
 
print(f"\ntexts: {texts}")
print(f"sent_messages: {sent_messages}")