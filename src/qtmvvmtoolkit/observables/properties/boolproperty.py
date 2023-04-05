from typing import Type
from .observableproperty import ObservableProperty


class ObservableBoolProperty(ObservableProperty[bool]):

    def __init__(self, prop: Type[bool]):
        super().__init__(prop, item=bool)
        pass
