# -*- coding:utf-8 -*-
from logging import warning
import typing
import warnings

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QWidget,
)

from .boolproperty import (
    ComputedObservableBoolProperty,
    ObservableBoolProperty,
)
from .floatproperty import (
    ComputedObservableFloatProperty,
    ObservableFloatProperty,
)
from .intproperty import ComputedObservableIntProperty, ObservableIntProperty
from .observableproperty import ComputedObservableProperty, ObservableProperty
from .relayableproperty import RelayableProperty
from .strproperty import ComputedObservableStrProperty, ObservableStrProperty

Observables = [
    ObservableProperty,
    ComputedObservableProperty,
    ObservableBoolProperty,
    ComputedObservableBoolProperty,
    ObservableFloatProperty,
    ComputedObservableFloatProperty,
    ObservableIntProperty,
    ComputedObservableIntProperty,
    ObservableStrProperty,
    ComputedObservableStrProperty,
]

display_properties = typing.Literal["hidden", "disabled"]


class BindableObject(QObject):
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        warnings.warn("deprecated: this will be removed in future")
        pass

    # @typing.overload
    # def binding_label(
    #     self,
    #     widget: QLabel,
    #     prop: typing.Literal,
    #     observable: ObservableBoolProperty | ComputedObservableBoolProperty,
    # ) -> None:
    #     ...

    # @typing.overload
    # def binding_label(
    #     self,
    #     widget: QLabel,
    #     prop: display_properties,
    #     observable: ObservableBoolProperty | ComputedObservableBoolProperty,
    # ) -> None:
    #     ...

    # def binding_label(
    #     self,
    #     widget: QLabel,
    #     prop: typing.Literal | display_properties,
    #     observable: ObservableProperty | ComputedObservableProperty,
    # ) -> None:
    #     return

    # Relayable Property
    def bind_relayable_property(
        self, value: RelayableProperty, function: typing.Callable[..., None]
    ) -> None:
        value.relayed.connect(lambda: function())
        return None

    def relaying(
        self, value: RelayableProperty, function: typing.Callable[..., None]
    ) -> None:
        value.relayed.connect(lambda: function())
        return None

    def bind_lineedit(self, prop: ObservableStrProperty, widget: QLineEdit) -> None:
        prop.valueChanged.connect(widget.setText)
        widget.textChanged.connect(prop.set)
        prop.valueChanged.emit(prop.get())
        return None

    def bind_lineedit_to_int(self, prop: ObservableIntProperty, widget: QLineEdit):
        prop.valueChanged.connect(lambda value: widget.setText(str(value)))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_lineedit_to_float(self, prop: ObservableFloatProperty, widget: QLineEdit):
        prop.valueChanged.connect(lambda value: widget.setText(str(round(value, 3))))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_label(self, prop: ObservableStrProperty, widget: QLabel) -> None:
        prop.valueChanged.connect(widget.setText)
        prop.valueChanged.emit(prop.get())
        return None

    def bind_label_to_int(self, prop: ObservableIntProperty, widget: QLabel) -> None:
        prop.valueChanged.connect(lambda value: widget.setText(str(value)))
        prop.valueChanged.emit(prop.get())
        return None

    def bind_combobox_items(self, prop: ObservableProperty, widget: QComboBox) -> None:
        prop.valueChanged.connect(widget.addItems)
        return None

    # QSPINBOX
    def bind_spinbox(
        self,
        prop: typing.Union[ObservableIntProperty, ComputedObservableIntProperty],
        widget: QSpinBox,
    ):
        prop.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(prop.set)
        prop.valueChanged.emit(prop.get())
        return None

    # QDoubleSpinBox
    def bind_dspin(self, value: ObservableFloatProperty, widget: QDoubleSpinBox):
        value.valueChanged.connect(widget.setValue)
        widget.valueChanged.connect(value.set)
        value.valueChanged.emit(value.get())
        return None

    def bind_dspin_percent(self, prop: ObservableFloatProperty, widget: QDoubleSpinBox):
        prop.valueChanged.connect(lambda value: widget.setValue(value * 100))
        widget.valueChanged.connect(lambda value: prop.set(value / 100))
        prop.valueChanged.emit(prop.get())
        return None

    # QPushButton
    def bind_button_command(
        self, button: QPushButton, command: typing.Callable[[], None]
    ):
        button.clicked.connect(lambda: command())
        return None

    def bind_button_state(self, prop: ObservableBoolProperty, widget: QPushButton):
        prop.valueChanged.connect(lambda value: widget.setEnabled(value))
        prop.valueChanged.emit(prop.get())
        return None
