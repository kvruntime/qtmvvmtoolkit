import typing
from typing import Type

from .observableproperty import ComputedObservableProperty, ObservableProperty


class ObservableStrProperty(ObservableProperty[str]):

    def __init__(self, value: Type[str]) -> object:
        super().__init__(value, item=str)
        pass


class ComputedObservableStrProperty(ComputedObservableProperty[str]):
    def __init__(
            self,
            value: Type[str],
            observable_props: typing.List[ObservableProperty],
            update_function: typing.Callable[..., Type[str]]
    ) -> None:
        super().__init__(value, observable_props, update_function, item=float)

    pass
