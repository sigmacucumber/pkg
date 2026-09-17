import sys
from PyQt5 import QtWidgets
from main import Ui_MainWindow
from controller import ColorController

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = ColorController(self)
        self.controller.setup_connections()
        self.controller.on_rgb_changed()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())