import random
import time

name = input("What is your name? ")
time.sleep(1)
print("Hello, " + name.capitalize(), "Time to play hangman! let me think of a word.")
time.sleep(3)


def hang_Man():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks', "rice", "chickpeas", "pulses", "bread", "meat",
             "milk", "bacon", "eggs", "sauce",
             "Chicken", "apple", "pudding", 'orange', 'pear', 'banana', 'kiwi', 'banana']
    word = random.choice(words)
    print("Guess the letters in the word")
    guesses = ''
    turns = len(word) + 3
    
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed +=1
                
        if failed ==0:
            print("You Win")
            print("The word is: ",word)
            break
        
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more tries')
            if turns == 0:
                  print("You Lose the word was",word)        
                  
    repeat = input("Would you like to play again?\n Press Y for Yes, N for No, and M for Menu: ")
    error_Check = repeat.upper()
    if error_Check == 'Y':
        hang_Man()
    elif error_Check == 'N':
        print("Thanks for playing!")
        quit()
    elif error_Check == 'M':
        from arcade import menu_Screen
        menu_Screen()
    else:
        repeat


hang_Man()
    
        
        
