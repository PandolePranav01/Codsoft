def chatbot_response(user_input):
  user_input = user_input.lower()  

  if "hello" in user_input:
      return "Hello! How can I help you today?"
  elif "hi" in user_input:
      return "Hi there! How can I assist you?"
  elif "how are you" in user_input:
      return "I'm just a bot, but I'm doing great! How about you?"
  elif "what is your name" in user_input:
      return "I'm a simple chatbot created by OpenAI. What's your name?"
  elif "bye" in user_input or "goodbye" in user_input:
      return "Goodbye! Have a nice day!"
  elif "help" in user_input:
      return "Sure, I'm here to help! What do you need assistance with?"
  elif "what can you do" in user_input:
      return "I can chat with you and help with simple tasks. What do you need?"
  elif "thank you" in user_input:
      return "You're welcome! If you have any more questions, feel free to ask."
  elif "who created you" in user_input:
      return "I was created by the team at OpenAI to assist with simple tasks and provide information."
  else:
      return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
  print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
  while True:
      user_input = input("You: ")
      if "bye" in user_input.lower():
          print("Chatbot: Goodbye! Have a nice day!")
          break
      response = chatbot_response(user_input)
      print(f"Chatbot: {response}")

if __name__ == "__main__":
  main()
