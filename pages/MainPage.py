from templates.ui_MainPage import Ui_Form
from PySide6.QtWidgets import QWidget
from viewmodels.userviewmodel import UserViewModel
from mvvmkit.bindableview import BindableView


class MainPage(QWidget, Ui_Form, BindableView):
    def __init__(self, vm: UserViewModel):
        super().__init__()
        self.setupUi(self)
        self.vm = vm
        self.setWindowTitle(self.vm.page_title)
        #
        self.bind(self.vm.username, self.entryUserName)
        self.bind(self.vm.email, self.entryEmail)

        self.bind(self.vm.username, self.labelUserName)
        self.bind(self.vm.email, self.labelEmail)

        self.buttonSend.clicked.connect(self.vm.command_send_info)
        pass
