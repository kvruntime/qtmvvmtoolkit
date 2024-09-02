# -*- coding:utf-8 -*-
import typing
from typing import Any, Callable

from qtpy.QtCore import Slot


@Slot()
class RelayCommand:
    """Relay command for button"""

    @typing.overload
    def __init__(self, func: Callable[..., None]) -> None: ...

    @typing.overload
    def __init__(
        self, func: Callable[..., None], **kwargs: dict[typing.Any, typing.Any]
    ) -> None: ...

    def __init__(
        self, func: Callable[..., None], **kwargs: dict[typing.Any, typing.Any]
    ) -> None:
        self.func = func
        self.kwargs = kwargs
        return

    def __call__(self) -> Any:
        if self.kwargs:
            return self.func(**self.kwargs)
        return self.func()
        # return
