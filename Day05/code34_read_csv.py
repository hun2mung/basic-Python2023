# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황

import csv

fileName = 'busanbus.csv'
dirName = 'C:/Source/studyPython2023/'
fullPath = dirName + fileName

file = open(fullPath, 'r', encoding='UTF-8')    # 오픈하면
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)     # list 자료구조로 가져옴

file.close()        # 반드시 닫아주세요!
