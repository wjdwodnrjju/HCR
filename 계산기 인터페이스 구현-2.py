from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("100x100")

#숫자, 결과 표시창.
number_entry = ttk.Entry(root, width=20)
number_entry.grid(row=0, columnspan=1)

#숫자 버튼.
button1 = ttk.Button(root, text="1")
button1.grid(row=1, column=0)

root.mainloop()
