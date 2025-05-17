import datetime
import shutil
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class Main_Wind(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/untitled.ui', self)
        self.pushButton.clicked.connect(self.buttons)

    def buttons(self):
        self.make_reserve_arc(self.source.text(), self.dest.text())

    def make_reserve_arc(self, source, dest):
        try:
            shutil.make_archive(source.strip().split('/')[-1] + str(datetime.datetime.now()).replace(' ', '')[:-7],
                                'zip', root_dir=source)
            shutil.move(source + str(datetime.datetime.now()).replace(' ', '')[:-7] + '.zip', dest)
        except Exception:
            print('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Wind()
    ex.show()
    sys.exit(app.exec())
