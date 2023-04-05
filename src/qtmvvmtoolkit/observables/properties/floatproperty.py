from typing import Type
from .observableproperty import ObservableProperty


class ObservableFloatProperty(ObservableProperty[float]):

    def __init__(self, value: Type[float]):
        super().__init__(value, item=float)
