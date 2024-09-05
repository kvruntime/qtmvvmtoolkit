# coding:utf-8
from pages.templates.PageUser_ui import Ui_PageUser
from qtmvvmtoolkit.objects import BindableObject
from qtpy.QtWidgets import QWidget
from viewmodels.uservm import UserViewModel


class PageUser(QWidget, Ui_PageUser, BindableObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.setupUi(self)  # type:ignore
        self.vm = UserViewModel()

        self.binding_value(self.entryName, self.vm.user.name)
        self.binding_value(self.spinAge, self.vm.user.age)
        self.buttonDisplay.clicked.connect(self.vm.command_display_user)
        return
