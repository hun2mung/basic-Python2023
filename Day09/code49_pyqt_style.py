# 스타일
import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet('color : red;'
                              'border-style : solid;'
                              'border-width : 5px;'
                              'border-color : #FA8072;'
                              'border-radius : 10px;'
                              )   
        
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet('color : green;'
                              'border-style : dashed;'
                              'border-width : 5px;'
                              'border-color : #7FFFD4;'
                              'border-radius : 1px;'
                              )   

        # 레이아웃 : QVBoxLayout -> 세로로 위치 / QBoxLayout -> 가로로 위치

        vbox = QVBoxLayout()        # 세로 구분짓는 레이아웃
        vbox.addWidget(lbl_red)     # 위젯 추가
        vbox.addWidget(lbl_green)   # 위젯 추가


        self.setLayout(vbox)        # 전체 레이아웃에 vbox 추가

        # 기본설정 - 사이즈, show() 필수!!!
        self.setWindowTitle('스타일 지정')
        self.setGeometry(300, 300, 500, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
