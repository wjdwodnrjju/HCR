from tkinter import *
from tkinter import ttk
 
#함수 추가.
def button_pressed(value):
    print(value,"pressed")
     
root = Tk()
root.title("Calculator")
root.geometry("100x100")
 
number_entry = ttk.Entry(root, width=20)
number_entry.grid(row=0, columnspan=1)
 
# command에 함수 연결. 전달값은 버튼의 숫자 '1'
button1 = ttk.Button(root, text="1", command=lambda:button_pressed('1'))
button1.grid(row=1, column=0)
 
root.mainloop()
