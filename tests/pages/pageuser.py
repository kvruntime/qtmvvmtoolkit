# coding:utf-8
from qtpy.QtWidgets import QWidget, QLineEdit, QSpinBox
from qtmvvmtoolkit.inputs import ObservableObject
from qtmvvmtoolkit.objects import BindableObject

from viewmodels.uservm import UserViewModel
from pages.templates.PageUser_ui import Ui_PageUser


class PageUser(QWidget, Ui_PageUser, BindableObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.setupUi(self)
        self.vm = UserViewModel()

        self.buttonDisplay.clicked.connect(self.vm.command_display_user)
        self.binding_spin(self.vm.ou, "age", self.spinAge)
        self.binding_entry(self.vm.ou, "name", self.entryName)
        return

    def binding_entry(
        self, observable: ObservableObject, attr: str, widget: QLineEdit
    ) -> None:
        def _handle_change(attr, value):
            if attr == widget.objectName():
                widget.setText(str(value))

        if observable.has_attr(attr):
            widget.setObjectName(attr)

            observable.valueChanged.connect(_handle_change)
            widget.textChanged.connect(lambda value: observable.rbinding(attr, value))
        observable.valueChanged.emit(attr, observable.get(attr))

        return None

    def binding_spin(
        self, observable: ObservableObject, attr: str, widget: QSpinBox
    ) -> None:
        def _handle_change(attr, value):
            if attr == widget.objectName():
                widget.setValue(int(value))

            return None

        if observable.has_attr(attr):
            widget.setObjectName(attr)

            observable.valueChanged.connect(_handle_change)
            widget.valueChanged.connect(lambda value: observable.rbinding(attr, value))
        observable.valueChanged.emit(attr, observable.get(attr))

        return None
