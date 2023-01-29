from PyQt6.QtWidgets import QWidget, QFrame
from PyQt6 import QtCore
import typing

from qtmvvmkit.navigations.router import Router
from qtmvvmkit.templates.pages.ui_NavigationPage import Ui_PageNavifation


class NavigationPage(QWidget, Ui_PageNavifation):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.navigationBar:typing.Optional[QFrame]
        self.navigationContent:typing.Optional[QWidget]
        self.router:typing.Optional[Router]
        
        
        self.intializeComponent()
        pass
    
    def intializeComponent(self):
        self.navigationBar = QFrame(self)
        self.navigationContent = QWidget(self)
        # FIXME: implement router for this kind of router outlet
        # self.router = Router(self.navigationContent)
        
        return None
    pass