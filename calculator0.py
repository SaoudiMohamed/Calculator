import tkinter as tk
from tkinter import ttk

# the main programm :
def main():
	
	root = tk.Tk()
	# entry
	entry = ttk.Entry(root, width = 300, font = ('', 18, ''), justify = 'right')
	
  # TODO find better way to create buttons

# Create :
  # numbers :
	b1 = ttk.Button(root, text = '1', width = 5)
	b2 = ttk.Button(root, text = '2', width = 5)
	b3 = ttk.Button(root, text = '3', width = 5)

  # operations :
	bplus = ttk.Button(root, text = '+', width = 5)
	equ = ttk.Button(root, text = '=', width = 5)

  # clear :
	clr = ttk.Button(root, text = 'clr', width = 5)
	bs = ttk.Button(root, text = "<-", width = 5)

# Configure :

	# set width = 300, height = 500
	root.geometry("300x500")
	# Don't allow resizing in the x or y direction
	root.resizable(0, 0)
	entry.pack()
	entry.state(['readonly'])

  # buttons :
	b1.config(command = lambda : b_click(entry, '1'))
	b2.config(command = lambda : b_click(entry, '2'))
	b3.config(command = lambda : b_click(entry, '3'))
	bplus.config(command = lambda : b_click(entry, '+'))
	clr.config(command = lambda : clear(entry))
	bs.config(command = lambda : backspace(entry))
	equ.config(command = lambda : equal(entry))


# Pack :
	b1.pack()
	b2.pack()
	b3.pack()
	bplus.pack()
	equ.pack()
	clr.pack()
	bs.pack()

	# infinte loop
	root.mainloop()


# TODO minimize repetitive code using Decorators

# buttons click command
def b_click(e, n):
  e.state(['!readonly'])
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
  e.state(['!readonly'])
  res = eval(e.get())
  e.delete(0, tk.END)
  e.insert(0, res)
  e.state(['readonly'])



if __name__ == "__main__" : main()