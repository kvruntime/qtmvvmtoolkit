import typing
from typing import Generic, Type, TypeVar

from PyQt6 import QtCore
from PyQt6.QtCore import *

from .observableproperty import ObservableProperty

T = TypeVar("T", int, str, float, object, bool)
Types = [[object], [int], [float], [str], [bool]]


class ComputedObservableProperty(Generic[T], QtCore.QObject):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(
        self,
        value: Type[T],
        observable_props: typing.List[ObservableProperty[typing.Any]],
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
        return

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


class ComputedObservableBoolProperty(ComputedObservableProperty[bool]):
    def __init__(
        self,
        value: Type[bool],
        observable_props: typing.List[ObservableProperty[typing.Any]],
        update_function: typing.Callable[..., Type[bool]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=bool)
        return


class ComputedObservableFloatProperty(ComputedObservableProperty[float]):
    def __init__(
        self,
        value: Type[float],
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., Type[float]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=float)
        return


class ComputedObservableIntProperty(ComputedObservableProperty[int]):
    def __init__(
        self,
        value: Type[int],
        observable_props: typing.Sequence[ObservableProperty[typing.Any]],
        update_function: typing.Callable[..., Type[int]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=int)
        pass


class ComputedObservableStrProperty(ComputedObservableProperty[str]):
    def __init__(
        self,
        value: Type[str],
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., Type[str]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=float)
        return
