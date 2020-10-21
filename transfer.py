import tkinter
from tkinter import *
import time
import shutil
import os

class ParentWindow(Frame):
    def __init__ (fname, master):
        Frame.__init__ (fname)

        fname.master = master
        fname.master.resizable(width=True, height =True)
        fname.master.geometry('{}x{}'.format(830, 120)) 
        fname.master.title('Copy-Move GUI') 
        fname.master.config(bg = 'blue')

        fname.sourceLocation = StringVar()
        fname.destinationLocation = StringVar()
        
        fname.link_Label = Label(fname.master, text ="Enter folder path to check : ",bg = "white") 
        fname.link_Label.grid(row = 1, column = 0,pady = 5, padx = 5) 
        
        fname.sourceText = Entry(fname.master, width = 50,textvariable = fname.sourceLocation) 
        fname.sourceText.grid(row = 1, column = 1,pady = 5, padx = 5,columnspan = 2) 
        
        fname.destinationLabel = Label(fname.master, text ="Enter folder destination  : ",bg ="white") 
        fname.destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5) 
        
        fname.destinationText = Entry(fname.master, width = 50,text = fname.destinationLocation) 
        fname.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5,columnspan = 2) 
        
        fname.moveButton = Button(fname.master, text ="Move File", width = 15, command=fname.last_mod_time) 
        fname.moveButton.grid(row = 3, column = 2, pady = 5, padx = 5) 

#========================================================================================================


    def last_mod_time(fname):
        n = fname.sourceLocation.get()
        s = fname.destinationLocation.get()
        secondsinDay = 24*60*60
        src = '{}'.format(n)
        dst = '{}'.format(s)
        now = time.time()
        before = now - secondsinDay
        return os.path.getmtime(fname)

        for fname in os.listdir(src):
            src_fname = os.path.join(src, fname)
            if last_mod_time(src_fname) > before:
                dst_fname = os.path.join(dst, fname)
                shutil.move(src_fname, dst_fname)

if __name__=="__main__":
    root=Tk()
    App = ParentWindow(root)
    root.mainloop()
