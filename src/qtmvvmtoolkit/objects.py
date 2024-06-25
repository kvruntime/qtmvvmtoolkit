# coding:utf-8

import typing
import warnings

from qtpy.QtCore import QObject, Qt, QVariant
from qtpy.QtGui import QAction
from qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSpinBox,
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

    def binding(
        self,
        widget: QWidget,
        observable: ObservableProperty[typing.Any],
        prop: str,
    ) -> None:
        # to know the type of observable
        _type: type = typing.get_args(observable.__orig_class__)[0]

        match _type:
            case _ if isinstance(_type, int):
                print("int")
            case _ if isinstance(_type, float):
                print("float")
            case _ if isinstance(_type, str):
                print("str")
            case _:
                print("nothing")
        return None

    # Widgets
    def binding_widget(
        self,
        widget: QWidget,
        observable: typing.Union[
            ObservableProperty[bool], ComputedObservableProperty[bool]
        ],
        prop: typing.Literal["visibility", "state", "readonly"],
    ):
        if prop == "visibility":
            observable.valueChanged.connect(widget.setVisible)
        if prop == "state":
            observable.valueChanged.connect(widget.setEnabled)
        if prop == "readonly":
            if hasattr(widget, "setReadOnly"):
                observable.valueChanged.connect(widget.setReadOnly)
        observable.valueChanged.emit(observable.get())
        return None

    # Input widgets
    def binding_textedit(
        self,
        widget: QLineEdit,
        observable: ObservableProperty[typing.Any],
        disable_editing: bool = False,
        bindings: typing.Literal["on-typing", "on-typed"] = "on-typed",
    ) -> None:
        _type: typing.Type = observable.__orig_class__.__args__[0]

        if disable_editing:
            widget.setReadOnly(disable_editing)
        if _type == str:
            if bindings == "on-typing":
                widget.textChanged.connect(observable.set)

            if bindings == "on-typed":
                widget.editingFinished.connect(lambda: observable.set(widget.text()))

            observable.valueChanged.connect(widget.setText)
            observable.valueChanged.emit(observable.get())

        if _type in [int, float]:
            if bindings == "on-typing":
                # widget.textChanged.connect(observable.set)
                widget.textChanged.connect(
                    lambda: self.__handle_textedit_binding(widget, observable)
                )
                ...
            if bindings == "on-typed":
                # widget.editingFinished.connect(lambda: observable.set(widget.text()))
                widget.editingFinished.connect(
                    lambda: self.__handle_textedit_binding(widget, observable)
                )
                ...
            observable.valueChanged.connect(lambda value: widget.setText(str(value)))
            observable.valueChanged.emit(observable.get())
        return None

    def __handle_textedit_binding(
        self,
        widget: QLineEdit,
        observable: ObservableProperty[typing.Any],
    ) -> None:
        print("called")
        _type: typing.Type = observable.__orig_class__.__args__[0]
        try:
            _value = _type(eval(widget.text()))
            observable.set(_value)
        except NameError:
            widget.clear()
        except SyntaxError:
            widget.clear()
        return None

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
        warnings.warn("WARN: deprecated function")
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
        warnings.warn("WARN: deprecated function")
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

    def binding_label(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableProperty[typing.Any], ComputedObservableProperty[typing.Any]
        ],
    ) -> None:
        _type: typing.Type = observable.__orig_class__.__args__[0]

        if _type == str:
            observable.valueChanged.connect(widget.setText)
            observable.valueChanged.emit(observable.get())

        if _type in [int, float]:
            observable.valueChanged.connect(lambda value: widget.setText(str(value)))
            observable.valueChanged.emit(observable.get())
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
        warnings.warn("WARN: Deprecated features (use binding_combobox insted)")
        widget.setDuplicatesEnabled(False)
        widget.setMaxVisibleItems(max_visible_items)
        observable.valueChanged.connect(widget.clear)
        observable.valueChanged.connect(
            lambda values: self._fill_combobox_items(widget, values)
        )
        if select_default:
            observable.valueChanged.emit(observable.collection)
            # widget.setCurrentIndex(0)
        else:
            widget.setCurrentIndex(-1)
            observable.valueChanged.emit(observable.collection)
        return None

    def _fill_combobox_items(
        self,
        widget: QComboBox,
        values: typing.List[typing.Any],
        display_name: typing.Optional[str] = None,
    ) -> None:
        for value in values:
            if isinstance(value, (str, int, float)):
                widget.addItem(str(value), userData=QVariant(value))
            else:
                if display_name:
                    _display_name = getattr(value, display_name, None)
                    if _display_name:
                        widget.addItem(_display_name, userData=QVariant(value))
                else:
                    widget.addItem(str(value), userData=QVariant(value))

            # if isinstance(value, Path):
            #     widget.addItem(value.name, userData=QVariant(value))
            # else:
            #     widget.addItem(str(value), userData=QVariant(value))
        return None

    def binding_combobox_value(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[str],
            ComputedObservableProperty[str],
        ],
    ) -> None:
        warnings.warn("WARN: deprecated function")
        # TODO: assume all value are converted into str before call addItems
        # widget.currentTextChanged.connect(observable.set) Old
        # widget.currentTextChanged.emit(widget.currentText)
        widget.currentTextChanged.connect(lambda: observable.set(widget.currentData()))
        widget.currentTextChanged.emit(widget.currentText())
        return None

    def binding_combobox_selection(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[typing.Any],
            ComputedObservableProperty[typing.Any],
        ],
    ) -> None:
        warnings.warn("WARN: preview feature")
        widget.currentTextChanged.connect(lambda: observable.set(widget.currentData()))
        widget.currentTextChanged.emit(widget.currentText())
        # widget.currentTextChanged.emit(widget.currentData())
        # observable.set()
        return None

    def binding_combobox(
        self,
        widget: QComboBox,
        observable: ObservableCollection[typing.Any],
        selection_default: bool = False,
        display_name: typing.Optional[str] = None,
        visibles_items: int = 7,
    ) -> None:
        widget.setDuplicatesEnabled(False)
        widget.setMaxVisibleItems(visibles_items)
        widget.clear()

        observable.valueChanged.connect(widget.clear)
        observable.valueChanged.connect(
            lambda values: self._fill_combobox_items(widget, values, display_name)
        )
        if selection_default:
            observable.valueChanged.emit(observable.collection)
            # widget.setCurrentIndex(0)
        else:
            observable.valueChanged.emit(observable.collection)
            widget.setCurrentIndex(-1)
        return None

    # QCheckBox
    def binding_checkbox(
        self,
        widget: QCheckBox,
        observable: typing.Union[
            ObservableProperty[bool],
            ComputedObservableProperty[bool],
        ],
    ) -> None:
        # TODO: handle each case along the checked state
        observable.valueChanged.connect(widget.setChecked)
        widget.stateChanged.connect(
            lambda: self.__handle_checkbox_binding(widget, observable)
        )
        observable.valueChanged.emit(observable.get())
        return None

    def __handle_checkbox_binding(
        self,
        widget: QCheckBox,
        observable: typing.Union[
            ObservableProperty[bool],
            ComputedObservableProperty[bool],
        ],
    ) -> None:
        if widget.checkState() == Qt.CheckState.Checked:
            observable.set(True)
        if widget.checkState() == Qt.CheckState.Unchecked:
            observable.set(False)
        return None

    # Relayable
    def binding_relayable(
        self,
        func: typing.Callable[[], None],
        relayable: RelayableProperty,
    ) -> None:
        relayable.relayed.connect(func)
        return None

    # Commands
    def binding_command(
        self,
        widget: typing.Union[
            QPushButton,
            QToolButton,
            QAction,
            QRadioButton,
        ],
        command: RelayCommand,
    ) -> None:
        if isinstance(widget, (QAction, QToolButton)):
            widget.triggered.connect(command)
        if isinstance(widget, QPushButton):
            widget.clicked.connect(command)
        if isinstance(widget, QRadioButton):
            widget.clicked.connect(command)
        return None
