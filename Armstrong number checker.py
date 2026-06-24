# 🔢 ARMSTRONG NUMBER CHECKER

print("🧮 MATHEMATICAL PROPERTY CHECKER 🧮")

# 1. Take user input and keep a copy as both a string and a number
num_str = input("Enter a positive integer to check: ").strip()

if num_str.isdigit():
    num = int(num_str)
    num_digits = len(num_str)  # Number of digits (e.g., 3 for 153)
    
    # 2. Core math logic loop
    temp = num
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10  # Get the last digit
        sum_of_powers += digit ** num_digits  # Raise digit to the power of total digits
        temp //= 10  # Remove the last digit from temp
        
    # 3. Compare the calculated sum with the original number
    print("\n--- RESULTS ---")
    if num == sum_of_powers:
        print(f"✅ {num} is an Armstrong number!")
        # Breakdown visualization
        breakdown = " + ".join([f"{d}^{num_digits}" for d in num_str])
        print(f"👉 Because {breakdown} = {sum_of_powers}")
    else:
        print(f"❌ {num} is NOT an Armstrong number.")
else:
    print("Invalid input. Please enter a positive whole number.")
