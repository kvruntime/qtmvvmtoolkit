# coding:utf-8

import typing

from qtpy.QtCore import QObject
from qtpy.QtGui import QAction
from qtpy.QtWidgets import (
    QComboBox,
    QPushButton,
    QRadioButton,
    QToolButton,
    QWidget,
)

from qtmvvmtoolkit.commands import RCommand, RelayCommand
from qtmvvmtoolkit.inputs import (
    ComputedObservableProperty,
    ObservableCollection,
    ObservableProperty,
)

T = typing.TypeVar("T")

class BindableObject(QObject):
    def __init__(
        self,
        parent: typing.Optional[QWidget] = None,
    ) -> None: ...
    def binding_state(
        self,
        widget: QWidget,
        observable: typing.Union[
            ObservableProperty[bool], ComputedObservableProperty[bool]
        ],
        prop: typing.Literal["visibility", "state", "readonly"],
    ) -> None: ...
    def binding_value(
        self,
        widget: QWidget,
        observable: typing.Union[ObservableProperty[T], ComputedObservableProperty[T]],
        *,
        string_format: typing.Optional[str] = None,
        mode: typing.Literal["1-way", "2-way"] = "2-way",
        bindings: typing.Literal["on-typing", "on-typed"] = "on-typed",
        use_percentage: bool | None = None,
    ) -> None: ...
    def binding_rcommand(
        self,
        widget: QObject,
        command: RCommand,
    ) -> None: ...
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
