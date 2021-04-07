#Welcoming users to program
def welcome():
    print('''
Welcome to Calculator
''')

def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplicatioin
    / for division
    ''')

    #asking for input of 2 numbers to perform operations on them
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    #Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    #Subtraction
    elif operation == '-':
        print('{} - {} ='.format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplication
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 * number_2)

    #Division
    elif operation == '/':
        print('{} / {} ='.format(number_1, number_2))
        print(number_1 / number_2)

    #if no operation is entered print this message
    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

#give users option to restart program
def again():

    calc_again = input('''
Do you want to calculate again?
Please type Y for Yes or N for No.
''')

    #if user types Y run the calculate() function adding parameters for error
    if calc_again.upper() == 'Y':
        calculate()

    #if use types N, say good-bye to the user and end the program adding parameters for error
    elif calc_again.upper() == 'N':
        print('See you later.')

    #if user types another key, run the function again
    else:
        again()

#call welcome() from outside the function
welcome()
#call calculate() outside of the function
calculate()

            
