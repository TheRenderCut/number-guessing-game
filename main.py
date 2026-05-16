import random
print("Welcome to the number guessing game!")
print("-----LEVELS-----")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")
user_choice = int(input("Choose your difficulty!: "))
def guess(user_num, sys_num):
    counter = 1
    while user_num != sys_num:
        counter += 1
        if user_num > sys_num:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        user_num = int(input("Enter your number again!: "))
    print("Congratulations! You guessed the number correctly.")
    print(f"You guessed the number in {counter} times!")
match user_choice:
    case 1:
        print("Welcome to EASY MODE!")
        user_num = int(input("Please enter a number between 1 to 10: "))
        sys_num = random.randint(1, 10)
        guess(user_num, sys_num)
    case 2:
        print("Welcome to MEDIUM MODE!!")
        user_num = int(input("Please enter a number between 1 to 50: "))
        sys_num = random.randint(1, 50)
        guess(user_num, sys_num)
    case 3:
        print("Welcome to HARD MODE!!!")
        user_num = int(input("Please enter a number between 1 to 100: "))
        sys_num = random.randint(1, 100)
        guess(user_num, sys_num)
    case _:
        print("Choose between 1, 2 and 3!")