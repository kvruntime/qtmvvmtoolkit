# coding:utf-8
import typing

# from PyQt6.QtCore import QObject
from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QComboBox

T = typing.TypeVar("T", int, str, float, object, bool, object)


class ObservableCollection(QObject, typing.Generic[T]):
    valueChanged = Signal(list, name="valueChanged")

    def __init__(self, value: list[T]) -> None:
        super().__init__()
        self.value = value
        return None

    def get(self) -> list[T]:
        return self.value

    def set(self, value: list[T]) -> None:
        self.value = value
        self.valueChanged.emit(value)
        return None

    def clear(self) -> None:
        self.value.clear()
        self.valueChanged.emit(self.value)
        return None

    def append(self, value: T) -> None:
        self.value.append(value)
        self.valueChanged.emit(self.value)
        return None

    def remove(self) -> None:
        self.valueChanged.emit(self.value)
        return None

    def extend(self, values: list[T]) -> None:
        self.value.extend(values)
        self.valueChanged.emit(self.value)
        return None

    def binding(self, method: typing.Callable[[typing.Any], None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def bind_combobox(self, widget: QComboBox):
        widget.clear()
        self.valueChanged.connect(widget.addItems)
        self.valueChanged.emit(self.value)
        return None

    # pop
    # __getitem__
    # index
    # __len__
    # __contains__
    # __iter__
