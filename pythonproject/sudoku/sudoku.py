import tkinter as tk

main=tk.Tk()

main.title('Sudoku!')
label = tk.Label(main,text = '➤SUDOKU!',font='Times 20 bold')
main.state('zoomed')
label.pack()
main.resizable(False,False)

def start():
    pass

def clear():
    pass

start=tk.Button(main,text='Start!',font='Helvetica 15 bold',fg='White',bg='Green',command = start)
start.place(x=800,y=1000)

clear=tk.Button(main,text='Clear',font='Helvetica 15 bold',fg='White',bg='Red',command = clear)
clear.place(x=1150,y=1000)

name=tk.Entry(main,font='Helvetica 15 bold')
name.place(x=900,y=1000,height='40')

main.mainloop()
