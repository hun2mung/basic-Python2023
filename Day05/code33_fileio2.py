# 파일 읽어오기
file = open('./Day05/sample10.txt', 'r', encoding='UTF-8')

while True:
    text = file.read()
    if not text: break
    print(text)

file.close()