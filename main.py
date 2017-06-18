import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyMainWindow(QMainWindow):
    m_C = 0

    def __init__(self):
        super(MyMainWindow, self).__init__()
        loadUi('tempconverter.ui', self)

    def update(self, C, F):
        C, F = int(C), int(F)
        if self.m_C == C:
            return
        self.m_C = C

        self.lcdC.display(C)
        self.lcdF.display(F)
        self.dialC.setValue(C)
        self.dialF.setValue(F)

    def on_dialC_valueChanged(self, C):
        F = C * 9 / 5 + 32
        self.update(C, F)

    def on_dialF_valueChanged(self, F):
        C = 5 / 9 * (F - 32)
        self.update(C, F)


def main():
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
