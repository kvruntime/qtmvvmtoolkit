from PyQt6.QtWidgets import QWidget
from typing import Type

# NOTE: start formel route implementation
class Route:
    def __init__(self, path:str, element:Type[QWidget]) -> None:
        self.path=path
        self.element=element
        pass
    
    def getPath(self):
        pass

    def getElement(self):
        pass