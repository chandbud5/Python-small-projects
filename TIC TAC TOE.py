# IMPROVEMENTS NEEDED

# CREATE MENU FOR QUIT AND NEW GAME, UNDO, REDO

# INVALID IF PLAYER SELECT PREVIOUSLY SELECTED BOX




# Tic Tak Toe Game


from tkinter import *
from tkinter import messagebox

root = Tk()

# Entry box to write your name
label = Label(root,text="TIC TAC TOE GAME",bg="black",fg="white")
label.grid(row=0,column=2,ipadx=5, ipady=15,padx=8,pady=18)

label1 = Label(root,text="Player 1",bg="light green")
label1.grid(row=1,column=1,sticky=E,ipady=9)

entry1 = Entry(root,bg = "orange",fg = "blue")
entry1.grid(row = 1, column =2,ipady=10, sticky=W+E)


label2 = Label(root,text="Player 2",bg="light green")
label2.grid(row=2,column=1,sticky=E,ipady=9)

entry2 = Entry(root,bg = "orange", fg="blue")
entry2.grid(row=2, column=2,ipady=10, sticky=W+E)

def namecheck():
    if entry2.get()=="":
        messagebox._show("Error","Please enter the player name")


# Defining Function when button pressed

player = 1


def buttonpressed1():
    global player
    if player == 1:
        button1.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button1.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed2():
    global player
    if player == 1:
        button2.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button2.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed3():
    global player
    if player == 1:
        button3.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button3.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed4():
    global player
    if player == 1:
        button4.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button4.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed5():
    global player
    if player == 1:
        button5.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button5.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed6():
    global player
    if player == 1:
        button6.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button6.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed7():
    global player
    if player == 1:
        button7.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button7.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed8():
    global player
    if player == 1:
        button8.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button8.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

def buttonpressed9():
    global player
    if player == 1:
        button9.config(text="X", fg="red")
        player = 2
    elif player == 2:
        button9.config(text="O", fg="Blue")
        player = 1
    namecheck()
    check()

# Defining Checking Function

def check():
    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):


        messagebox._show("CONGRATS", "{} is the winner".format(entry1.get()))

    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):


        messagebox._show("CONGRATS","{} is the winner".format(entry2.get()))


# Defining All 9 Buttons


button1 = Button(root, text="", bg="White", command = buttonpressed1)
button1.grid(row=3, column=1, ipadx=60, ipady=40)

button2 = Button(root, text="", bg="White", command = buttonpressed2)
button2.grid(row=3, column=2, ipadx=60, ipady=40)

button3 = Button(root, text="", bg="White", command = buttonpressed3)
button3.grid(row=3, column=3, ipadx=60, ipady=40)

button4 = Button(root, text="", bg="White", command = buttonpressed4)
button4.grid(row=4, column=1, ipadx=60, ipady=40)

button5 = Button(root, text="", bg="White", command = buttonpressed5)
button5.grid(row=4, column=2, ipadx=60, ipady=40)

button6 = Button(root, text="", bg="White", command = buttonpressed6)
button6.grid(row=4, column=3, ipadx=60, ipady=40)

button7 = Button(root, text="", bg="White", command = buttonpressed7)
button7.grid(row=5, column=1, ipadx=60, ipady=40)

button8 = Button(root, text="", bg="White", command = buttonpressed8)
button8.grid(row=5, column=2, ipadx=60, ipady=40)

button9 = Button(root, text="", bg="White", command = buttonpressed9)
button9.grid(row=5, column=3, ipadx=60, ipady=40)


root.mainloop()