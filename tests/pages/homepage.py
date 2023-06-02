from os import name
import typing

from PyQt6.QtWidgets import *
from qtmvvmtoolkit.objects.bindable_object import BindableObject
from viewmodels.homevm import HomeViewModel

from qtmvvmtoolkit.commands import RelayCommand


class HomePage(QWidget, BindableObject):
    def __init__(self) -> None:
        super().__init__()
        self.vm = HomeViewModel()

        self.initialize_component()
        self.initialize_binding()
        return

    def initialize_component(self):
        layout = QVBoxLayout(self)

        self.entryName = QLineEdit(self)
        self.labelName = QLabel("--#--", self)
        self.labelVoltage = QLabel("V")

        self.spinCapacity = QDoubleSpinBox()
        self.spinVoltage = QSpinBox()
        self.spinEnergy = QSpinBox()
        self.spinEnergy.setReadOnly(True)
        self.spinEnergy.setMaximum(99990)

        self.cboxNames = QComboBox(self)

        self.buttonCall = QPushButton("Caller")

        layout.addWidget(QLabel("<h2>Observables Str Properties</h2>"))
        layout.addWidget(self.entryName)
        layout.addWidget(self.labelName)
        layout.addSpacing(10)
        layout.addWidget(QLabel("<h2>Computed Properties Sections</h2>"))
        layout.addWidget(self.spinVoltage)
        layout.addWidget(self.labelVoltage)
        layout.addWidget(self.spinCapacity)
        layout.addWidget(self.spinEnergy)

        layout.addWidget(QLabel("<h2>Relayables Properties Sections</h2>"))
        layout.addWidget(self.buttonCall)
        layout.addWidget(QLabel("<h2>Observables Collections</h2>"))
        layout.addWidget(self.cboxNames)

        return None

    def initialize_binding(self) -> None:

        self.vm.username.binding(self.labelName.setText)
        self.vm.username.binding(self.entryName.setText)
        self.binding_widget(self.labelName, self.vm.hide, "visibility")

        self.vm.username.binding_reverse(self.entryName.textChanged)
        self.vm.hide.valueChanged.connect(self.entryName.setReadOnly)

        self.vm.voltage.binding(self.spinVoltage.setValue)
        self.vm.voltage.binding_reverse(self.spinVoltage.valueChanged)
        self.vm.voltage.binding(
            lambda value: self.labelVoltage.setText(f"Voltage={value:02d}V")
        )
        self.binding_widget(self.spinVoltage, self.vm.hide, "visibility")
        self.vm.capacity.binding_percent(self.spinCapacity.setValue)
        self.vm.capacity.binding_reverse_percent(self.spinCapacity.valueChanged)
        self.vm.energy.valueChanged.connect(self.spinEnergy.setValue)

        self.spinEnergy.valueChanged.connect(self.vm.energy.set)

        self.binding_command(
            self.buttonCall,
            RelayCommand(self.display_information, name="viktor"),
        )

        self.vm.infos.binding(self.operation)
        return None

    def operation(self, value: list[str]):
        self.cboxNames.clear()
        self.cboxNames.setDuplicatesEnabled(False)
        self.cboxNames.addItems(value)
        return None

    def display_information(self, name: str):
        self.launch_operation()
        self.vm.infos.append(name)
        self.vm.infos.append("word")
        return None

    def launch_operation(self):
        self.vm.hide.set(not self.vm.hide.get())
        return None
