import random
print("Welcome to the number guessing game!")
def replaying(replay):
    if replay.lower() == 'y':
        diff_level()
    elif replay.lower() == 'n':
        print("Thank You for playing!")
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
    replay = input("Do you want to play again?(y/n):")
    while replay.lower() != 'y' and replay.lower() != 'n':
            print("Choose either y or n")
            replay = input("Do you want to play again?(y/n):")
    replaying(replay)
def diff_level():
    print("-----LEVELS-----")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    user_choice = int(input("Choose your difficulty!: "))
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
diff_level()