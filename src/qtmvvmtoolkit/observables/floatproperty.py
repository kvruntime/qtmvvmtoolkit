import typing
from typing import Type

from .observableproperty import ComputedObservableProperty, ObservableProperty


class ObservableFloatProperty(ObservableProperty[float]):
    def __init__(self, value: Type[float]):
        super().__init__(value, item=float)


class ComputedObservableFloatProperty(ComputedObservableProperty[float]):
    def __init__(
        self,
        value: Type[float],
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., Type[float]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=float)

    pass
