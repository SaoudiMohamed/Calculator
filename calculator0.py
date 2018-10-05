import tkinter as tk
from tkinter import ttk

errorHappened = False

# the main programm :


def main():

    root = tk.Tk()
    # entry
    entry = ttk.Entry(root, font=('', 18, ''), justify='right')

    # TODO find better way to create buttons

# Create :
    # numbers :
    b0 = ttk.Button(root, text='0', width=3)
    b1 = ttk.Button(root, text='1', width=3)
    b2 = ttk.Button(root, text='2', width=3)
    b3 = ttk.Button(root, text='3', width=3)
    b4 = ttk.Button(root, text='4', width=3)
    b5 = ttk.Button(root, text='5', width=3)
    b6 = ttk.Button(root, text='6', width=3)
    b7 = ttk.Button(root, text='7', width=3)
    b8 = ttk.Button(root, text='8', width=3)
    b9 = ttk.Button(root, text='9', width=3)

    # operations :
    bplus = ttk.Button(root, text='+', width=3)
    bminus = ttk.Button(root, text='-', width=3)
    btimes = ttk.Button(root, text='*', width=3)
    bdiv = ttk.Button(root, text='/', width=3)
    equ = ttk.Button(root, text='=', width=3)
    lpar = ttk.Button(root, text='(', width=3)
    rpar = ttk.Button(root, text=')', width=3)
    point = ttk.Button(root, text='.', width=3)

    # clear :
    clr = ttk.Button(root, text='clr', width=4)
    bs = ttk.Button(root, text="<-", width=3)

# Configure :

    # set width = 300, height = 500
    # root.geometry("300x500")
    # Don't allow resizing in the x or y direction
    root.resizable(0, 0)
    entry.grid(row=0, column=0, columnspan=4)
    entry.state(['readonly'])

    # buttons :
    b0.config(command=lambda: b_click(entry, '0'))
    b1.config(command=lambda: b_click(entry, '1'))
    b2.config(command=lambda: b_click(entry, '2'))
    b3.config(command=lambda: b_click(entry, '3'))
    b4.config(command=lambda: b_click(entry, '4'))
    b5.config(command=lambda: b_click(entry, '5'))
    b6.config(command=lambda: b_click(entry, '6'))
    b7.config(command=lambda: b_click(entry, '7'))
    b8.config(command=lambda: b_click(entry, '8'))
    b9.config(command=lambda: b_click(entry, '9'))

    bplus.config(command=lambda: b_click(entry, '+'))
    bminus.config(command=lambda: b_click(entry, '-'))
    btimes.config(command=lambda: b_click(entry, '*'))
    bdiv.config(command=lambda: b_click(entry, '/'))
    lpar.config(command=lambda: b_click(entry, '('))
    rpar.config(command=lambda: b_click(entry, ')'))
    point.config(command=lambda: b_click(entry, '.'))

    equ.config(command=lambda: equal(entry))

    clr.config(command=lambda: clear(entry))
    bs.config(command=lambda: backspace(entry))


# Grid :
    b0.grid(row=5, column=0, sticky='nsew')
    b1.grid(row=4, column=0, sticky='nsew')
    b2.grid(row=4, column=1, sticky='nsew')
    b3.grid(row=4, column=2, sticky='nsew')
    b4.grid(row=3, column=0, sticky='nsew')
    b5.grid(row=3, column=1, sticky='nsew')
    b6.grid(row=3, column=2, sticky='nsew')
    b7.grid(row=2, column=0, sticky='nsew')
    b8.grid(row=2, column=1, sticky='nsew')
    b9.grid(row=2, column=2, sticky='nsew')

    bplus.grid(row=2, column=3, sticky='nsew')
    bminus.grid(row=3, column=3, sticky='nsew')
    btimes.grid(row=4, column=3, sticky='nsew')
    bdiv.grid(row=5, column=3, sticky='nsew')
    lpar.grid(row=1, column=0, sticky='nsew')
    rpar.grid(row=1, column=1, sticky='nsew')
    point.grid(row=5, column=1, sticky='nsew')
    equ.grid(row=5, column=2, sticky='nsew')

    clr.grid(row=1, column=3, sticky='nsew')
    bs.grid(row=1, column=2, sticky='nsew')

    # infinte loop
    root.mainloop()


# TODO minimize repetitive code using Decorators

# buttons click command
def b_click(e, n):
    global errorHappened
    e.state(['!readonly'])
    if errorHappened:
        e.delete(0, tk.END)
        errorHappened = False
        e.config(foreground='black')
    e.insert(tk.END, n)
    e.state(['readonly'])

# clear command


def clear(e):
    e.state(['!readonly'])
    e.delete(0, tk.END)
    e.state(['readonly'])

# backspace command


def backspace(e):
    e.state(['!readonly'])
    e.delete(len(e.get())-1)
    e.state(['readonly'])

# equal command


def equal(e):
    global errorHappened
    e.state(['!readonly'])
    try:
        res = eval(e.get())
        e.delete(0, tk.END)
        e.insert(0, res)
    except:
        e.delete(0, tk.END)
        e.config(foreground='red')
        e.insert(0, 'ERROR')
        errorHappened = True
        # e.config(foreground='black')
    e.state(['readonly'])


if __name__ == "__main__":
    main()
