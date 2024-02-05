import typing
from qtpy.QtWidgets import *
from qtpy.QtGui import QIcon


class Shell:
    _Current: typing.Any

    def __init__(self) -> None:
        self._outlet: typing.Union[QTabWidget, QStackedWidget]
        self._routes: typing.Dict[str, QWidget] = {}
        return

    @classmethod
    @property
    def Current(cls):
        try:
            if Shell.__Default:
                return Shell.__Default
        except AttributeError:
            Shell.__Default = Shell()
            return Shell.__Default

    def add_outlet(
        self,
        outlet: typing.Union[QStackedWidget, QTabWidget],
    ):
        self._outlet = outlet
        return

    def register_route(self, route: str, widget: QWidget) -> None:
        if isinstance(widget, (QTabWidget)):
            self._register_for_tab(route, widget)
        if isinstance(widget, (QStackedWidget)):
            self._register_for_stacked(widget)
        self._routes.update({route: widget})
        return

    def _register_for_tab(self, route: str, widget: QWidget) -> None:
        self._outlet.addTab(widget, route)
        return None

    def _register_for_stacked(self, widget: QWidget) -> None:
        self._outlet.addWidget(widget)
        return None

    def goto(self, route: str) -> None:
        _widget = self._routes.get(route)
        if _widget:
            self._outlet.setCurrentWidget(_widget)
        return None

    def bind_navigation(
        self,
        button: typing.Union[QPushButton, QToolButton],
        route: str,
        icon: typing.Optional[QIcon] = None,
    ) -> None:
        if icon:
            button.setIcon(icon)
        button.clicked.connect(lambda: self.goto(route))
        return None
