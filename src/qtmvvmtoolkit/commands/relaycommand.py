from typing import Any, Callable

# Use this as decoartor of the callable


class RelayCommand:
    def __init__(self, func: Callable) -> None:
        self.func = func
        pass

    def __call__(self, *args) -> Any:
        self.func(args=args)
        pass
