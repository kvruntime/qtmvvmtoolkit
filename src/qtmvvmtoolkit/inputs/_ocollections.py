# coding:utf-8
import typing

# from PyQt6.QtCore import QObject
from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QComboBox
from typing import TypeVar, Generic, Callable, Any


_T = TypeVar("_T")


class ObservableSignals(QObject):
    valueChanged = Signal(object)


class SigInst(Generic[_T]):
    @staticmethod
    def connect(slot: Callable[[_T], Any], type: type | None = ...) -> None:
        ...

    @staticmethod
    def disconnect(slot: Callable[[_T], Any] = ...) -> None:
        ...

    @staticmethod
    def emit(*args: _T) -> None:
        ...


class ObservableCollection(QObject, typing.Generic[_T]):
    valueChanged: SigInst[_T]

    def __init__(self, value: list[_T]) -> None:
        super().__init__()
        self.value = value
        self.signals = ObservableSignals()
        return None

    def get(self) -> list[_T]:
        return self.value

    def set(self, value: list[_T]) -> None:
        self.value = value
        self.valueChanged.emit(value)
        return None

    def clear(self) -> None:
        self.value.clear()
        self.valueChanged.emit(self.value)
        return None

    def append(self, value: _T) -> None:
        self.value.append(value)
        self.valueChanged.emit(self.value)
        return None

    def remove(self) -> None:
        self.valueChanged.emit(self.value)
        return None

    def extend(self, values: list[_T]) -> None:
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

    def __getattr__(self, name: str) -> SigInst:
        attr = getattr(self.signals.__class__, name, None)
        if isinstance(attr, Signal):
            return getattr(self.signals, name)
        raise AttributeError(
            f"{self.__class__.name!r} object has no attribute {name!r}"
        )

    # pop
    # __getitem__
    # index
    # __len__
    # __contains__
    # __iter__
