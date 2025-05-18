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
        print(self.source.text(), self.dest.text())
        make_reserve_arc(self.source.text(), self.dest.text())


def make_reserve_arc(source, dest):
    time = (str(datetime.datetime.now()).replace(' ', '_'))
    time = time.replace('.', ':')
    shutil.make_archive(base_name=time.strip(), format='7Z', root_dir=source.strip())
    shutil.move(time.strip() + '.7Z', dest.strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Wind()
    ex.show()
    sys.exit(app.exec())
