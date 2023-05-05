# -*- coding:utf-8 -*-
import typing
from typing import Generic, Type, TypeVar

from PyQt6 import QtCore
from PyQt6.QtCore import *

T = TypeVar("T", int, str, float, object, bool)
Types = [[object], [int], [float], [str], [bool]]


class ObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(self, value: Type[T], item: Type[T]):
        super().__init__()
        self.item: Type[T] = item
        assert isinstance(value, self.item)
        self.value: Type[T] = value
        self.set(value)
        pass

    def get(self) -> T:
        return self.value

    def set(self, value: Type[T]):
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

    def binding_reverse(self, signal: QtCore.pyqtBoundSignal) -> None:
        """Reverse binding method"""
        signal.connect(self.set)
        return None


class ComputedObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(
        self,
        value: Type[T],
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., Type[T]],
        item: Type[T],
    ) -> None:
        super().__init__()
        self.value: Type[T] = value
        self.item: Type[T] = item
        assert isinstance(self.value, self.item)
        self.update_function: typing.Callable[..., Type[T]] = update_function
        self.properties = observable_props

        for observable_prop in self.properties:
            observable_prop.valueChanged.connect(self.update)
        pass

    def get(self) -> Type[T]:
        return self.value

    def set(self, value: Type[T]):
        assert isinstance(value, self.item)
        self.value = value
        self.valueChanged.emit(self.value)
        return None

    def update(self) -> None:
        self.update_function()
        self.valueChanged.emit(self.value)
        _result = self.update_function()

        if _result and isinstance(_result, self.item):
            self.set(_result)
        return None

    def binding(self, method: typing.Callable[[], None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None