import random
import time

name = input("What is your name? ")
print("Hello, " + name.capitalize(), "Time to play hangman!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

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
              print("You Loose")

        
