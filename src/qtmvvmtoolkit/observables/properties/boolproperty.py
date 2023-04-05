from typing import Type
from .observableproperty import ObservableProperty


class ObservableBoolProperty(ObservableProperty[bool]):

    def __init__(self, value: Type[bool]):
        super().__init__(value, item=bool)
        pass
