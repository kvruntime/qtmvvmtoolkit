# coding:utf-8
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from viewmodels.homevm import HomeViewModel

from qtmvvmtoolkit.commands import RelayCommand
from qtmvvmtoolkit.converters import ToStrConverter
from qtmvvmtoolkit.objects import BindableObject


class PageHome(QWidget, BindableObject):
    def __init__(self) -> None:
        super().__init__()
        self.vm = HomeViewModel()

        self.initialize_component()
        self.initialize_binding()

        print("<===>")
        print(6 in self.vm.numbers)
        print(self.vm.numbers.pop(3))
        for number in self.vm.numbers:
            print(number)
        return

    def initialize_component(self):
        lay = QHBoxLayout()
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
        self.entry_cbox_value = QLineEdit()
        self.entry_for_number = QLineEdit()

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
        layout.addWidget(self.entry_cbox_value)
        layout.addWidget(self.entry_for_number)
        layout.addWidget(self.checkNumbers)
        layout.addStretch()

        return None

    def initialize_binding(self) -> None:
        self.binding_label_string(self.labelName, self.vm.username)
        converter = ToStrConverter(str, str)
        converter.convert(8)
        self.binding_textedit(
            self.entryName,
            self.vm.username,
        )
        self.binding_checkbox(self.checkNumbers, self.vm.state)
        self.binding_spinbox(self.spinVoltage, self.vm.voltage)
        self.binding_label_number(
            self.labelVoltage, self.vm.voltage, lambda value: f"{value:5.2f} v"
        )
        self.binding_widget(self.spinVoltage, self.vm.hide, "visibility")
        self.binding_doublespinbox(self.spinCapacity, self.vm.capacity)
        self.binding_doublespinbox(self.spinEnergy, self.vm.energy)

        self.binding_command(self.buttonCall, RelayCommand(self.display_information))

        self.binding_combobox(
            self.cboxNames, self.vm.user_infos, False, display_name="infos"
        )
        self.binding_combobox_selection(self.cboxNames, self.vm.user)
        # self.vm.user.binding(lambda u: print(f"user=>{u}"))
        # self.vm.user.binding(lambda u: self.entry_cbox_value.setText(u.name))
        self.binding_textedit(self.entry_for_number, self.vm.counter)
        # self.binding_combobox_realvalue(self.cboxNames, self.vm.username)
        return None

    def display_information(self):
        self.launch_operation()
        self.vm.fill_numbers()
        return None

    def launch_operation(self):
        self.vm.hide.set(not self.vm.hide.get())
        return None
