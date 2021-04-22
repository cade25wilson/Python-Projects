from tkinter import *
import tkinter as tk
from tkinter import messagebox


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 230)
        self.master.maxsize(500, 230)
        self.master.title("Auto Move File")
        self.master.configure(bg="blue")
        
        self.found_source = StringVar()
        self.found_source.set('Hangman')
        self.txt_source = tk.Entry(self.master, width=60, textvariable=self.found_source)
        self.txt_source.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

        self.found_dest = StringVar()
        self.found_dest.set('GuessingGame')
        self.txt_dest = tk.Entry(self.master, width=60, textvariable=self.found_dest)
        self.txt_dest.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

        self.found_dest = StringVar()
        self.found_dest.set('Snake')
        self.txt_dest = tk.Entry(self.master, width=60, textvariable=self.found_dest)
        self.txt_dest.grid(row=2, column=1, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

        self.btn_word = tk.Button(self.master, width=12, height=1, text="Play", command= self.word_Guess)
        self.btn_word.grid(row=0, column=3, padx=(10, 0), pady=(10, 20))

        self.btn_num = tk.Button(self.master, width=12, height=1, text="Play",command= self.guessing_Game2)
        self.btn_num.grid(row=1, column=3, padx=(10, 0), pady=(10, 20))
        
        self.btn_transfer = tk.Button(self.master, width=12, height=1, text="Play",command= self.snake2)
        self.btn_transfer.grid(row=2, column=3, padx=(10, 0), pady=(10, 20))

    def word_Guess(self):
        from hangman_game import hangMan
        hangman()

    def guessing_Game2(self):
        from number_guessing_game import guessinGame
        guessinGame()

    def snake2(self):
        from snake import gameLoop
        gameloop()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
