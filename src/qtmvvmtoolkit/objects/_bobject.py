# coding:utf-8
import typing
import warnings
from pathlib import Path

from PyQt6.QtGui import QAction
from qtpy.QtCore import QObject, QVariant
from qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QTextEdit,
    QToolButton,
    QWidget,
)

from qtmvvmtoolkit.commands import RelayCommand
from qtmvvmtoolkit.inputs import (
    ComputedObservableProperty,
    ObservableCollection,
    ObservableProperty,
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
        return None

    def initialize_binding(self) -> None:
        return None

    # Widgets
    def binding_widget(
        self,
        widget: QWidget,
        observable: typing.Union[
            ObservableProperty[float], ComputedObservableProperty[float]
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
            ObservableProperty[int],
            ObservableProperty[float],
            ComputedObservableProperty[int],
            ComputedObservableProperty[float],
        ],
    ) -> None:
        widget.setReadOnly(True)
        observable.valueChanged.connect(lambda value: widget.setText(str(value)))
        observable.valueChanged.emit(observable.get())
        return None

    def binding_textedit_str(
        self,
        widget: QLineEdit,
        observable: typing.Union[
            ObservableProperty[str],
            ComputedObservableProperty[str],
        ],
    ) -> None:
        observable.valueChanged.connect(widget.setText)
        widget.textChanged.connect(observable.set)
        observable.valueChanged.emit(observable.get())
        return None

    def binding_label_number(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableProperty[int],
            ObservableProperty[float],
            ComputedObservableProperty[int],
            ComputedObservableProperty[float],
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

        observable.valueChanged.emit(observable.get())
        return

    def binding_label_string(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableProperty[str], ComputedObservableProperty[str]
        ],
    ) -> None:
        observable.valueChanged.connect(widget.setText)
        observable.valueChanged.emit(observable.get())
        return None

    # Commands
    def binding_command(
        self,
        widget: typing.Union[QPushButton, QToolButton, QAction, QRadioButton],
        command: RelayCommand,
    ) -> None:
        if isinstance(widget, (QAction, QToolButton)):
            widget.triggered.connect(command)
        if isinstance(widget, QPushButton):
            widget.clicked.connect(command)
        if isinstance(widget, QRadioButton):
            widget.clicked.connect(command)
        return None

    # SpinBox
    def binding_spinbox(
        self,
        widget: QSpinBox,
        observable: typing.Union[
            ObservableProperty[int],
            ComputedObservableProperty[int],
        ],
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
            ObservableProperty[float],
            ComputedObservableProperty[float],
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
        self,
        widget: QComboBox,
        observable: ObservableCollection[typing.Any],
        select_default: bool = True,
        max_visible_items: int = 7,
    ) -> None:
        # TODO: assume all value are converted into str before call addItems
        widget.setDuplicatesEnabled(False)
        widget.setMaxVisibleItems(max_visible_items)
        observable.valueChanged.connect(widget.clear)
        observable.valueChanged.connect(
            lambda values: self._fill_combobox_items(widget, values)
        )
        if select_default:
            observable.valueChanged.emit(observable.value)
            # widget.setCurrentIndex(0)
        else:
            widget.setCurrentIndex(-1)
            observable.valueChanged.emit(observable.value)
        return None

    def _fill_combobox_items(
        self, widget: QComboBox, values: typing.List[typing.Any]
    ) -> None:
        for value in values:
            if isinstance(value, Path):
                widget.addItem(value.name, userData=QVariant(value))
            else:
                widget.addItem(str(value), userData=QVariant(value))
        return

    def binding_combobox_value(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[str],
            ComputedObservableProperty[str],
        ],
    ) -> None:
        # TODO: assume all value are converted into str before call addItems
        # widget.currentTextChanged.connect(observable.set) Old
        # widget.currentTextChanged.emit(widget.currentText)
        widget.currentTextChanged.connect(lambda: observable.set(widget.currentData()))
        widget.currentTextChanged.emit(widget.currentText())
        return None

    def binding_combobox_realvalue(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[typing.Any], ComputedObservableProperty[typing.Any]
        ],
    ) -> None:
        warnings.warn("preview features")
        widget.currentTextChanged.connect(lambda: observable.set(widget.currentData()))
        widget.currentTextChanged.emit(widget.currentData())
        return None

    # QCheckBox
    def binding_checkbox(
        self,
        widget: QCheckBox,
        observable: typing.Union[
            ObservableProperty[bool], ComputedObservableProperty[bool]
        ],
    ) -> None:
        # TODO: handle each case along the checked state
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
