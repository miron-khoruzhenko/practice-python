# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # self.ui.pushButton.actionEvent()
        self.ui.pushButton.released.connect(self.onPush)

    
    def onPush(self):
        print(self.ui.lineEdit.text())  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    # widget.onPush()
    widget.show()
    sys.exit(app.exec())




# # This Python file uses the following encoding: utf-8
# from pathlib import Path
# import sys

# from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QSystemTrayIcon, QMenu, QPushButton
# from PySide6.QtCore import QFile, Slot, Signal, QObject, QThreadPool
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtGui import QAction, QIcon, QTextCursor
# from PySide6.QtDesigner import QDesignerFormWindowCursorInterface


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

# #load ui#
#         loader = QUiLoader()
#         path = os.fspath(Path(__file__).resolve().parent / "form.ui")
#         ui_file = QFile(path)
#         ui_file.open(QFile.ReadOnly)
#         self.ui = loader.load(ui_file)
#         ui_file.close()
#         self.setCentralWidget(self.ui)
# #_load ui_#

# #Bindings#
#         self.ui.pushButton.released.connect(self.pushButtonReleased)
# #_Bindings_#

#     def changeToMainScreen(self):
#         print('2')
#         loader = QUiLoader()
#         path = os.fspath(Path(__file__).resolve().parent / "mainScreen.ui")
#         ui_file = QFile(path)
#         ui_file.open(QFile.ReadOnly)
#         self.ui = loader.load(ui_file)
#         ui_file.close()
#         self.setCentralWidget(self.ui)
# import os

#     def pushButtonReleased(self):
#         print('1')
#         self.changeToMainScreen()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = MainWindow()
#     widget.show()
#     sys.exit(app.exec())
