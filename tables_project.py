from tkinter import *

root = Tk()


# Defining function on button click
def fetch():
    i = int(entry.get())
    labeltext1.set(("{} * 1 = {}".format(i, i * 1)))
    labeltext2.set(("{} * 2 = {}".format(i, i * 2)))
    labeltext3.set(("{} * 3 = {}".format(i, i * 3)))
    labeltext4.set(("{} * 4 = {}".format(i, i * 4)))
    labeltext5.set(("{} * 5 = {}".format(i, i * 5)))
    labeltext6.set(("{} * 6 = {}".format(i, i * 6)))
    labeltext7.set(("{} * 7 = {}".format(i, i * 7)))
    labeltext8.set(("{} * 8 = {}".format(i, i * 8)))
    labeltext9.set(("{} * 9 = {}".format(i, i * 9)))
    labeltext10.set(("{} * 10 = {}".format(i, i * 10)))


# creating entry box for taking input
entry = Entry(root, bg="black", fg="white")
entry.pack()

# creating buttons
Button(root, text="Go", command=fetch).pack()

# creating label 1
labeltext1 = StringVar()
labeltext1 .set('----')
label = Label(root, textvariable=labeltext1, bg="turquoise")
label.pack()

# creating label 2
labeltext2 = StringVar()
labeltext2.set('----')
label = Label(root, textvariable = labeltext2, bg = "yellow")
label.pack()

# creating label 3
labeltext3 = StringVar()
labeltext3.set('----')
label = Label(root, textvariable = labeltext3, bg = "magenta")
label.pack()

# creating label 4
labeltext4 = StringVar()
labeltext4.set('----')
label = Label(root, textvariable = labeltext4, bg = "sky blue")
label.pack()

# creating label 5
labeltext5 = StringVar()
labeltext5.set('----')
label = Label(root, textvariable = labeltext5, bg = "red")
label.pack()

# creating label 6
labeltext6 = StringVar()
labeltext6.set('----')
label = Label(root, textvariable = labeltext6, bg = "light green")
label.pack()

# creating label 7
labeltext7 = StringVar()
labeltext7.set('----')
label = Label(root, textvariable = labeltext7, bg = "orange")
label.pack()

# creating label 8
labeltext8 = StringVar()
labeltext8.set('----')
label = Label(root, textvariable = labeltext8, bg = "cyan")
label.pack()

# creating label 9
labeltext9 = StringVar()
labeltext9.set('----')
label = Label(root, textvariable = labeltext9, bg = "grey")
label.pack()

# creating label 10
labeltext10 = StringVar()
labeltext10.set('----')
label = Label(root, textvariable = labeltext10, bg = "pink")
label.pack()


root.mainloop()