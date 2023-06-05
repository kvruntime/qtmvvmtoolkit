# -*- coding:utf-8 -*-
import typing
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QToolButton,
    QLineEdit,
    QTextEdit,
    QLabel,
)

# from qtpy.QtWidgets import *
from qtmvvmtoolkit.commands import RelayCommand
from qtmvvmtoolkit.inputs.computedproperty import (
    ComputedObservableBoolProperty,
    ComputedObservableFloatProperty,
    ComputedObservableIntProperty,
    ComputedObservableStrProperty,
)

from qtmvvmtoolkit.inputs.observableproperty import (
    ObservableBoolProperty,
    ObservableFloatProperty,
    ObservableIntProperty,
    ObservableStrProperty,
)


class BindableObject(QObject):
    def __init__(self) -> None:
        super().__init__()
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
            observable.valueChanged.connect(widget.setHidden)
        if prop == "state":
            observable.valueChanged.connect(widget.setDisabled)
        observable.valueChanged.emit(observable.get())
        return None

    # Input widgets
    # def binding_inputs_str(
    #     self,
    #     widget: typing.Union[QLineEdit, QTextEdit],
    #     observable: typing.Union[
    #         ObservableIntProperty,
    #         ObservableFloatProperty,
    #         ComputedObservableIntProperty,
    #         ComputedObservableFloatProperty,
    #     ],
    # ) -> None:
    #     observable.valueChanged.connect(lambda value:widget.setText(str(value)))
    #     observable.valueChanged.emit(observable.get())
    #     return None

    def binding_label_number(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableIntProperty,
            ObservableFloatProperty,
            ComputedObservableIntProperty,
            ComputedObservableFloatProperty,
        ],
        transformer: typing.Optional[typing.Callable[[typing.Union[int, float]], str]] = None,
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
        raise NotImplementedError("Unavalaible for now")
        # return

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
