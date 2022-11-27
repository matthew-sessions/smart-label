from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget, QFileDialog
from video_manager import VideoManager
import sys

from py_ui.ui_core_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listWidget = QListWidget()
        self.video_manager = VideoManager(self)
        self.ui.scrollArea.setWidget(self.listWidget)

    def keyPressEvent(self, event):
        self.video_manager.pass_keypress(event)


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    sys.exit(app.exec())