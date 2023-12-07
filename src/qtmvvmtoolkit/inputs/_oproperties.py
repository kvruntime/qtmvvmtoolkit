# coding:utf-8
import typing
from pathlib import Path
from typing import Generic, List, Sequence, TypeVar

from PyQt6.QtCore import pyqtBoundSignal
from qtpy.QtCore import QObject, Signal

T = TypeVar("T")


class _BaseTypes:
    def __init__(self) -> None:
        self.types_list: List[type] = [
            object,
            int,
            float,
            str,
            bool,
            Path,
        ]
        self.types: List[list[type]] = [[t] for t in self.types_list]
        return

    def register_new_types(self, types: Sequence[type]) -> None:
        for typ in types:
            self.types_list.append(typ)
            self.types.append([typ])
        return None


base_types = _BaseTypes()


class IObservableProperty(QObject):
    valueChanged = Signal(name="valueChanged")

    def get(self) -> typing.Any:
        ...

    def set(self, value: typing.Any):
        ...

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        ...

    def rbinding(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        ...


class ObservableProperty(IObservableProperty, Generic[T]):
    valueChanged = Signal(*base_types.types, name="valueChanged")

    def __init__(self, value: T):
        super().__init__()
        self.value: T = value
        self.set(value)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        if value != self.value:
            self.value = value
            self.valueChanged.emit(self.value)
        return

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def rbinding(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        signal.connect(self.set)
        self.valueChanged.emit(self.get())
        return None


class ComputedObservableProperty(QObject, Generic[T]):
    valueChanged = Signal(*base_types.types, name="valueChanged")

    def __init__(
        self,
        value: T,
        observable_props: typing.List[IObservableProperty],
        update_function: typing.Callable[..., T],
    ) -> None:
        super().__init__()
        self.value: T = value
        self.update_function = update_function
        self.observable_props = observable_props

        for observable_prop in self.observable_props:
            observable_prop.valueChanged.connect(self.update)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        # assert isinstance(value, self.item)
        self.value = value
        self.valueChanged.emit(self.value)
        return None

    def update(self) -> None:
        _result = self.update_function()
        self.set(_result)
        return None

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None
