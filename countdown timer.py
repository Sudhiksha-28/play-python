import time

print("⏱️ PYTHON COUNTDOWN TIMER ⏱️")

# 1. Take user input for how many seconds to count down
seconds = int(input("Enter time in seconds to count down: "))

print("\n🚀 Starting countdown...")

# 2. The range loop runs backwards: starts at 'seconds', stops at 0, steps by -1
for i in range(seconds, 0, -1):
    print(f"⏳ {i} seconds remaining...")
    time.sleep(1) # This forces Python to stop and wait exactly 1 second

print("\n🔔 BEEP BEEP BEEP! Time is up! 🎉")