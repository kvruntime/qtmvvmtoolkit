# Form implementation generated from reading ui file 'PageNav.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PageNav(object):
    def setupUi(self, PageNav):
        PageNav.setObjectName("PageNav")
        PageNav.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PageNav)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxNavArea = QtWidgets.QGroupBox(PageNav)
        self.groupBoxNavArea.setObjectName("groupBoxNavArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxNavArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutNavBar = QtWidgets.QVBoxLayout()
        self.layoutNavBar.setObjectName("layoutNavBar")
        self.verticalLayout.addLayout(self.layoutNavBar)
        self.buttonPage4 = NavButton(self.groupBoxNavArea)
        self.buttonPage4.setObjectName("buttonPage4")
        self.verticalLayout.addWidget(self.buttonPage4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBoxNavArea)
        self.routeView = QtWidgets.QStackedWidget(PageNav)
        self.routeView.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.routeView.setObjectName("routeView")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.page1)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.routeView.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.page2)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_3.addWidget(self.commandLinkButton)
        self.routeView.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton = QtWidgets.QRadioButton(self.page3)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.routeView.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.gridLayout = QtWidgets.QGridLayout(self.page4)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.page4)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.page4)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.routeView.addWidget(self.page4)
        self.horizontalLayout.addWidget(self.routeView)

        self.retranslateUi(PageNav)
        self.routeView.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(PageNav)

    def retranslateUi(self, PageNav):
        _translate = QtCore.QCoreApplication.translate
        PageNav.setWindowTitle(_translate("PageNav", "Form"))
        self.groupBoxNavArea.setTitle(_translate("PageNav", "NavBar"))
        self.buttonPage4.setText(_translate("PageNav", "Page4"))
        self.checkBox.setText(_translate("PageNav", "CheckBox"))
        self.commandLinkButton.setText(_translate("PageNav", "CommandLinkButton"))
        self.radioButton.setText(_translate("PageNav", "RadioButton"))
        self.pushButton_2.setText(_translate("PageNav", "PushButton"))
from mvvmkit.navigations.ButtonNav import NavButton
