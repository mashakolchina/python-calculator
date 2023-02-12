from tkinter import *
from tkinter import messagebox
from tkinter import font

def logical(operation):
    if operation == 'c':
        lbl['text'] = '0'
    elif operation == 'DEL':
        lbl ['text'] = lbl ['text'][0:-1]
    elif operation == 'X^2':
        lbl['text'] = str(eval(lbl['text']) ** 2)
    elif operation == '=':
        lbl['text'] = str(eval(lbl['text']))
    else:
        if lbl['text'] == '0':
            lbl['text'] = ' '
        lbl['text'] = lbl['text'] + operation


root = Tk()
root.title('Мини-калькулятор')
root.geometry('485x550')
root['bg'] = 'black'
lbl = Label(root, text='0', bg='black', fg='white', font=('Consolas', 21, 'bold'))
lbl.place(x=11, y=50)
btns = [
        'c', 'DEL', '*', '=',
        '1', '2', '3', '/',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        '(', '0', ')', 'X^2']
x = 10
y = 140
for bt in btns:
    def com(x=bt):
        logical(x)
    Button(text=bt, bg='white', font=('Consolas', 15), command=com).place(x=x, y=y, width=115, height=79)
    x +=117
    if x > 400:
        x = 10
        y +=81
root.mainloop()



