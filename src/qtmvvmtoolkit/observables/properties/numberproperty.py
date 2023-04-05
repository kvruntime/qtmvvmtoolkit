import typing

from .observableproperty import ObservableProperty

Number = typing.Union[int,float]

class ObservableNumberProperty(ObservableProperty[Number]):

    def __init__(self, prop: typing.Type[Number]):
        super().__init__(prop, item=Number)
        pass