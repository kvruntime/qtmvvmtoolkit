# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.entryUserName = QLineEdit(Form)
        self.entryUserName.setObjectName(u"entryUserName")

        self.gridLayout.addWidget(self.entryUserName, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.entryEmail = QLineEdit(Form)
        self.entryEmail.setObjectName(u"entryEmail")

        self.gridLayout.addWidget(self.entryEmail, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelUserName = QLabel(Form)
        self.labelUserName.setObjectName(u"labelUserName")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelUserName.setFont(font)
        self.labelUserName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelUserName)

        self.labelEmail = QLabel(Form)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setFont(font)
        self.labelEmail.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelEmail)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonSend = QPushButton(Form)
        self.buttonSend.setObjectName(u"buttonSend")

        self.verticalLayout_2.addWidget(self.buttonSend)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Email", None))
        self.labelUserName.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.buttonSend.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

