from typing import Type
import typing
from .observableproperty import ObservableProperty, ComputedObservableProperty


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
