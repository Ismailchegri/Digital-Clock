import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 100)
        self.setWindowTitle('Digital Clock')
        self.time_label = QLabel(self)
        self.time = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet('font-size: 100px;' 'color: hsl(63, 33%, 86%)')
        self.setStyleSheet('background-color: hsl(7, 47%, 49%);')

        self.time_update()
        self.time.timeout.connect(self.time_update)
        self.time.start(1000)

        fontid = QFontDatabase.addApplicationFont('Bruce Forever.ttf') 
        font_family = QFontDatabase.applicationFontFamilies(fontid)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
    
    def time_update(self):
        current_time = QTime().currentTime().toString('HH:mm:ss')
        self.time_label.setText(current_time)
        
def main():
    app = QApplication(sys.argv)
    Clock = DigitalClock()
    Clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 