from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


import datetime
import os
import shutil
import sqlite3
import time

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 230)
        self.master.maxsize(500, 230)
        self.master.title("Auto Move File")
        self.master.configure(bg="blue")
        
        self.found_source = StringVar()
        self.found_source.set('Source directory')
        self.txt_source = tk.Entry(self.master, width=60, textvariable=self.found_source)
        self.txt_source.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

        self.found_dest = StringVar()
        self.found_dest.set('Destination directory')
        self.txt_dest = tk.Entry(self.master, width=60, textvariable=self.found_dest)
        self.txt_dest.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

        self.btn_source = tk.Button(self.master, width=12, height=1, text="Browse..", command= self.get_source)
        self.btn_source.grid(row=0, column=3, padx=(10, 0), pady=(10, 20))

        self.btn_dest = tk.Button(self.master, width=12, height=1, text="Browse..",command=self.get_dest)
        self.btn_dest.grid(row=1, column=3, padx=(10, 0), pady=(10, 20))
        
        self.btn_transfer = tk.Button(self.master, width=16, height=2, text="Transfer Files",
                                    command=lambda: self.move_files(self.found_source, self.found_dest))
        self.btn_transfer.grid(row=2, column=2, padx=(0, 0), pady=(10, 10))


    def get_source(self):
        self.txt_source.delete(0, 60)
        self.found_source = filedialog.askdirectory()
        self.txt_source.insert(0, self.found_source)


    def get_dest(self):
        self.txt_dest.delete(0, 60)
        self.found_dest = filedialog.askdirectory()
        self.txt_dest.insert(0, self.found_dest)


    def move_files(self, source, destination):
        now = datetime.datetime.now()
        ago = now - datetime.timedelta(hours=24)
        print('The following .txt files were modified in the last 24 hours: \n')

        for files in os.listdir(source):
            if files.endswith('.txt'):
                path = os.path.join(source, files)
                st = os.stat(path)
                mtime = datetime.datetime.fromtimestamp(st.st_mtime)
                if mtime > ago:
                    print('{} ~ last modified {}'.format(path, mtime))
                    file_source = os.path.join(source, files)
                    file_destination = os.path.join(destination, files)
                    shutil.move(file_source, file_destination)
                    print("\tMoved {} to {}.\n".format(files, destination))






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
