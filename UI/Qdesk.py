# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Qdesk.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Qdesk(object):
    def setupUi(self, Qdesk):
        Qdesk.setObjectName("Qdesk")
        Qdesk.resize(466, 356)
        Qdesk.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Qdesk.setAcceptDrops(True)
        Qdesk.setWindowOpacity(1.0)
        Qdesk.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(Qdesk)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")

        Qdesk.setCentralWidget(self.centralwidget)

        self.retranslateUi(Qdesk)
        QtCore.QMetaObject.connectSlotsByName(Qdesk)

    def retranslateUi(self, Qdesk):
        _translate = QtCore.QCoreApplication.translate
        Qdesk.setWindowTitle(_translate("Qdesk", "Qdesk"))
        self.pushButton.setText(_translate("Qdesk", "新建卡片"))
