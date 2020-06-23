# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './tiff_io_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(371, 381)
        DockWidget.setFloating(True)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSelectTiff = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnSelectTiff.setMaximumSize(QtCore.QSize(90, 32))
        self.btnSelectTiff.setObjectName("btnSelectTiff")
        self.horizontalLayout.addWidget(self.btnSelectTiff)
        self.labelFileTiff = QtWidgets.QLabel(self.dockWidgetContents)
        self.labelFileTiff.setText("")
        self.labelFileTiff.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelFileTiff.setObjectName("labelFileTiff")
        self.horizontalLayout.addWidget(self.labelFileTiff)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSelectMetaFile = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnSelectMetaFile.setMaximumSize(QtCore.QSize(130, 32))
        self.btnSelectMetaFile.setObjectName("btnSelectMetaFile")
        self.horizontalLayout_3.addWidget(self.btnSelectMetaFile)
        self.labelFileMeta = QtWidgets.QLabel(self.dockWidgetContents)
        self.labelFileMeta.setText("")
        self.labelFileMeta.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelFileMeta.setObjectName("labelFileMeta")
        self.horizontalLayout_3.addWidget(self.labelFileMeta)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonAsArray = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonAsArray.setObjectName("radioButtonAsArray")
        self.verticalLayout_2.addWidget(self.radioButtonAsArray)
        self.radioButtonAsArrayMulti = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonAsArrayMulti.setObjectName("radioButtonAsArrayMulti")
        self.verticalLayout_2.addWidget(self.radioButtonAsArrayMulti)
        self.radioButtonImread = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonImread.setObjectName("radioButtonImread")
        self.verticalLayout_2.addWidget(self.radioButtonImread)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_axes_default = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_axes_default.setChecked(True)
        self.radioButton_axes_default.setObjectName("radioButton_axes_default")
        self.verticalLayout.addWidget(self.radioButton_axes_default)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_axes_custom = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_axes_custom.setText("")
        self.radioButton_axes_custom.setObjectName("radioButton_axes_custom")
        self.horizontalLayout_2.addWidget(self.radioButton_axes_custom)
        self.lineEdit_axes_custom = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_axes_custom.setText("")
        self.lineEdit_axes_custom.setMaxLength(4)
        self.lineEdit_axes_custom.setObjectName("lineEdit_axes_custom")
        self.horizontalLayout_2.addWidget(self.lineEdit_axes_custom)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.btnLoadIntoWorkEnv = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoadIntoWorkEnv.sizePolicy().hasHeightForWidth())
        self.btnLoadIntoWorkEnv.setSizePolicy(sizePolicy)
        self.btnLoadIntoWorkEnv.setObjectName("btnLoadIntoWorkEnv")
        self.verticalLayout_3.addWidget(self.btnLoadIntoWorkEnv)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)
        DockWidget.setTabOrder(self.btnSelectTiff, self.btnSelectMetaFile)
        DockWidget.setTabOrder(self.btnSelectMetaFile, self.radioButtonAsArray)
        DockWidget.setTabOrder(self.radioButtonAsArray, self.radioButtonAsArrayMulti)
        DockWidget.setTabOrder(self.radioButtonAsArrayMulti, self.radioButtonImread)
        DockWidget.setTabOrder(self.radioButtonImread, self.radioButton_axes_default)
        DockWidget.setTabOrder(self.radioButton_axes_default, self.radioButton_axes_custom)
        DockWidget.setTabOrder(self.radioButton_axes_custom, self.lineEdit_axes_custom)
        DockWidget.setTabOrder(self.lineEdit_axes_custom, self.btnLoadIntoWorkEnv)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Tiff file &I/O"))
        self.btnSelectTiff.setText(_translate("DockWidget", "Select file"))
        self.btnSelectMetaFile.setText(_translate("DockWidget", "Select meta data"))
        self.groupBox.setToolTip(_translate("DockWidget", "The options for “Load Method” correspond to the tifffile library method that is used for loading the images"))
        self.groupBox.setTitle(_translate("DockWidget", "Load Method:"))
        self.radioButtonAsArray.setToolTip(_translate("DockWidget", "Usually faster alternative to imread"))
        self.radioButtonAsArray.setText(_translate("DockWidget", "asarray"))
        self.radioButtonAsArrayMulti.setToolTip(_translate("DockWidget", "Use if tiff was created in append mode"))
        self.radioButtonAsArrayMulti.setText(_translate("DockWidget", "asarray - multi series"))
        self.radioButtonImread.setToolTip(_translate("DockWidget", "Should work for most tiffs if they were not created in append mode."))
        self.radioButtonImread.setText(_translate("DockWidget", "i&mread"))
        self.groupBox_2.setTitle(_translate("DockWidget", "Axes order"))
        self.radioButton_axes_default.setToolTip(_translate("DockWidget", "default option, usual dimensions"))
        self.radioButton_axes_default.setText(_translate("DockWidget", "2D: [t, x, y] || 3D: [t, z, x, y]"))
        self.lineEdit_axes_custom.setPlaceholderText(_translate("DockWidget", "Custom, ex: xyzt"))
        self.btnLoadIntoWorkEnv.setText(_translate("DockWidget", "Load into workEnv"))

