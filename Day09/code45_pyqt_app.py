import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):   # QWidget 상속 받음
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):       # GUI 화면 설정       
        self.setWindowTitle('Simple Window')       # 타이틀 설정
        # self.move(960, 540)       # 위치 잡기
        self.resize(400, 200)       # 사이즈 설정
        self.show()     # 출력 핵심!



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())