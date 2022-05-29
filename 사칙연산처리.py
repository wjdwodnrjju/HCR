# 사칙연산 처리
def math_button_pressed(value):
    global operation # 함수 바깥의 글로벌 변수사용
    golbal temp_number
    if not number_entry.get()=='': #기존에 입력한 숫자가 있을때만 연산버튼 인식
        operation = value
        temp_number = int(number_entry.get()) #입력된 숫자를 임시변수로 옮기고,
        number_entry.delete(0,'end') #입력칸을 비우고, 다음숫자를 입력받을 준비.
        print(temp_number,operation)
