# 클래스 생성

class Person:           # 클래스 선언
    name = '익명'       # 속성 변수
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가(__init__)
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    # 재정의(overriding) : 원하는 기능으로 변경
    def __init__(self, name = '홍길동', height = 170, gender = 'male'): # 매개변수(파라미터) 기본값
        self.name = name            # self.속성변수 = 매개변수
        self.height = height
        self.gender = gender      

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자 외 매직메서드(함수) ex) __str__
    def __str__(self) -> str:              # string값으로 return 받음
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'
    
donghun = Person('이동훈',170,'male')  # 이렇게 만들어진 객체를 instance라 한다. # 객체 생성.
# donghun.name = '이동훈'
# donghun.height = '170'
# donghun.gender = 'male'
# donghun.blood_type = 'RH+ A'

print(f'{donghun.name}의 혈액형은 {donghun.blood_type}입니다.')

donghun.run('Fast')
print(donghun)

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)

print('==========================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)

print(ashely)
