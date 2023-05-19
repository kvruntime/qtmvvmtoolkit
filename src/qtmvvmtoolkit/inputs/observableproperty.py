# -*- coding:utf-8 -*-
import typing
from typing import Generic, Type, TypeVar

from PyQt6.QtCore import *

T = TypeVar("T", int, str, float, object, bool)
Types = [[object], [int], [float], [str], [bool]]


class ObservableProperty(QObject, Generic[T]):
    valueChanged = pyqtSignal(*Types, name="valueChanged")

    def __init__(self, value: T, item: T):
        super().__init__()
        self.item: T = item
        self.value: T = value
        self.set(value)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        assert isinstance(value, self.item)
        if value != self.value:
            self.value = value
            self.valueChanged.emit(self.value)
        return

    def binding(self, method: typing.Callable[[typing.Any], None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def binding_reverse(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        signal.connect(self.set)
        return None

    def binding_reverse(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        signal.connect(self.set)
        return None


class ObservableBoolProperty(ObservableProperty[bool]):
    def __init__(self, value: Type[bool]) -> None:
        super().__init__(value, item=bool)
        pass


class ObservableFloatProperty(ObservableProperty[float]):
    def __init__(self, value: float) -> None:
        super().__init__(value, item=float)
        return


class ObservableIntProperty(ObservableProperty[int]):
    def __init__(self, value: int) -> None:
        super().__init__(value, item=int)
        return


class ObservableStrProperty(ObservableProperty[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value, item=str)
        return
