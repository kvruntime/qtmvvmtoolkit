from .observableproperty import ObservableProperty

import typing

Item = typing.TypeVar("Item", bound=typing.List)

class ObservableListProperty(ObservableProperty, typing.Generic[Item]):
    def __init__(self, prop:typing.List[Item]) -> None:
        super().__init__(prop)
        pass
    
    def get(self):
        return
    
    def set(self, value:typing.List[Item]):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return