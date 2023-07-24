# -*- coding:utf-8 -*-
from pathlib import Path
import typing

from PyQt6.QtGui import QAction
from qtpy.QtCore import QObject, QVariant
from qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QToolButton,
    QWidget,
)

from qtmvvmtoolkit.commands import RelayCommand
from qtmvvmtoolkit.inputs import (
    ComputedObservableBoolProperty,
    ComputedObservableFloatProperty,
    ComputedObservableIntProperty,
    ComputedObservableStrProperty,
    ObservableBoolProperty,
    ObservableCollection,
    ObservableFloatProperty,
    ObservableIntProperty,
    ObservableStrProperty,
    RelayableProperty,
)


class BindableObject(QObject):
    def __init__(
        self,
        parent: typing.Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        return

    def initialize_component(self) -> None:
        raise NotImplementedError()

    def initialize_binding(self) -> None:
        raise NotImplementedError()

    # Widgets
    def binding_widget(
        self,
        widget: QWidget,
        observable: typing.Union[
            ObservableBoolProperty, ComputedObservableBoolProperty
        ],
        prop: typing.Literal["visibility", "state"],
    ):
        if prop == "visibility":
            observable.valueChanged.connect(widget.setVisible)
        if prop == "state":
            observable.valueChanged.connect(widget.setEnabled)
        observable.valueChanged.emit(observable.get())
        return None

    # Input widgets
    def binding_textedit_number(
        self,
        widget: QLineEdit,
        observable: typing.Union[
            ObservableIntProperty,
            ObservableFloatProperty,
            ComputedObservableIntProperty,
            ComputedObservableFloatProperty,
        ],
    ) -> None:
        widget.setReadOnly(True)
        observable.valueChanged.connect(lambda value: widget.setText(str(value)))
        observable.valueChanged.emit(observable.get())
        return None

    def binding_textedit_str(
        self,
        widget: QLineEdit,
        observable: typing.Union[ObservableStrProperty, ComputedObservableStrProperty],
    ) -> None:
        observable.valueChanged.connect(widget.setText)
        widget.textChanged.connect(observable.set)
        observable.valueChanged.emit(observable.get())
        return None

    def binding_label_number(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableIntProperty,
            ObservableFloatProperty,
            ComputedObservableIntProperty,
            ComputedObservableFloatProperty,
        ],
        transformer: typing.Optional[
            typing.Callable[[typing.Union[int, float]], str]
        ] = None,
    ) -> None:
        if not transformer:
            observable.valueChanged.connect(
                lambda value: widget.setText(str(value)),
            )
        if transformer:
            observable.valueChanged.connect(
                lambda value: widget.setText(transformer((value))),
            )

            pass
        observable.valueChanged.emit(observable.get())
        return

    def binding_label_string(
        self,
        widget: QLabel,
        observable: typing.Union[ObservableStrProperty, ComputedObservableStrProperty],
    ) -> None:
        observable.valueChanged.connect(widget.setText)
        observable.valueChanged.emit(observable.get())
        return None

    # Commands
    def binding_command(
        self,
        widget: typing.Union[QPushButton, QToolButton, QAction],
        command: RelayCommand,
    ) -> None:
        if isinstance(widget, (QAction, QToolButton)):
            widget.triggered.connect(command)
        if isinstance(widget, QPushButton):
            widget.clicked.connect(command)
        return None

    # SpinBox
    def binding_spinbox(
        self,
        widget: QSpinBox,
        observable: typing.Union[ObservableIntProperty, ComputedObservableIntProperty],
        transformer: typing.Optional[typing.Literal["percent"]] = None,
    ) -> None:
        if transformer == "percent":
            observable.valueChanged.connect(
                lambda value: widget.setValue(int(value * 100))
            )
            widget.valueChanged.connect(lambda value: observable.set(int(value / 100)))
            observable.valueChanged.emit(observable.get())
            return None

        observable.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(observable.set)
        observable.valueChanged.emit(observable.get())
        return None

    def binding_doublespinbox(
        self,
        widget: QDoubleSpinBox,
        observable: typing.Union[
            ObservableFloatProperty,
            ComputedObservableFloatProperty,
        ],
        transformer: typing.Optional[typing.Literal["percent"]] = None,
    ) -> None:
        if transformer == "percent":
            observable.valueChanged.connect(lambda value: widget.setValue(value * 100))
            widget.valueChanged.connect(lambda value: observable.set(value / 100))
            observable.valueChanged.emit(observable.get())
            return None

        observable.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(observable.set)
        observable.valueChanged.emit(observable.get())
        return None

    # Comboxbox
    def binding_combobox_items(
        self, widget: QComboBox, observable: ObservableCollection[typing.Any]
    ) -> None:
        # TODO: assume all value are converted into str before call addItems
        widget.setDuplicatesEnabled(False)
        observable.valueChanged.connect(widget.clear)
        # observable.valueChanged.connect(widget.addItems) Old
        # observable.valueChanged.connect(
        #     lambda values: (
        #         [
        #             widget.addItem(str(value), userData=QVariant(value))
        #             for value in values
        #         ]
        #     )
        # )
        observable.valueChanged.connect(
            lambda values: self._fill_combobox_items(widget, values)
        )
        observable.valueChanged.emit(observable.value)
        # widget.setCurrentIndex(-1)
        return None

    def _fill_combobox_items(
        self, widget: QComboBox, values: typing.List[typing.Any]
    ) -> None:
        for value in values:
            if isinstance(value, Path):
                widget.addItem(value.name, userData=QVariant(value))
            else:
                widget.addItem(str(value), userData=QVariant(value))
        widget.setCurrentIndex(-1)
        return

    def binding_combobox_value(
        self,
        widget: QComboBox,
        observable: typing.Union[ObservableStrProperty, ComputedObservableStrProperty],
    ) -> None:
        # TODO: assume all value are converted into str before call addItems
        # widget.currentTextChanged.connect(observable.set) Old
        # widget.currentTextChanged.emit(widget.currentText)
        widget.currentTextChanged.connect(lambda: observable.set(widget.currentData()))
        widget.currentTextChanged.emit(widget.currentText())
        return None

    # QCheckBox
    def binding_checkbox(
        self,
        widget: QCheckBox,
        observable: typing.Union[
            ObservableBoolProperty, ComputedObservableBoolProperty
        ],
    ) -> None:
        observable.valueChanged.connect(widget.setChecked)
        widget.stateChanged.connect(observable.set)
        observable.valueChanged.emit(observable.get())
        return None

    # Relayable

    def binding_relayable(
        self,
        func: typing.Callable[[], None],
        relayable: RelayableProperty,
    ) -> None:
        relayable.relayed.connect(func)
        return None
