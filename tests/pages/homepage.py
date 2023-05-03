import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *

from qtmvvmtoolkit.observables import BindableObject
from viewmodels.homevm import HomeViewModel


class HomePage(QWidget, BindableObject):
    def __init__(self, parent: typing.Optional[QWidget] = None ) -> None:
        super().__init__(parent)

        self.vm = HomeViewModel()

        self.initialize_components()
        self.initialize_bindings()

    def initialize_components(self):

        layout = QVBoxLayout(self)

        self.labelName = QLabel("--#--", self)
        self.entryName = QLineEdit(self)

        self.spinCapacity = QSpinBox()
        self.spinVoltage = QSpinBox()
        self.spinEnergy = QSpinBox()
        self.spinEnergy.setReadOnly(True)
        self.spinEnergy.setMaximum(99990)

        self.buttonCall = QPushButton("Caller")

        layout.addWidget(QLabel("<h2>Observables Str Properties</h2>"))
        layout.addWidget(self.entryName)
        layout.addWidget(self.labelName)
        layout.addSpacing(10)
        layout.addWidget(QLabel("<h2>Computed Properties Sections</h2>"))
        layout.addWidget(self.spinCapacity)
        layout.addWidget(self.spinVoltage)
        layout.addWidget(self.spinEnergy)

        layout.addWidget(QLabel("<h2>Relayables Properties Sections</h2>"))
        layout.addWidget(self.buttonCall)

        return None

    def initialize_bindings(self) -> None:
        self.bind_label(self.vm.username, self.labelName)
        self.bind_lineedit(self.vm.username, self.entryName)
        self.bind_spinbox(self.vm.voltage, self.spinVoltage)
        self.bind_spinbox(self.vm.capacity, self.spinCapacity)
        self.bind_spinbox(self.vm.energy, self.spinEnergy)

        self.bind_button_command(self.buttonCall, self.vm.command_call_relay)
        self.relaying(self.vm.changed, self.display_information)
        return None

    def display_information(self):
        res = QMessageBox.information(QWidget(), "Informations", "Calling...", QMessageBox.StandardButton.Close|QMessageBox.StandardButton.Yes)
        print(res)
        if res.Close:
            self.launch_operation()

        return None
    def launch_operation(self):
        for index in range(100_000):
            print("operating...")
        return None