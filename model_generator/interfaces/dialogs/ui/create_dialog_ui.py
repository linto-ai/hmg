# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 399)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_LE = QtWidgets.QLineEdit(self.groupBox)
        self.name_LE.setText("")
        self.name_LE.setObjectName("name_LE")
        self.horizontalLayout.addWidget(self.name_LE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.location_LE = QtWidgets.QLineEdit(self.groupBox)
        self.location_LE.setObjectName("location_LE")
        self.horizontalLayout_2.addWidget(self.location_LE)
        self.locationChange_PB = QtWidgets.QPushButton(self.groupBox)
        self.locationChange_PB.setObjectName("locationChange_PB")
        self.horizontalLayout_2.addWidget(self.locationChange_PB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_Button = QtWidgets.QPushButton(self.groupBox_2)
        self.add_Button.setObjectName("add_Button")
        self.verticalLayout_3.addWidget(self.add_Button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.hotwords_Widget = QtWidgets.QListWidget(self.groupBox_2)
        self.hotwords_Widget.setObjectName("hotwords_Widget")
        self.horizontalLayout_5.addWidget(self.hotwords_Widget)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.cancel_PB = QtWidgets.QPushButton(Dialog)
        self.cancel_PB.setObjectName("cancel_PB")
        self.horizontalLayout_4.addWidget(self.cancel_PB)
        self.create_PB = QtWidgets.QPushButton(Dialog)
        self.create_PB.setObjectName("create_PB")
        self.horizontalLayout_4.addWidget(self.create_PB)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create New Project"))
        self.groupBox.setTitle(_translate("Dialog", "Project Location"))
        self.label.setText(_translate("Dialog", "Project Name"))
        self.name_LE.setPlaceholderText(_translate("Dialog", "new_project"))
        self.label_2.setText(_translate("Dialog", "Project Location"))
        self.location_LE.setPlaceholderText(_translate("Dialog", "project folder will be created here"))
        self.locationChange_PB.setText(_translate("Dialog", "Change"))
        self.groupBox_2.setTitle(_translate("Dialog", "Keywords"))
        self.add_Button.setText(_translate("Dialog", "Add"))
        self.cancel_PB.setText(_translate("Dialog", "Cancel"))
        self.create_PB.setText(_translate("Dialog", "Create"))
