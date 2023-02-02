# 자료형

# None => 값이 없는 값(파이썬에선 NULL 대신 사용) 
None    # 컴퓨터왈 난몰라
print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))    # 정수형 타입 출력

val = 3.14
print(type(val))    # 실수형 타입 출력

val = 'Hello'
print(type(val))    # 문자열 타입 출력

val = 0b1010        # 2진수 표현
print(type(val))    # 정수형 타입 출력

val = 12.234234234234234234234234
print(type(val))

val = 4_520_000
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Life is short, You need Python'
print(val)
print(type(val))

# 탈출문자
val = 'Hell\nWorld!'    # \n => 한 줄 띄어쓰기
print(val)
val = 'Hell\tWorld!'    # \t => tab만큼 간격 띄우기
print(val)
val = 'Hell\t\bWorld!'  # \b => 한 칸 땡기기
print(val)
# ''' 사용 시 다음 줄에서도 이어서 쓰기 가능
val = '''Life is short, 
You need Python'''
print(val)

val = "Hi, I'm 'DongHun'"       # 같은 역할, 유용한 사용 방법
print(val)
val = 'Hi, I\'m \'DongHun\''
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1))  # 1 == True
print(bool(0))  # 0 == False
print(bool(2))  # 2 == True, 1이외의 값은 True라고 x(True라고 뜨긴 함)


