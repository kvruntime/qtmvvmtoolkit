import typing
from PyQt6.QtWidgets import QPushButton, QWidget
from qtmvvmtoolkit.navigations.navigationmanager import NavigationManager
from pathlib import Path
from PyQt6.QtGui import QIcon


class NavButton(QPushButton):
    def __init__(
        self,
        parent: typing.Optional[QWidget] = None,
        *,
        text: str = "",
        router: NavigationManager | None = None,
        path: str = "",
        icon_path: typing.Optional[Path] = None
    ):
        super().__init__()
        self.setParent(parent)  # type: ignore FIXME: fix element assignation
        self.setText(text)
        self._navigation_manager = router
        self._path = path
        # type: ignore FIXME: fix element assignation
        self.setIcon(QIcon(icon_path.as_posix())) if icon_path else None

        self._binds()
        pass

    def _goto(self):
        if self._navigation_manager:
            self._navigation_manager.goto(self._path)
        return None

    def set_navigation_manager(self, navigation_manager: NavigationManager):
        self._navigation_manager = navigation_manager
        return

    def set_path(self, path: str):
        self._path = path
        return None

    def _binds(self):
        self.clicked.connect(self._goto)
        return None
