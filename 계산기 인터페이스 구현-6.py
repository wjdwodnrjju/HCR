from tkinter import *
from tkinter import ttk
 
def button_pressed(value):
    number_entry.insert("end",value)
    print(value,"pressed")
     
root = Tk()
root.title("Calculator")
root.geometry("250x200")  # 버튼폭에 맞춰서 확장.
 
entry_value = StringVar(root, value='')
 
number_entry = ttk.Entry(root, textvariable = entry_value, width=20)
number_entry.grid(row=0, columnspan=3) #columnspan 은 여러칸에 걸쳐서 표시함.
 
# button 9개 추가
button7 = ttk.Button(root, text="7", command = lambda:button_pressed('7'))
button7.grid(row=1, column=0)
button8 = ttk.Button(root, text="8", command = lambda:button_pressed('8'))
button8.grid(row=1, column=1)
button9 = ttk.Button(root, text="9", command = lambda:button_pressed('9'))
button9.grid(row=1, column=2)
 
button4 = ttk.Button(root, text="4", command = lambda:button_pressed('4'))
button4.grid(row=2, column=0)
button5 = ttk.Button(root, text="5", command = lambda:button_pressed('5'))
button5.grid(row=2, column=1)
button6 = ttk.Button(root, text="6", command = lambda:button_pressed('6'))
button6.grid(row=2, column=2)
 
button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=3, column=0)
button2 = ttk.Button(root, text="2", command = lambda:button_pressed('2'))
button2.grid(row=3, column=1)
button3 = ttk.Button(root, text="3", command = lambda:button_pressed('3'))
button3.grid(row=3, column=2)
 
root.mainloop()
