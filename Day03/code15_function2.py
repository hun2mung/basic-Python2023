# 함수

# 함수, 파라미터, 리턴 (4가지 만드는 방법)
# 1. 파라미터 o, 리턴 o
# 2. 파라미터 o, 리턴 x
# 3. 파라미터 x, 리턴 o
# 4. 파라미터 x, 리턴 x

# 함수 정의 - 실행 x
def add(x, y):  
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def hello():
    print('Hello~!!!')

def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수 호출
hello()
print(hello2())

add(1024, 5)
sub(1024, 100)
mul(512, 2)
div(108, 10)
