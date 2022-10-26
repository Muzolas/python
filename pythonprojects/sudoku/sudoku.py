import sqlite3
from tkinter import *
from time import *
import tkinter as tk


class Sudoku:

    def clear(self):
        pass

    def start(self):
        pass

    def time(self):
        pass

    def scoreboard(self):
        pass

    def number(self):
        pass
    
    main = Tk()
    main.title('Sudoku!')
    main.state('zoomed')
    main.resizable(False, False)

    title = Label(main, text='➤SUDOKU!', font='Times 30 bold')
    title.pack(expand=1, anchor='n')

    squares = Label(main, bg='black')
    squares.place(x=660, y=120)
    
    numbers = Label(main,bg='black',fg='white')
    numbers.place(x=660, y=750)

    for i in range(9):    
        for j in range(9):
            square = Label(master=squares, relief=GROOVE, borderwidth=1,width=9,height=4)
            square.grid(row=i, column=j)
            
        for i in range(1,10):

            number = Button(master=numbers, relief=RAISED, borderwidth=1,fg='white')
            number.grid(row=j,column=i)
            label1 = Label(master=number, text=[i],font="Helvetica 15 bold")
            label1.pack(ipadx=22, ipady=20)
            
    time = Label(main, font='Helvetica 15 bold',
                 bg='gray', text='00.00.00', fg='white')
    time.place(x=900, y=940, height=50, width=120)

    start = Button(main, text='Start!', font='Helvetica 15 bold',
                   fg='White', bg='Green', bd=5, command=start)
    start.place(x=740, y=1000, width=200)

    clear = Button(main, text='Clear', font='Helvetica 15 bold',
                   fg='White', bg='Red', bd=5, command=clear)
    clear.place(x=980, y=1000, width=200)

    name = Entry(main, font='Helvetica 15 bold', bd=5)
    name.place(x=670, y=945, width=200, height=45)

    scoreboard = Button(main, text='Scoreboard', font='Helvetica 15 bold',
                        fg='White', bg='#cff00FF7F', bd=5, command=scoreboard)
    scoreboard.place(x=1050, y=940, width=200)

    mainloop()


sudoku = Sudoku()
