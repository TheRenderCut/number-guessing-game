import random
print("Welcome to the number guessing game!")
user_num = int(input("Please enter a number between 1 to 10: "))
sys_num = random.randint(1,10)
if user_num == sys_num:
    print("CORRECT! You guessed the number.")
else:
    print("WRONG! The correct number was", sys_num)