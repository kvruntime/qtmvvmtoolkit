# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageNav.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QCommandLinkButton,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from mvvmkit.navigations.ButtonNav import NavButton

class Ui_PageNav(object):
    def setupUi(self, PageNav):
        if not PageNav.objectName():
            PageNav.setObjectName(u"PageNav")
        PageNav.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(PageNav)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBoxNavArea = QGroupBox(PageNav)
        self.groupBoxNavArea.setObjectName(u"groupBoxNavArea")
        self.verticalLayout = QVBoxLayout(self.groupBoxNavArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layoutNavBar = QVBoxLayout()
        self.layoutNavBar.setObjectName(u"layoutNavBar")

        self.verticalLayout.addLayout(self.layoutNavBar)

        self.buttonPage4 = NavButton(self.groupBoxNavArea)
        self.buttonPage4.setObjectName(u"buttonPage4")

        self.verticalLayout.addWidget(self.buttonPage4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBoxNavArea)

        self.routeView = QStackedWidget(PageNav)
        self.routeView.setObjectName(u"routeView")
        self.routeView.setFrameShape(QFrame.Box)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.checkBox = QCheckBox(self.page1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(75, 125, 74, 20))
        self.routeView.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.commandLinkButton = QCommandLinkButton(self.page2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(35, 125, 186, 41))
        self.routeView.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.radioButton = QRadioButton(self.page3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 115, 88, 20))
        self.routeView.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.gridLayout = QGridLayout(self.page4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.page4)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.page4)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.routeView.addWidget(self.page4)

        self.horizontalLayout.addWidget(self.routeView)


        self.retranslateUi(PageNav)

        self.routeView.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(PageNav)
    # setupUi

    def retranslateUi(self, PageNav):
        PageNav.setWindowTitle(QCoreApplication.translate("PageNav", u"Form", None))
        self.groupBoxNavArea.setTitle(QCoreApplication.translate("PageNav", u"GroupBox", None))
        self.buttonPage4.setText(QCoreApplication.translate("PageNav", u"Page4", None))
        self.checkBox.setText(QCoreApplication.translate("PageNav", u"CheckBox", None))
        self.commandLinkButton.setText(QCoreApplication.translate("PageNav", u"CommandLinkButton", None))
        self.radioButton.setText(QCoreApplication.translate("PageNav", u"RadioButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("PageNav", u"PushButton", None))
    # retranslateUi

