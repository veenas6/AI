import re
# Predefined chatbot rules
rules = [
    (r"hello|hi|hey", 
    "Hello! How can I help you?"),
    (r"how are you", 
     "I am fine. Thank you for asking!"),
    (r"what is your name|your name", 
     "My name is SimpleBot."),
    (r"who are you", 
     "I am a simple rule-based chatbot."),
    (r"what can you do|help", 
     "I can answer simple questions using predefined rules."),
    (r"what is artificial intelligence|define ai", 
     "Artificial Intelligence is the simulation of human intelligence in machines."),
    (r"thank you|thanks", 
     "You are welcome!"),
    (r"bye|goodbye|exit", 
     "Goodbye! Have a nice day.")
]
def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    # Check input against predefined patterns
    for pattern, response in rules:
        if re.search(pattern, user_input):
             return response
    # Default response when no pattern matches
    return "Sorry, I don't understand that."
print("===================================")
print("       SIMPLE RULE-BASED CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if re.search(r"bye|goodbye|exit", user_input.lower()):
        break
