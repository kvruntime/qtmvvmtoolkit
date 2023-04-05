# -*- coding:utf-8 -*-
import typing
from typing import Generic, Type, TypeVar, NewType

from PyQt6 import QtCore

# Number = typing.Union[int, float]

T = TypeVar("T", int, str, float, object, bool)
Types = [[object], [int], [float], [str], [bool]]



class ObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(self, prop: Type[T], item: Type[T]):
        super().__init__()
        self.item: Type[T] = item
        assert isinstance(prop, self.item)
        self.prop:Type[T] = prop
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
            update_function: typing.Callable[..., Type[T]],
            item: Type[T]
    ) -> None:
        super().__init__()
        self.prop:Type[T] = prop
        self.item:Type[T] = item
        assert isinstance(self.prop, self.item)

        self.update_function:typing.Callable[..., Type[T]] = update_function
        self.properties = observable_props

        for observable_prop in self.properties:
            observable_prop.valueChanged.emit(self.update)
        pass

    def get(self) -> Type[T]:
        return self.prop

    def set(self, value: Type[T]):
        self.prop = value
        self.valueChanged.emit(self.prop)
        return None

    def update(self) -> None:
        self.update_function()
        self.valueChanged.emit(self.prop)

        # NOTE:New experimenting feature
        self.set(self.update_function())
        return None

    pass
