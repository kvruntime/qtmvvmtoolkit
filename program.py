from PySide6.QtWidgets import *
from pages.MainPage import MainPage
from viewmodels.userviewmodel import UserViewModel
import qdarktheme

app = QApplication([])
app.setStyleSheet(qdarktheme.load_stylesheet(theme="light"))
win = MainPage(UserViewModel())
win.show()
app.exec()
