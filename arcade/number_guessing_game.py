import random

def guessingGame():
    random_number = random.randint(1,100)
    win = False
    turns = 0
    attempts = 0
    name = input("Please enter your name: \n")
    while win == False:
        user_Guess = input("enter a number between 1 and 100: ")
        turns +=1
        if random_number ==int(user_Guess):
            print("You Won!")
            print("Number of turns you used: ",turns)
            win == True
            break
        else:
            if random_number>int(user_Guess):
                print("Your guess was low please enter a higher number")
            else:
                print("Your guess was high, please enter a lower number")

    f = open("number_guess_highscore.txt", "a")
    f.write("\n")
    f.write(str(turns))
    f.write(" ")
    f.write(name.capitalize())
    f.close()
    user_Answer = input("Would you like to play again? Y = Yes, N = No\n")
    error_Check = user_Answer.upper()
    if error_Check == 'Y':
        guessingGame()
    elif error_Check =='N':
        print("thanks for playing!")
        quit()
    else:
        print("Please enter a 'Y' or 'N'")
        user_Answer

guessingGame()
