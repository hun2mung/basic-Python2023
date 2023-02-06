# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)

# 파이썬에서 자주 쓰는 것은 \n 뿐이다.

print('1.Hello.\r\nWorld')
print('2.Hello.\nWorld')    # 이걸 권장

print('3.Hello.\n\tWorld')  # t 탭
print('4.Hello.\n\t\bWorld')  # b 백스페이스

print('5.Hello.\n\'World\'')  # \' 문자열 내 홑따옴표
print('6.Hello."World"')
print('7.Hello.\"World\"')

print('8.Hello. \\ World')  # \를 문자열에 표현
print('9.Hello\0')  # \0 문장의 끝

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작
me = '저'
name = '이동훈'
age = 26
print('%s는 %s입니다. %d입니다.'%(me, name, age))

print(f'{254.112233:.2f}')  #최신식

print('%.4f' %(254.112233)) # 전체자리수.소수점






