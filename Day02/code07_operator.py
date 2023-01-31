# 연산자
# 할당연산 assignment
# 2 = 1 (x)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2)         #소수 나누기
print(1024 // 2)        #정수 나누기
print(1024 % 2)         #나머지
print(6 // 3)
print(6 % 3)            #

print(2 ** 10)          #2의 10제곱

# print(6 / 0)          # error
# print(6 // 0)

# 문자열 연산(+, * 만 가능)
first = 'Hello'
second = 'World'
print(first + second)
print(first + ' ' + second)
print(first, second)

print(first * 4)

#문자열 길이
print(len(first))
#문자열에서 각 인덱스의 문자
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
#print(first[5])    # error
#문자열의 뒤에서 부터 해당 인덱스 문자
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기
current = '2023-01-31 15:14:02' #현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일' + current[11:13] + '시' + current[14:16] + '분' +current[17:] + '초')

print(current[-19:-15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7
print(que)          # 변경됨

# que[5] = 10         # que의 길이가 5이다. 4번 인덱스가 마지막이라 error 발생.
# print(que)

que.append(10)          # append로 리스트 마지막에 원하는 숫자 추가
print(que)          

que.insert(3, 99)       # 특정 인덱스에 추가
print(que)

que.remove(99)          # 해당 값 삭제
print(que)

# tup = (1, 2, 3, 4, 5)
# tup[1] = 9          # 튜플은 변경이 불가하여 error 발생
# print(tup)

# 문자열 == 문자 리스트
title = 'python'
print(title)

# title[0] = 'P' # 문자열에서는 변경불가 
print('P' + title[1:])

# 일반적인 문자형 리스트 
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)

text[0] = 'P'   # 문자형에서는 가능
print(text[0])

# 문자열 포맷팅 => 바꾸고 싶은 부분 변강 가능
print ("I'm so happy {0} you, {1}!!".format(2, 'Hey'))  # 구식
# 최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print (f"I'm so happy {preword} you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')

# split => 문자열을 특정문자로 자르기
full_name = 'Dong Hun. Lee'
vals = full_name.split()    # 스페이스
print(type(vals))
print(vals)

vals = full_name.split('.') # .으로 지정
print(vals)

print(full_name.replace('Dong Hun.', 'Ashely'))

# 문자열 공백 없애기
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|')
print(hi.rstrip() + '|')
print(hi.strip() + '|')

# 문자열에서 값을 찾기
print(full_name.index('H'))
# print(full_name.index('z'))   # 존재하지 않아 error

print(full_name.find('Z'))      # 찾는 게 없으면 -1 
print(full_name.find('H'))

# 찾는 단어의 개수
print(full_name.count('e'))

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)
