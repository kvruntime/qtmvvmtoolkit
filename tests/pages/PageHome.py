from qtmvvmkit.widgets.tabbedpage import TabbedPage
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QPushButton


class PageHome(TabbedPage):
    def __init__(self, parent: typing.Optional[QWidget] = None ) -> None:
        super().__init__(parent)
        
        self.navigationBar.addWidget(QPushButton("PageOne"))
        self.navigationBar.addWidget(QPushButton("PageTwo"))
        pass