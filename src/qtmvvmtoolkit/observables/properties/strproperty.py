from typing import Type
from .observableproperty import ObservableProperty


class ObservableStrProperty(ObservableProperty[str]):

    def __init__(self, value: Type[str]) -> object:
        super().__init__(value, item=str)
        pass


