# coding:utf-8
import typing

from qtpy.QtWidgets import QMainWindow, QWidget
from .ishell import RouteItem, IShell


class MainWindowShell(IShell):
    def __init__(self, outlet: typing.Optional[QMainWindow] = None) -> None:
        self.outlet = outlet
        self.routes: dict[str, RouteItem] = dict()
        if self.outlet:
            self.current_page: QWidget = self.outlet.centralWidget()
            self.current_path: str = None
        return

    def set_outlet(self, outlet: QMainWindow) -> None:
        if not self.outlet:
            self.outlet = outlet
            self.current_page: QWidget = self.outlet.centralWidget()
        return None

    def register(self, route: RouteItem) -> None:
        self.routes.update({route.path: route})
        return None

    def goto(self, path: str) -> None:
        _new_widget = self.routes.get(path, None)
        if _new_widget and self.outlet:
            self.routes.update(
                {
                    self.current_path: RouteItem(
                        path=self.current_path,
                        element=self.outlet.takeCentralWidget(),
                    )
                }
            )
            self.outlet.setCentralWidget(_new_widget.element)
            self.current_page = self.outlet.centralWidget()
            self.current_path = path
        return None

    def go_previous(self) -> None:
        return super().go_previous()

    def go_next(self) -> None:
        return super().go_next()
