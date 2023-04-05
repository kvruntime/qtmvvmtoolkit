# -*- coding:utf-8 -*-
import typing
from typing import Generic, Type, TypeVar

from PyQt6 import QtCore

Number = typing.Union[int, float]

T = TypeVar("T", int, str, float, object, Number, bool)
Types = [[object], [int], [float], [str]]


class ObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(self, prop: Type[T], item: Type[T]):
        super().__init__()
        self.item: Type[T] = item
        assert isinstance(prop, self.item)
        self.prop = prop
        self.set(prop)
        pass

    def get(self) -> T:
        return self.prop

    def set(self, value: Type[T]):
        assert isinstance(value, self.item)
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return


class ComputedObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(
            self,
            prop: Type[T],
            observable_props: typing.Sequence[ObservableProperty],
            update_function: typing.Callable,
            item: Type[T]
    ) -> None:
        super().__init__()
        self.prop = prop
        self.item = item
        assert isinstance(self.prop, self.item)
        
        self.update_function = update_function
        self.properties = observable_props
        
        for prop in self.properties:
            prop.valueChanged.emit(self.update)
        pass

    def get(self) -> T:
        return self.prop

    def set(self, value: T):
        self.prop = value
        self.valueChanged.emit(self.prop)
        return None

    def update(self) -> None:
        self.update_function()
        self.valueChanged.emit(self.prop)
        return None

    pass
