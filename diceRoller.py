#importing module for random number generation
import random

#range of the values of a die
min_val = 1
max_val = 6

#loop the rolling user input
roll_again ="yes"

#numbering dice to add values
die_one = random.randint(min_val, max_val)
die_two = random.randint(min_val, max_val)

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")

    #generating and printing 1st random integer from 1 to 6
    print(die_one)

    #generating and printing 2nd random integer from 1 to 6
    print(die_two)

    #adding total for the user
    s="the total is "
    total=die_one+die_two
    print(s,total)

    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?")
