from tkinter import ON
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from qtmvvmtoolkit.observables.objects import BindableObject
from viewmodels.homevm import HomeViewModel


class HomePage(QWidget, BindableObject):
    def __init__(self, parent: typing.Optional[QWidget] = None ) -> None:
        super().__init__(parent)
        self.vm = HomeViewModel()

        self.initialize_components()
        self.intialize_bindings()
        pass

    def initialize_components(self):
        layout = QVBoxLayout(self)

        self.labelName = QLabel("---username---", self)
        self.entryName = QLineEdit(self)

        layout.addWidget(self.entryName)
        return None

    def intialize_bindings(self) -> None:
        self.bind_label(self.vm.username, self.labelName)
        self.bind_lineedit(self.vm.username, self.entryName)
        return None