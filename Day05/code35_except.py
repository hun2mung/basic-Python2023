# 예외
# 오류 검거 - 디버깅, 예외 검거 - 예외 처리

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

try :
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:        # exit()있어도 실행되고 종료됨
    print('계속 되나요?')
# 원시적인 예외처리
# if y == 0 :
#     print('y에 0을 넣지마세요')
#     exit()

print('테스트')
try:
    print(div(x, y))
# except ZeroDivisionError as e:    # 굳이 여러 예외처리 사용X
#     print('0으로 나누면 안되요!')
except Exception as e:      # 평상 시 사용. 여러 사용 시 항상 제일 마지막에 해야됨
    print(e)
finally:        # 예외가 발생되도 무조건 실행
    print('계산은 계속됩니다!!')
print(add(x, y))
print(mul(x, y))
