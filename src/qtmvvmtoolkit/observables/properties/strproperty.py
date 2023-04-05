from typing import Type
from .observableproperty import ObservableProperty


class ObservableStrProperty(ObservableProperty[str]):

    def __init__(self, prop: Type[str]) -> object:
        super().__init__(prop, item=str)
        pass
