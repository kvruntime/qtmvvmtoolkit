import sys
import typing
from pathlib import Path

from PyQt6 import QtGui, QtWidgets


class BaseApp(QtWidgets.QApplication):
    def __init__(
        self,
        argv: typing.List[str],
        appShell: typing.Type[QtWidgets.QMainWindow] = QtWidgets.QMainWindow,
    ) -> None:
        super().__init__(argv)
        self.appShell = appShell()
        pass

    def configureApplication(self, appName: str, appVersion: str, minWdth: int) -> None:
        self.setApplicationName(appName)
        self.setApplicationDisplayName(appName)
        self.setApplicationVersion(appVersion)
        self.appShell.setWindowTitle(appName)
        self.appShell.setMinimumWidth(minWdth)
        return None

    def centerWindow(self):
        qt_rectangle = self.appShell.frameGeometry()
        center_point = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        )
        qt_rectangle.moveCenter(center_point)
        self.appShell.move(qt_rectangle.topLeft())
        return None

    def registerFont(self, fontFile: Path):
        if not fontFile.exists():
            return None

        fontId = QtGui.QFontDatabase.addApplicationFont(str(fontFile))
        QtGui.QFontDatabase.applicationFontFamilies(fontId)
        return None

    def useFont(self, fontId: str, fontSize: int = 10) -> None:
        self.setFont(QtGui.QFont(fontId, fontSize))
        self.appShell.setFont(QtGui.QFont(fontId, fontSize))
        return None

    def launch(self) -> None:
        sys.exit(self.exec())
