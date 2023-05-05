import typing

from PyQt6.QtWidgets import *
from viewmodels.homevm import HomeViewModel

from qtmvvmtoolkit.inputs import RelayCommand


class HomePage(QWidget):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.vm = HomeViewModel()

        self.initialize_components()
        self.initialize_bindings()

    def initialize_components(self):
        layout = QVBoxLayout(self)

        self.entryName = QLineEdit(self)
        self.labelName = QLabel("--#--", self)
        self.labelVoltage = QLabel("V")

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
        layout.addWidget(self.spinVoltage)
        layout.addWidget(self.labelVoltage)
        layout.addWidget(self.spinCapacity)
        layout.addWidget(self.spinEnergy)

        layout.addWidget(QLabel("<h2>Relayables Properties Sections</h2>"))
        layout.addWidget(self.buttonCall)

        return None

    def initialize_bindings(self) -> None:
        self.vm.username.binding(self.labelName.setText)
        self.vm.username.binding(self.entryName.setText)
        self.vm.hide.valueChanged.connect(self.labelName.setHidden)

        self.vm.username.binding_reverse(self.entryName.textChanged)
        self.vm.hide.valueChanged.connect(self.entryName.setReadOnly)

        self.vm.voltage.binding(self.spinVoltage.setValue)
        self.vm.voltage.binding_reverse(self.spinVoltage.valueChanged)
        self.vm.voltage.binding(
            lambda value: self.labelVoltage.setText(f"Voltage={value:02d}V")
        )
        self.vm.hide.binding(lambda value: self.spinVoltage.setVisible(not value))
        self.vm.capacity.binding(self.spinCapacity.setValue)
        self.vm.capacity.binding_reverse(self.spinCapacity.valueChanged)
        self.vm.energy.valueChanged.connect(self.spinEnergy.setValue)
        self.spinEnergy.valueChanged.connect(self.vm.energy.set)

        # self.vm.changed.binding(self.display_information)
        self.buttonCall.clicked.connect(
            RelayCommand(self.display_information, name="viktor")
        )
        return None

    def display_information(self, name: str):
        self.launch_operation()
        print(name)
        return None

    def launch_operation(self):
        self.vm.hide.set(not self.vm.hide.get())
        return None
