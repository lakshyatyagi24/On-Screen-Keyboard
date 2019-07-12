from tkinter import *
import tkinter

Keyboard_App = tkinter.Tk()
Keyboard_App.title("On Screen Keyboard")
Keyboard_App.resizable(0,0)

def select(value):
    if value == "<-":
        entry2 = entry.get()
        pos = entry2.find("")
        pos2=entry2[pos:]
        entry.delete(pos2, tkinter.END)
    elif value == 'SPACE':
        entry.insert(tkinter.END, ' ')
    elif value == 'TAB':
        entry.insert(tkinter.END, '     ')
    else:
        entry.insert(tkinter.END, value)


buttons=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
         'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT', '1', '2', '3', '?', 'SPACE']

#label1=Label(Keyboard_App, text='                                                    ').grid(row=0, columnspan=1)
entry = Entry(Keyboard_App, width = 138)
entry.grid(row = 1, columnspan = 15)

varRow = 2
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if button != 'SPACE':
        tkinter.Button(Keyboard_App, text = button, width=5, bg="#000000", fg='#ffffff', activebackground = "#ffffff", activeforeground = "#000990", relief = 'raised', padx=4, pady=4, bd=4, command=command).grid(row=varRow, column=varColumn)

    if button == 'SPACE':
        tkinter.Button(Keyboard_App, text = button, width=60, bg="#000000", fg='#ffffff', activebackground = "#ffffff", activeforeground = "#000000", relief = 'ridge', padx=4, pady=4, bd=4, command=command).grid(row=6, column= 1, columnspan=16)

    varColumn+=1
    if varColumn > 14 and varRow ==2:
        varColumn = 0
        varRow+=1
    if varColumn > 14 and varRow == 3:
        varColumn = 0
        varRow+=1

lblDisplay=Label(Keyboard_App, text="Program Warehouse", font=('arial', 15, 'bold'), justify =CENTER)
lblDisplay.grid(row=6, column=0, columnspan=4)


Keyboard_App.mainloop()
