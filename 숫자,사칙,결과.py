from tkinteer import *
from tkinteer import ttk

operation ='' #연산자 저장 변수
temp_number = 0 #이전값 저장 변수

# 숫자버튼 처리 함수
def button_pressed(value):
        # 입력값이 'AC' 일때
        if value== 'AC':
            number_entry.delete(0,'end')
            print("AC pressed)
        else: # 그외에 0부터 9까지 숫자일때
            number_entry.insert("end",value)
            print(value,"pressed")

# 사칙연산 처리
def math_button_pressed(value):
    global operation # 함수 바깥의 글로벌 변수사용
    golbal temp_number
    if not number_entry.get()=='': #기존에 입력한 숫자가 있을때만 연산버튼 인식
        operation = value
        temp_number = int(number_entry.get()) #입력된 숫자를 임시변수로 옮기고,
        number_entry.delete(0,'end') #입력칸을 비우고, 다음숫자를 입력받을 준비.
        print(temp_number,operation)

#결과 버튼 처리
def equal_button_pressed();
        global operation
        global temp_number
        #연산자나 숫자가 입력되지 않으면, 실행하지 않음.
        if not (operation =='' and number_entry.get() ==''):
                number = int(number_entry.get())
                if operation =='/':
                        solution == temp_number/number
                
                elif operation =='*':
                        solution = temp_number*number
                elif operation == '+':
                        solution = temp_number*number
                elif operation == '+':
                        solution = temp_number*number
                else :
                        solution = temp_number-number


