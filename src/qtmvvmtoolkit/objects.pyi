# coding:utf-8

import typing

from qtpy.QtCore import QObject
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
    ) -> None: ...
    def binding(
        self,
        widget: QWidget,
        observable: ObservableProperty[typing.Any],
        prop: str,
    ) -> None: ...

    # Widgets
    def binding_widget(
        self,
        widget: QWidget,
        observable: typing.Union[
            ObservableProperty[bool], ComputedObservableProperty[bool]
        ],
        prop: typing.Literal["visibility", "state", "readonly"],
    ): ...

    # Input widgets
    def binding_textedit(
        self,
        widget: QLineEdit,
        observable: ObservableProperty[typing.Any],
        disable_editing: bool = False,
        bindings: typing.Literal["on-typing", "on-typed"] = "on-typed",
    ) -> None: ...
    def __handle_textedit_binding(
        self,
        widget: QLineEdit,
        observable: ObservableProperty[typing.Any],
    ) -> None: ...
    def binding_textedit_number(
        self,
        widget: QLineEdit,
        observable: typing.Union[
            ObservableProperty[int],
            ObservableProperty[float],
            ComputedObservableProperty[int],
            ComputedObservableProperty[float],
        ],
    ) -> None: ...
    def binding_textedit_str(
        self,
        widget: QLineEdit,
        observable: typing.Union[
            ObservableProperty[str],
            ComputedObservableProperty[str],
        ],
    ) -> None: ...
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
    ) -> None: ...
    def binding_label_string(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableProperty[str], ComputedObservableProperty[str]
        ],
    ) -> None: ...
    def binding_label(
        self,
        widget: QLabel,
        observable: typing.Union[
            ObservableProperty[typing.Any], ComputedObservableProperty[typing.Any]
        ],
    ) -> None: ...

    # SpinBox
    def binding_spinbox(
        self,
        widget: QSpinBox,
        observable: typing.Union[
            ObservableProperty[int],
            ComputedObservableProperty[int],
        ],
        transformer: typing.Optional[typing.Literal["percent"]] = None,
    ) -> None: ...
    def binding_doublespinbox(
        self,
        widget: QDoubleSpinBox,
        observable: typing.Union[
            ObservableProperty[float],
            ComputedObservableProperty[float],
        ],
        transformer: typing.Optional[typing.Literal["percent"]] = None,
    ) -> None: ...

    # Comboxbox
    def binding_combobox_items(
        self,
        widget: QComboBox,
        observable: ObservableCollection[typing.Any],
        select_default: bool = True,
        max_visible_items: int = 7,
    ) -> None: ...
    def _fill_combobox_items(
        self,
        widget: QComboBox,
        values: typing.List[typing.Any],
        display_name: typing.Optional[str] = None,
    ) -> None: ...
    def binding_combobox_value(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[str],
            ComputedObservableProperty[str],
        ],
    ) -> None: ...
    def binding_combobox_selection(
        self,
        widget: QComboBox,
        observable: typing.Union[
            ObservableProperty[typing.Any],
            ComputedObservableProperty[typing.Any],
        ],
    ) -> None: ...
    def binding_combobox(
        self,
        widget: QComboBox,
        observable: ObservableCollection[typing.Any],
        selection_default: bool = False,
        display_name: typing.Optional[str] = None,
        visibles_items: int = 7,
    ) -> None: ...

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
        ...

    def __handle_checkbox_binding(
        self,
        widget: QCheckBox,
        observable: typing.Union[
            ObservableProperty[bool],
            ComputedObservableProperty[bool],
        ],
    ) -> None: ...

    # Relayable
    def binding_relayable(
        self,
        func: typing.Callable[[], None],
        relayable: RelayableProperty,
    ) -> None: ...
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
    ) -> None: ...
