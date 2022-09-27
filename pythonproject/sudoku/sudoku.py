import sys
import sqlite3
from tkinter import *
import tkinter as tk
from time import *

class Window(tk.Tk):

    def __init__(self):

        # self.create_connection()

        def clear(self):
            pass

        def start(self):
            pass

        main = Tk()
        main.title('Sudoku!')
        main.state('zoomed')
        main.resizable(False, False)
        
        title = Label(main, text='➤SUDOKU!', font='Times 20 bold')
        title.pack(expand=1, anchor='n')
        
        start = Button(main, text='Start!', font='Helvetica 15 bold',fg='White', bg='Green', command=start)
        start.place(x=750, y=1000, width=200)

        clear = Button(main, text='Clear', font='Helvetica 15 bold',fg='White', bg='Red', command=clear)
        clear.place(x=970, y=1000, width=200)

        name = Entry(main, font='Helvetica 15 bold')
        name.pack(expand=1, anchor='center')

        for i in range(9):
            for j in range(9):   
                frame = Frame(master=main,relief=FLAT,bd=2)
                frame.grid(row=i, column=j)
                label = Label(master=frame)
                label.pack(side=LEFT)

        mainloop()

    # def create_connection(self):

    #     connection = sqlite3.connect("scoreboard.db")

    #     self.cursor = connection.cursor()
    #     self.cursor.execute("Create Table If not exists users (username TEXT,time Text)")

    #     connection.commit()


window = Window()
