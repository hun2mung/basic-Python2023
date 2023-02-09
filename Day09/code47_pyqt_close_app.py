# 윈도우 창닫기 앱
# 2023.02.09
# LDH

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ininUI()

    def ininUI(self):
        btn = QPushButton('Quit', self)
        btn.move(320, 170)
        btn.resize(btn.sizeHint())
        btn.setToolTip('이거 누르면 그냥 꺼져요. <b>조심</b>하세요!!!')     # 버튼 툴팁
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Qut Button')
        self.setGeometry(1000, 200, 400, 200)    # x, y, width, height
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
