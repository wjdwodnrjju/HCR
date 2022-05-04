# 숫자버튼 처리 함수
def button_pressed(value):
        # 입력값이 'AC' 일때
        if value== 'AC':
            number_entry.delete(0,'end')
            print("AC pressed)
        else: # 그외에 0부터 9까지 숫자일때
            number_entry.insert("end",value)
            print(value,"pressed")
