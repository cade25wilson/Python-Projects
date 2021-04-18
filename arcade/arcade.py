
def menu_Screen():
    selection = input("Welcome to the arcade what game would you like to play?\n 1 = hangman \n 2 = number guesser \n 3 = snake\n")
    if selection == '1':
        from hangman_game import hangMan
        hangman()
    elif selection == '2':
        from number_guessing_game import guessingGame
        guessinGame()
    else:
        if selection == '3':
            from snake import gameLoop
            gameLoop()
menu_Screen()



