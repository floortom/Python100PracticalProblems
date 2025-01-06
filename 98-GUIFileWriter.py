from tkinter import *

window = Tk()

file = open("guiWriter.txt", "a+")

def add():
    file.write(userValue.get() + "\n")
    entry.delete(0, END)

def save():
    global file
    file.close()
    file = open("guiWriter.txt", "a+")

def close():
    file.close()
    window.destroy()

userValue = StringVar()
entry = Entry(textvariable=userValue)
entry.grid(row=0, column=0)

buttonAdd = Button(window, text="Add line", command=add)
buttonAdd.grid(row=0, column=1)

buttonSave = Button(window, text="Save", command=save)
buttonSave.grid(row=0, column=2)

buttonClose = Button(window, text="Close", command=close)
buttonClose.grid(row=0, column=3)

window.mainloop()
