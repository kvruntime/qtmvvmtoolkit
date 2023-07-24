# coding:utf-8
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from qtmvvmtoolkit.widgets.navbutton import NavButton
from viewmodels.homevm import HomeViewModel

from qtmvvmtoolkit.commands import RelayCommand
from qtmvvmtoolkit.objects.bindable_object import BindableObject


class HomePage(QWidget, BindableObject):
    def __init__(self) -> None:
        super().__init__()
        self.vm = HomeViewModel()

        self.initialize_component()
        self.initialize_binding()
        return

    def initialize_component(self):
        lay = QHBoxLayout()
        btn1 = NavButton("btn-1")
        btn1.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowBack))
        lay.addWidget(btn1)
        lay.addWidget(
            NavButton(
                "btn-1",
                icon=self.style().standardIcon(
                    QStyle.StandardPixmap.SP_DialogHelpButton
                ),
            )
        )
        lay.addWidget(NavButton("btn-3"))
        lay.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(lay)

        self.entryName = QLineEdit(self)
        self.labelName = QLabel("--#--", self)
        self.labelVoltage = QLabel("V")

        self.spinCapacity = QDoubleSpinBox()
        self.spinVoltage = QSpinBox()
        self.spinEnergy = QDoubleSpinBox()
        self.spinEnergy.setReadOnly(True)
        self.spinEnergy.setMaximum(99990)
        self.checkNumbers = QCheckBox(self)

        self.cboxNames = QComboBox(self)

        self.buttonCall = QPushButton("Caller")
        # self.buttonCall.setProperty()

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
        layout.addWidget(self.checkNumbers)
        layout.addStretch()

        return None

    def initialize_binding(self) -> None:
        # self.vm.username.binding(self.labelName.setText)
        self.binding_label_string(self.labelName, self.vm.username)
        # self.vm.username.binding(self.entryName.setText)
        self.binding_textedit_str(self.entryName, self.vm.username)
        self.binding_widget(self.labelName, self.vm.hide, "visibility")

        self.vm.username.binding_reverse(self.entryName.textChanged)
        self.vm.hide.valueChanged.connect(self.entryName.setReadOnly)
        self.binding_checkbox(self.checkNumbers, self.vm.valid_numbers)
        self.binding_spinbox(self.spinVoltage, self.vm.voltage)
        self.binding_label_number(
            self.labelVoltage, self.vm.voltage, lambda value: f"{value:5.2f} v"
        )
        self.binding_widget(self.spinVoltage, self.vm.hide, "visibility")
        self.binding_doublespinbox(self.spinCapacity, self.vm.capacity)
        self.binding_doublespinbox(self.spinEnergy, self.vm.energy)

        self.binding_command(self.buttonCall, RelayCommand(self.display_information))

        self.binding_combobox_items(self.cboxNames, self.vm.infos)
        self.binding_combobox_value(self.cboxNames, self.vm.username)
        return None

    def display_information(self):
        self.launch_operation()
        self.vm.fill_numbers()
        return None

    def launch_operation(self):
        self.vm.hide.set(not self.vm.hide.get())
        return None
