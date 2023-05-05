import typing
from typing import Type

from .observableproperty import ComputedObservableProperty, ObservableProperty


class ObservableIntProperty(ObservableProperty[int]):
    def __init__(self, value: Type[int]):
        super().__init__(value, item=int)
        pass


class ComputedObservableIntProperty(ComputedObservableProperty[int]):
    def __init__(
        self,
        value: Type[int],
        observable_props: typing.Sequence[ObservableProperty],
        update_function: typing.Callable[..., Type[int]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=int)
        pass

    pass
