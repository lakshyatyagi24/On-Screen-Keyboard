from tkinter import *
import tkinter

Keyboard_App = tkinter.Tk()
Keyboard_App.title("On Screen Keyboard")
Keyboard_App.resizable(0,0)
shift_active=False

def select(value):#made shift work, remove character works now and you add character at cursor position
    global shift_active
    if value == "<-":
        entry_text = entry.get()
        
        
        entry.delete(entry.index(INSERT)-1,entry.index(INSERT))#prolly have to insert try catch for 0-1
    elif value == 'SPACE':
        entry.insert(tkinter.END, ' ')
    elif value == 'TAB':
        entry.insert(tkinter.END, '     ')
    elif value== "SHIFT":
        shift_active= not shift_active
        
    else:
        if value.isalpha:
            if shift_active:
                entry.insert(tkinter.INSERT, value.upper())
            else:
                entry.insert(tkinter.INSERT,value.lower())
        else:
            entry.insert(tkinter.INSERT,value)

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
