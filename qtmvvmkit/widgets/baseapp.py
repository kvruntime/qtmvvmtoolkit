from PyQt6.QtWidgets import QApplication
from pathlib import Path
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFontDatabase, QFont, QIcon

class BaseApp(QApplication):
    def configure(self):
        self.setApplicationName("KYA-EcoLabel")
        self.setApplicationDisplayName("KYA-EcoLabel")
        self.setApplicationVersion("")
        
        return None

    def addFont(self, font_file: Path):
        if not font_file.exists():
            return
        font_id = QFontDatabase.addApplicationFont(str(font_file))
        family = QFontDatabase.applicationFontFamilies(font_id)
        print(family)
        return None

    def useFont(self, family: str, size:int=10):
        self.setFont(QFont(family, size))
        return None


    
    def setIcon(self, filename:str):
        self.setWindowIcon(QIcon(filename))

    def useStyleSheet(self, style_file: Path):
        if not style_file.exists():
            return
        self.setStyleSheet(style_file.read_text(encoding="utf-8"))
    pass