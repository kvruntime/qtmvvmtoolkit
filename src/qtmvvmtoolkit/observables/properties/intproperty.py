from typing import Type
from .observableproperty import ObservableProperty

class ObservableIntProperty(ObservableProperty[int]):

    def __init__(self, prop: Type[int]):
        super().__init__(prop, item=int)
        pass
