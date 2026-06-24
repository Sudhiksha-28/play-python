import random
import time

# 1. A list of possible responses stored as strings
responses = [
    "It is certain! 🟢",
    "Without a doubt! ✅",
    "Reply hazy, try again later... 🟡",
    "Ask again later... ⏳",
    "Don't count on it. ❌",
    "My sources say no. 🔴",
    "Outlook good! 👍",
    "Very doubtful. 🧐"
]

print("🔮 WELCOME TO THE MAGIC 8-BALL 🔮")

while True:
    # 2. Ask the user for a yes/no question
    question = input("\nAsk the 8-Ball a Yes/No question (or type 'exit' to quit): ").strip()
    
    if question.lower() == "exit":
        print("Goodbye! May good fortune follow you! 🌟")
        break
        
    if question:
        print("🤔 Consulting the mystical spirits...")
        time.sleep(1.5)  # Adds a realistic delay dramatic effect
        
        # 3. Pick a random item out of the responses array
        prediction = random.choice(responses)
        print(f"🔮 The 8-Ball says: {prediction}")
    else:
        print("You must ask a question to get an answer!")