import webbrowser
import os
import tkinter
from tkinter import *

# Creating GUI For user to input what they want on webpage
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Setup')
        self.master.config(bg='blue')

        self.varBody = StringVar()

        self.lblBody = Label(self.master,text='Body: ',font=("Helvetica", 16),bg=('blue'))
        self.lblBody.grid(row=4, column=0, padx=(30,0), pady=(10,0))
        
# Creating text box for user to input data
        self.txtBody = Entry(self.master,text=self.varBody, font=("Helvetica", 16))
        self.txtBody.grid(row=4, column=1, padx=(30,0), pady=(10,0))
#Creating button to initiate process of opening webpage lambda binds 2 functions into single button
        self.btnSubmit = Button(self.master, text="Submit", width= 10, height=2, bg='purple', command=lambda:[self.Write(), self.Submit()])
        self.btnSubmit.grid(row=5, column=0,padx=(30,0), pady=(10,0))
#functions that write what needs to be displayed and to open browser
    def Write(self):
        b = self.varBody.get()
        f = open('challenge.html','w')
        message = """<html>
        <head></head>
        <body>{}</body>
        </html>""".format(b)
        f.write(message)
        f.close()
    
#using cwd() to make sure it opens on any device    
    def Submit(self):
        filename = 'file:///'+os.getcwd()+'/' + 'challenge.html'
        webbrowser.open_new_tab(filename)

if __name__=="__main__":
    root=Tk()
    App = ParentWindow(root)
    root.mainloop()
    
