# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/hdd/repositories/qt/ui/features.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Features(object):
    def setupUi(self, Features):
        Features.setObjectName("Features")
        Features.resize(1276, 956)
        self.verticalLayout = QtWidgets.QVBoxLayout(Features)
        self.verticalLayout.setObjectName("verticalLayout")
        self.audio_parameters = QtWidgets.QGroupBox(Features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_parameters.sizePolicy().hasHeightForWidth())
        self.audio_parameters.setSizePolicy(sizePolicy)
        self.audio_parameters.setMinimumSize(QtCore.QSize(150, 0))
        self.audio_parameters.setCheckable(False)
        self.audio_parameters.setObjectName("audio_parameters")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.audio_parameters)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.audio_parameters)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.sample_rate = QtWidgets.QSpinBox(self.audio_parameters)
        self.sample_rate.setEnabled(False)
        self.sample_rate.setMinimum(1)
        self.sample_rate.setMaximum(88000)
        self.sample_rate.setProperty("value", 16000)
        self.sample_rate.setObjectName("sample_rate")
        self.horizontalLayout_16.addWidget(self.sample_rate)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.audio_parameters)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.encoding = QtWidgets.QSpinBox(self.audio_parameters)
        self.encoding.setEnabled(False)
        self.encoding.setMinimum(1)
        self.encoding.setMaximum(4)
        self.encoding.setProperty("value", 2)
        self.encoding.setObjectName("encoding")
        self.horizontalLayout_18.addWidget(self.encoding)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.audio_parameters)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.sample_t = QtWidgets.QDoubleSpinBox(self.audio_parameters)
        self.sample_t.setDecimals(4)
        self.sample_t.setMinimum(0.0001)
        self.sample_t.setSingleStep(0.5)
        self.sample_t.setProperty("value", 1.0)
        self.sample_t.setObjectName("sample_t")
        self.horizontalLayout_17.addWidget(self.sample_t)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_17)
        self.verticalLayout.addWidget(self.audio_parameters)
        self.preprocess = QtWidgets.QGroupBox(Features)
        self.preprocess.setObjectName("preprocess")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.preprocess)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preEmp_CB = QtWidgets.QCheckBox(self.preprocess)
        self.preEmp_CB.setChecked(True)
        self.preEmp_CB.setObjectName("preEmp_CB")
        self.horizontalLayout.addWidget(self.preEmp_CB)
        self.preEmp_SB = QtWidgets.QDoubleSpinBox(self.preprocess)
        self.preEmp_SB.setMinimum(0.01)
        self.preEmp_SB.setMaximum(0.99)
        self.preEmp_SB.setSingleStep(0.01)
        self.preEmp_SB.setProperty("value", 0.97)
        self.preEmp_SB.setObjectName("preEmp_SB")
        self.horizontalLayout.addWidget(self.preEmp_SB)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.preprocess)
        self.windows = QtWidgets.QGroupBox(Features)
        self.windows.setObjectName("windows")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.windows)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.windows)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.window_t_SP = QtWidgets.QDoubleSpinBox(self.windows)
        self.window_t_SP.setDecimals(3)
        self.window_t_SP.setMinimum(0.001)
        self.window_t_SP.setMaximum(1.0)
        self.window_t_SP.setSingleStep(0.001)
        self.window_t_SP.setProperty("value", 0.064)
        self.window_t_SP.setObjectName("window_t_SP")
        self.horizontalLayout_2.addWidget(self.window_t_SP)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.windows)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.stride_t_SB = QtWidgets.QDoubleSpinBox(self.windows)
        self.stride_t_SB.setDecimals(3)
        self.stride_t_SB.setMinimum(0.001)
        self.stride_t_SB.setMaximum(1.0)
        self.stride_t_SB.setSingleStep(0.001)
        self.stride_t_SB.setProperty("value", 0.032)
        self.stride_t_SB.setObjectName("stride_t_SB")
        self.horizontalLayout_3.addWidget(self.stride_t_SB)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.windows)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.window_fun_CoB = QtWidgets.QComboBox(self.windows)
        self.window_fun_CoB.setObjectName("window_fun_CoB")
        self.window_fun_CoB.addItem("")
        self.window_fun_CoB.addItem("")
        self.window_fun_CoB.addItem("")
        self.window_fun_CoB.addItem("")
        self.horizontalLayout_4.addWidget(self.window_fun_CoB)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.windows)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(Features)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.feature_CoB = QtWidgets.QComboBox(Features)
        self.feature_CoB.setEnabled(False)
        self.feature_CoB.setObjectName("feature_CoB")
        self.feature_CoB.addItem("")
        self.feature_CoB.addItem("")
        self.feature_CoB.addItem("")
        self.horizontalLayout_7.addWidget(self.feature_CoB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.feature_Widget = QtWidgets.QWidget(Features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_Widget.sizePolicy().hasHeightForWidth())
        self.feature_Widget.setSizePolicy(sizePolicy)
        self.feature_Widget.setObjectName("feature_Widget")
        self.verticalLayout.addWidget(self.feature_Widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(Features)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.output_row_LCD = QtWidgets.QLCDNumber(Features)
        self.output_row_LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_row_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_row_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.output_row_LCD.setProperty("intValue", 30)
        self.output_row_LCD.setObjectName("output_row_LCD")
        self.horizontalLayout_5.addWidget(self.output_row_LCD)
        self.label_6 = QtWidgets.QLabel(Features)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.output_col_LCD = QtWidgets.QLCDNumber(Features)
        self.output_col_LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_col_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_col_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.output_col_LCD.setObjectName("output_col_LCD")
        self.horizontalLayout_5.addWidget(self.output_col_LCD)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.change_PB = QtWidgets.QPushButton(Features)
        self.change_PB.setEnabled(False)
        self.change_PB.setObjectName("change_PB")
        self.horizontalLayout_8.addWidget(self.change_PB)
        self.setup_PB = QtWidgets.QPushButton(Features)
        self.setup_PB.setObjectName("setup_PB")
        self.horizontalLayout_8.addWidget(self.setup_PB)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Features)
        QtCore.QMetaObject.connectSlotsByName(Features)

    def retranslateUi(self, Features):
        _translate = QtCore.QCoreApplication.translate
        Features.setWindowTitle(_translate("Features", "Form"))
        self.audio_parameters.setTitle(_translate("Features", "Sample Parameters"))
        self.label_15.setText(_translate("Features", "Sample Rate"))
        self.sample_rate.setToolTip(_translate("Features", "<html><head/><body><p>Samples\'s sampling rate.</p></body></html>"))
        self.sample_rate.setSuffix(_translate("Features", "Hz"))
        self.label_17.setText(_translate("Features", "Encoding"))
        self.encoding.setToolTip(_translate("Features", "<html><head/><body><p>Sample encoding</p></body></html>"))
        self.encoding.setSuffix(_translate("Features", "B"))
        self.label_16.setText(_translate("Features", "Sample length"))
        self.sample_t.setToolTip(_translate("Features", "<html><head/><body><p>Expected sample duration.</p><p>Samples longer will be trimmed.</p><p>Sample shorter will be ignored.</p></body></html>"))
        self.sample_t.setSuffix(_translate("Features", "s"))
        self.preprocess.setTitle(_translate("Features", "Pre-processing"))
        self.preEmp_CB.setText(_translate("Features", "PreEmphasis"))
        self.preEmp_SB.setToolTip(_translate("Features", "<html><head/><body><p>PreEmphasis factor</p></body></html>"))
        self.windows.setTitle(_translate("Features", "Windows Parameters"))
        self.label.setText(_translate("Features", "Window length"))
        self.window_t_SP.setToolTip(_translate("Features", "<html><head/><body><p>Analysis window length</p></body></html>"))
        self.window_t_SP.setSuffix(_translate("Features", "s"))
        self.label_2.setText(_translate("Features", "Stride"))
        self.stride_t_SB.setToolTip(_translate("Features", "<html><head/><body><p>Analysis window stride</p></body></html>"))
        self.stride_t_SB.setSuffix(_translate("Features", "s"))
        self.label_3.setText(_translate("Features", "Window function"))
        self.window_fun_CoB.setToolTip(_translate("Features", "<html><head/><body><p>Window function to be applied.</p><p>Some features extraction process may have their own</p><p>window function.</p></body></html>"))
        self.window_fun_CoB.setItemText(0, _translate("Features", "none"))
        self.window_fun_CoB.setItemText(1, _translate("Features", "hamming"))
        self.window_fun_CoB.setItemText(2, _translate("Features", "hanning"))
        self.window_fun_CoB.setItemText(3, _translate("Features", "bark"))
        self.label_4.setText(_translate("Features", "Features"))
        self.feature_CoB.setItemText(0, _translate("Features", "mfcc"))
        self.feature_CoB.setItemText(1, _translate("Features", "lmfe"))
        self.feature_CoB.setItemText(2, _translate("Features", "plp"))
        self.label_5.setText(_translate("Features", "Ouput_size:"))
        self.output_row_LCD.setToolTip(_translate("Features", "<html><head/><body><p>Output vector number of row.</p></body></html>"))
        self.label_6.setText(_translate("Features", "x"))
        self.output_col_LCD.setToolTip(_translate("Features", "<html><head/><body><p>Output vector number of parameters.</p></body></html>"))
        self.change_PB.setText(_translate("Features", "Change Parameters"))
        self.setup_PB.setText(_translate("Features", "Setup Features Parameters"))
