import random

userWins = 0
compWins = 0

options = ["r", "p", "s"]

while True:
    userInput = input("Type R = rock, P = paper, S = scissor, or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    random_num = random.randint(0, 2)  # rock = 0, paper = 1, scissor = 2
    comp_pick = options[random_num]

    print(f"Computer picked {comp_pick} .")

    if userInput == "r" and comp_pick == "s":
        print("You won!")
        userWins += 1
    elif userInput == "p" and comp_pick == "r":
        print("You won!")
        userWins += 1
    elif userInput == "s" and comp_pick == "p":
        print("You won!")
        userWins += 1
    elif userInput == comp_pick:
        print("It's a draw")
    else:
        print("You lost!")
        compWins += 1

print(f"You won {userWins} times")
print(f"Computer won {compWins} times")

print("See you again!")
