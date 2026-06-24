# 🔄 PALINDROME WORD CHECKER

print("🔀 WELCOME TO THE PALINDROME CHECKER 🔀")

# 1. Take a word from the user and clean it up
word = input("Enter a single word: ").strip().lower()

if word.isalpha():  # Ensures the user typed letters, not numbers
    # 2. Reverse the string using Python's slice step index [::-1]
    reversed_word = word[::-1]
    
    print(f"\nOriginal: {word}")
    print(f"Backward: {reversed_word}")
    
    # 3. Check if they match
    print("\n--- RESULT ---")
    if word == reversed_word:
        print(f"✅ Wow! '{word}' is a palindrome!")
    else:
        print(f"❌ '{word}' is NOT a palindrome.")
else:
    print("Please enter a valid word containing only letters.")