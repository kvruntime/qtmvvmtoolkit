import typing
from typing import Type

from .observableproperty import ComputedObservableProperty, ObservableProperty


class ObservableBoolProperty(ObservableProperty[bool]):
    def __init__(self, value: Type[bool]):
        super().__init__(value, item=bool)
        pass


class ComputedObservableBoolProperty(ComputedObservableProperty[bool]):
    def __init__(
        self,
        value: Type[bool],
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., Type[bool]],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=bool)
        pass

    pass
