from typing import Type
from .observableproperty import ObservableProperty


class ObservableFloatProperty(ObservableProperty[float]):

    def __init__(self, prop: Type[float]):
        super().__init__(prop, item=float)
