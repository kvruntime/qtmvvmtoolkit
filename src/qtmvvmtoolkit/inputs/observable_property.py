# -*- coding:utf-8 -*-
from pathlib import Path
import typing
from typing import Generic, TypeVar
import warnings

import pandas as pd
from PyQt6.QtCore import pyqtBoundSignal
from qtpy.QtCore import QObject, Signal

T = TypeVar("T", int, str, float, object, bool, pd.DataFrame, Path)
Types = [[object], [int], [float], [str], [bool], [pd.DataFrame], [Path]]


class ObservableProperty(QObject, Generic[T]):
    valueChanged = Signal(*Types, name="valueChanged")

    def __init__(self, value: T, item: T):
        super().__init__()
        self.item: T = item
        self.value: T = value
        self.set(value)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        # assert isinstance(value, self.item)
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


class ObservableBoolProperty(ObservableProperty[bool]):
    def __init__(self, value: bool) -> None:
        super().__init__(value, item=bool)
        return


class ObservableFloatProperty(ObservableProperty[float]):
    def __init__(self, value: float) -> None:
        super().__init__(value, item=float)
        return

    def binding_percent(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        warnings.warn("this method is depreacated")
        self.valueChanged.connect(lambda value: method(value * 100))
        self.valueChanged.emit(self.get())
        return None

    def rbinding_percent(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        warnings.warn("this method is depreacated")
        signal.connect(lambda value: self.set(value / 100))
        self.valueChanged.emit(self.get())
        return None


class ObservableIntProperty(ObservableProperty[int]):
    def __init__(self, value: int) -> None:
        super().__init__(value, item=int)
        return

    def binding_percent(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        warnings.warn("this method is depreacated")
        self.valueChanged.connect(lambda value: method(value * 100))
        self.valueChanged.emit(self.get())
        return None

    def binding_reverse_percent(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        warnings.warn("this method is depreacated")
        signal.connect(lambda value: self.set(value / 100))
        self.valueChanged.emit(self.get())
        return None


class ObservableStrProperty(ObservableProperty[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value, item=str)
        return


class ObservablePathProperty(ObservableProperty[Path]):
    def __init__(self, value: Path) -> None:
        super().__init__(value, item=Path)
        return


class ObservableDataFrameProperty(ObservableProperty[pd.DataFrame]):
    def __init__(self, value: pd.DataFrame) -> None:
        super().__init__(value, item=pd.DataFrame)
        return

    # TODO: reimplemented set methods
    def set(self, value: T):
        self.value = value
        self.valueChanged.emit(self.value)
        return
