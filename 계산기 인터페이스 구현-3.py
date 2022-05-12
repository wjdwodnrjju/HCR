
from tkinter import *
from tkinter import ttk
 
 
root = Tk()
root.title("Calculator")
root.geometry("100x100")
 
number_entry = ttk.Entry(root, width=20)
number_entry.grid(row=0, columnspan=1)
 
# command=lambda: 뒤에 명령 작성.
button1 = ttk.Button(root, text="1", command=lambda:print("button 1"))
button1.grid(row=1, column=0)
 
root.mainloop()
