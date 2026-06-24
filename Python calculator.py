# 🧮 MENU-DRIVEN CALCULATOR

# Define individual functions for each math action
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("🔢 WELCOME TO THE PYTHON CALCULATOR 🔢")

while True:
    print("\n--- OPERATIONS ---")
    print("1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)\n5. Exit")
    
    choice = input("Select an operation (1-5): ")
    
    if choice == "5":
        print("Goodbye! Thanks for using the calculator. 👋")
        break
        
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\n--- RESULT ---")
        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Choice. Please choose a valid option.")