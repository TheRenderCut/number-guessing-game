import random
counter = 1
print("Welcome to the number guessing game!")
user_num = int(input("Please enter a number between 1 to 10: "))
sys_num = random.randint(1, 10)
while user_num != sys_num:
    counter += 1
    if user_num > sys_num:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    user_num = int(input("Please enter a number between 1 to 10: "))    
print("Congratulations! You guessed the number correctly.")
print(f"You guessed the number in {counter} times!")