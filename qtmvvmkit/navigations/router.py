from abc import ABC, abstractmethod
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget
from typing import Dict


class Router(ABC):
    @abstractmethod
    def __init__(self, target: QObject) -> None:
        super().__init__()
        self.target = target
        self.routes: Dict[str, QObject]
        pass

    @abstractmethod
    def registerRoute(self, path: str, element: QWidget):
        return None

    @abstractmethod
    def goTo(self, path: str):
        pass
    
    @abstractmethod
    def goToNext(self):
        pass

    @abstractmethod
    def goToPrevious(self):
        pass