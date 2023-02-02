# 클래스 생성

class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    def walk(self):
        print('걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')
    
    def stop(self):
        print('멈춥니다.')
    
donghun = Person()  # 이렇게 만들어진 객체를 instance라 한다.
donghun.name = '이동훈'
donghun.height = '170'
donghun.gender = 'male'
donghun.blood_type = 'RH+ A'

print(f'{donghun.name}의 혈액형은 {donghun.blood_type}입니다.')

donghun.run('Fast')