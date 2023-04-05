import typing

from .observableproperty import ObservableProperty

Number = typing.Union[int,float]

class ObservableNumberProperty(ObservableProperty[Number]):

    def __init__(self, value: typing.Type[Number]):
        super().__init__(value, item=Number)
        pass