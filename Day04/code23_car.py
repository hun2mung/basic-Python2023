# 자동차 클래스


class Car:                      # 초록색은 클래스
    __number = ' 54라 1234 '    # 캡슐화(encapsulaiton)

    def get_number(self) -> str:
        return self.__number

    # 클래스 외부에선 변경X, 멤버함수로는 내부 조작O
    def set_number(self, number):
        self.__number = number
    
    def __init__(self, number = '54라 1234') -> None:
        print('__init__')
        self.__number = number

    # def __new__(cls):               
    #     print('__new__')
    #     return super().__new__(cls)     # 부모클래스(상속) / super -> 부모
    
    def __str__(self) -> str:
        return f'차번호는 {self.__number}입니다'

yourcar = Car('88호 1234')
print(yourcar)
yourcar.__number = '11가1111'   # 외부에서는 멤버변수에 접근불가
print(yourcar)

print('클래스 내부함수 사용!')
yourcar.set_number('22나2222')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는요, 아이오닉이고, 번호는 {mycar.get_number()}입니다.')

mycar.__number = '123가 6789'
print(mycar)
print(mycar.get_number())