import tkinter as tk
from tkinter import ttk

def main():
	
	root = tk.Tk()
	# entry
	entry = ttk.Entry(root, width = 300, font = ('', 18, ''), justify = 'right')
	# buttons
	b1 = ttk.Button(root, text = '1', width = 5)
	b2 = ttk.Button(root, text = '2', width = 5)
	b3 = ttk.Button(root, text = '3', width = 5)
	plus = ttk.Button(root, text = '+', width = 5)
	equ = ttk.Button(root, text = '=', width = 5)
	clr = ttk.Button(root, text = 'clr', width = 5)
	bs = ttk.Button(root, text = "<-", width = 5)

	# TODO find better way to create buttons
	# for i in range(10) :
	# 	# number = ttk.Button(root, text = str(i), width = 5)
	# 	numbers.append(ttk.Button(root, text = str(i), width = 5))
	# 	print(len(numbers))
	# 	numbers[i].pack()
	# 	numbers[i].config(command = lambda : click(entry, str(i)))



	# set width = 300, height = 500
	root.geometry("300x500")
	# Don't allow resizing in the x or y direction
	root.resizable(0, 0)
	entry.pack()
	entry.state(['readonly'])

	b1.config(command = lambda : click(entry, '1'))
	b2.config(command = lambda : click(entry, '2'))
	b3.config(command = lambda : click(entry, '3'))
	plus.config(command = lambda : click(entry, '3'))
	clr.config(command = lambda : clear(entry))


	b1.pack()
	b2.pack()
	b3.pack()
	plus.pack()
	equ.pack()
	clr.pack()
	bs.pack()


	# infinte loop
	root.mainloop()

# def readonlyDecorator(f) :
# 	def wrapper(*args, **kwargs) :
# 		args[0].state(['!readonly'])
# 		f(iter(list(args)))
# 		args[0].state(['readonly'])
# 	return wrapper


# @readonlyDecorator
def click(e, n):
	e.insert(tk.END, n)


# @readonlyDecorator
def clear(e):
	e.delete(0, tk.END)

if __name__ == "__main__" : main()




