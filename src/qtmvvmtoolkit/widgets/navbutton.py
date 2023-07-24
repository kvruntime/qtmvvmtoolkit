# coding:utf-8
import typing
from pathlib import Path
import warnings

from qtpy.QtWidgets import QToolButton, QPushButton, QWidget
from qtpy.QtCore import QSize, Qt

from qtpy.QtGui import QIcon

from qtmvvmtoolkit.navigation import NavigationManager


class NavButton(QToolButton, QPushButton):
    def __init__(
        self,
        text: str = "",
        router: NavigationManager | None = None,
        path: str = "",
        icon_path: typing.Optional[Path] = None,
        icon: typing.Optional[QIcon] = None,
        parent: typing.Optional[QWidget] = None,
    ):
        super().__init__()
        self.setParent(parent)  # type: ignore FIXME: fix element assignation
        self.setText(text)
        self.setIconSize(QSize(30, 30))
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self._navigation_manager = router
        self._path = path

        if icon_path:
            self.setIcon(QIcon(icon_path.as_posix()))

        if icon:
            self.setIcon(icon)

        self.clicked.connect(self._goto)
        # config
        return

    def _goto(self):
        if self._navigation_manager:
            self._navigation_manager.goto(self._path)
        return None

    def set_navigation_manager(self, navigation_manager: NavigationManager):
        warnings.warn("deprecated: this function will be remove nextly")
        self._navigation_manager = navigation_manager
        return

    def set_path(self, path: str):
        warnings.warn("deprecated: this function will be remove nextly")
        self._path = path
        return None

    def set_config(self, navigation_manager: NavigationManager, path: str):
        self._navigation_manager = navigation_manager
        self._path = path
        return None
