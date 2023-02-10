# studyPython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력
    - 주석

```python
# desc : 콘솔출력           # 주석
print('Hello, Python!!')    # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
    - 흐름제어

```python
# 변수
val = 1

# 자료형
print(type(val))        # <class 'int'>

# 문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.')        # 파이는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.')   # 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')  # 파이는      3.142입니다.
```
## 3일차
1. 파이썬 기본
    - 흐름제어
        - 디버깅 시 F10 : 상세내용 넘어가기 / F11 : 상세내용까지 확인
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수

## 4일차
1. 파이썬 기본
    - 가상환경
        - global환경과 다른 환경을 만드는 것
    - 객체지향 OOP
        - 객체는 변수(명사)랑 함수(동사)의 집합.
        - 클래스 안 변수는 클래스 속성을 띄어 속성변수라 한다.
        - 클래스 안 함수는 파라미터로 self 필수.
        - 매직 메서드 : __init__(생성자) 등등
    - 패키지, 모듈
    
## 5일차
1. 파이썬 기본
    - 패키지 계속
        - 인터넷 : 네트워크를 통한 request 와 response
    - 입출력 다시
        - file = open('smaple.txt', 'w')  # 파일 쓰기로 만듦
        - r : 읽기, w : 쓰기, a : 추가쓰기
        - 절대 경로 : root부터 모든 경로 적는 것
        - 상대 경로 : 현재위치 기준으로 적는 것
        - open() 과 close()는 항상 함께
    - 예외처리
        - 오류 : 코딩 중 문법적 문제
        - 예외 : 실행되고 나서 생기는 문제
```python
#매직코드
# C int main(void){} 동일
if __name__ == '__main__':
    print('main을 실행합니다!')
```
```python
# 완전 다중입력(개수가 몇개든지 상관없음)
inputs = list(map(str, input('단어를 입력하세요 > ').split()))
```
```python
#utf-8
file = open('smaple.txt', 'a', encoding='utf-8')
```
```python
# 예외 발생 시 예외처리 필수.
try:    
    pass
except Exception as e:
    print(e)
```

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/hun2mung/studyPython2023/blob/main/Project/address_app.py)

![실행화면](https://raw.githubusercontent.com/hun2mung/studyPython2023/main/Images/my_address_app.png)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법(MD와 파이썬 함께 사용 가능하다는 것이 큰 장점.)
        - 노트북 생성 : 파일메뉴 > 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        -folium (지도 라이브러리)
 ## 8일차
 1. 파이썬 응용
    - 라이브러리 사용법
        - 웹크롤링용 라이브러리
    - 웹 크롤링 [소스](https://github.com/hun2mung/studyPython2023/blob/main/Day08/code44_web_crawling_tutorial.ipynb)
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링(버스 정류장 찾기)
        - BeautifulSoup 크롤링
![실행화면](https://raw.githubusercontent.com/hun2mung/studyPython2023/main/Images/jupyter_folium.png)

            Folium OpenAPI 연동화면

## 9일차
1. 파이썬 응용
    - GUI 개발
        - Tkinter 소개
        - PyQt 소개, 설치
        - 위젯
```
wikidocs : https://wikidocs.net/
wikibooks : https://wikibook.co.kr/
```
        
## 10일차
1. 파이썬 응용
- GUI 개발
    - PyQt 위젯 계속
    - PyQt 다이얼로그

![실행화면](https://raw.githubusercontent.com/hun2mung/studyPython2023/main/Images/dialog.png)
실행화면

 ```
클래스 함수 내 self 역할 : cbOption과 self.cbOption 과의 차이 -> self.가 빠지면 지역변수로 선언되어 글로벌 변수가 아니므로 다른 함수 내에서 활용 불가.
```
