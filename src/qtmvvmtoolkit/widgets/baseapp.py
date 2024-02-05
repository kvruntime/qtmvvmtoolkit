# coding:utf-8
import sys
import typing
from pathlib import Path

from qtpy.QtGui import QFontDatabase, QGuiApplication, QFont
from qtpy.QtWidgets import QApplication, QMainWindow


class BaseApp(QApplication):
    def __init__(
        self,
        argv: typing.List[str],
        appShell: typing.Type[QMainWindow] = QMainWindow,
    ) -> None:
        super().__init__(argv)
        self.appShell = appShell()
        return

    def configureApplication(self, appName: str, appVersion: str, minWdth: int) -> None:
        self.setApplicationName(appName)
        self.setApplicationDisplayName(appName)
        self.setApplicationVersion(appVersion)
        self.appShell.setWindowTitle(appName)
        self.appShell.setMinimumWidth(minWdth)
        return None

    def centerWindow(self):
        qt_rectangle = self.appShell.frameGeometry()
        center_point = QGuiApplication.primaryScreen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.appShell.move(qt_rectangle.topLeft())
        return None

    def registerFont(self, fontFile: Path):
        if not fontFile.exists():
            return None

        fontId = QFontDatabase.addApplicationFont(str(fontFile))
        QFontDatabase.applicationFontFamilies(fontId)
        return None

    def useFont(self, fontId: str, fontSize: int = 10) -> None:
        self.setFont(QFont(fontId, fontSize))
        self.appShell.setFont(QFont(fontId, fontSize))
        return None

    def launch(self) -> None:
        sys.exit(self.exec())
