import sqlite3
from tkinter import *
from time import *


def clear():
    pass


def start():
    pass

def time():
    pass

main = Tk()
main.title('Sudoku!')
main.state('zoomed')
main.resizable(False, False)

title = Label(main, text='➤SUDOKU!', font='Times 30 bold')
title.pack(expand=1, anchor='n')

squares = Label(main, width=100, height=100, bg='black')
squares.place(x=660, y=120)

for i in range(9):
    for j in range(9):
        frame = Frame(master=squares, relief=GROOVE, borderwidth=1)
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=f'0')
        label.pack(padx=25, pady=25)

time = Label(main,font='Helvetica 15 bold',bg='gray',text='00.00.00',fg='white')
time.place(x=900, y=940,height=50,width=120)

start = Button(main, text='Start!', font='Helvetica 15 bold',
               fg='White', bg='Green', bd=5,command=start)
start.place(x=740, y=1000, width=200)

clear = Button(main, text='Clear', font='Helvetica 15 bold',
               fg='White', bg='Red' ,bd=5,command=clear)
clear.place(x=980, y=1000, width=200)

name = Entry(main, font='Helvetica 15 bold',bd=5)
name.place(x=670, y=945, width=200, height=45)

scoreboard = Button(main, text='Scoreboard', font='Helvetica 15 bold',
                    fg='White', bg='#cff00FF7F',bd=5, command=time)
scoreboard.place(x=1050, y=940, width=200)

mainloop()
