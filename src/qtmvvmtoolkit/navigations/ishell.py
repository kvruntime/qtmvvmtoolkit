# coding:utf-8

from dataclasses import dataclass
import typing
from qtpy.QtWidgets import QWidget
from qtpy.QtCore import QObject


@dataclass
class RouteItem:
    path: str
    element: QWidget


class IShell:
    def __init__(self, outlet: typing.Optional[QObject] = None) -> None:
        self.outlet = outlet
        self.routes: dict[str, RouteItem] = dict()
        # if self.outlet:
        #     self.current_page: QWidget = self.outlet.centralWidget()
        #     self.current_path: str = None
        return

    def register_outlet(self, outlet: QObject) -> None:
        raise NotImplementedError("Must be implemented")

    def add_route(self, route: RouteItem) -> None:
        self.routes.update({route.path: route})
        return None

    def goto(self, path: str) -> None:
        raise NotImplementedError("Must be implemented")

    def go_next(self) -> None:
        raise NotImplementedError("Must be implemented")

    def go_previous(self) -> None:
        raise NotImplementedError("Must be implemented")
