# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 980)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.FileMenusLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.FileMenusLayout.setContentsMargins(0, 0, 0, 0)
        self.FileMenusLayout.setObjectName("FileMenusLayout")
        self.openFileBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.openFileBtn.setObjectName("openFileBtn")
        self.FileMenusLayout.addWidget(self.openFileBtn, 0, 0, 1, 1)
        self.mesfile_label = QtWidgets.QLabel(self.layoutWidget)
        self.mesfile_label.setObjectName("mesfile_label")
        self.FileMenusLayout.addWidget(self.mesfile_label, 1, 0, 1, 1)
        self.imgs_listw = QtWidgets.QListWidget(self.layoutWidget)
        self.imgs_listw.setEnabled(False)
        self.imgs_listw.setObjectName("imgs_listw")
        self.FileMenusLayout.addWidget(self.imgs_listw, 2, 1, 1, 1)
        self.progressBarLabel = QtWidgets.QLabel(self.layoutWidget)
        self.progressBarLabel.setText("")
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.FileMenusLayout.addWidget(self.progressBarLabel, 3, 0, 1, 2)
        self.imgs_list_label = QtWidgets.QLabel(self.layoutWidget)
        self.imgs_list_label.setObjectName("imgs_list_label")
        self.FileMenusLayout.addWidget(self.imgs_list_label, 1, 1, 1, 1)
        self.mesfile_listw = QtWidgets.QListWidget(self.layoutWidget)
        self.mesfile_listw.setEnabled(False)
        self.mesfile_listw.setObjectName("mesfile_listw")
        self.FileMenusLayout.addWidget(self.mesfile_listw, 2, 0, 1, 1)
        self.listSplitSeq = QtWidgets.QListWidget(self.layoutWidget)
        self.listSplitSeq.setEnabled(False)
        self.listSplitSeq.setObjectName("listSplitSeq")
        self.FileMenusLayout.addWidget(self.listSplitSeq, 2, 2, 1, 1)
        self.imgs_list_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.imgs_list_label_2.setObjectName("imgs_list_label_2")
        self.FileMenusLayout.addWidget(self.imgs_list_label_2, 1, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 600))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnChangeSMap = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnChangeSMap.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnChangeSMap.sizePolicy().hasHeightForWidth())
        self.btnChangeSMap.setSizePolicy(sizePolicy)
        self.btnChangeSMap.setMinimumSize(QtCore.QSize(0, 10))
        self.btnChangeSMap.setMaximumSize(QtCore.QSize(100, 22))
        self.btnChangeSMap.setObjectName("btnChangeSMap")
        self.gridLayout.addWidget(self.btnChangeSMap, 3, 2, 1, 1)
        self.histogram = HistogramLUTWidget(self.layoutWidget1)
        self.histogram.setObjectName("histogram")
        self.gridLayout.addWidget(self.histogram, 1, 1, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 2)
        self.resetscaleBtn = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.resetscaleBtn.sizePolicy().hasHeightForWidth())
        self.resetscaleBtn.setSizePolicy(sizePolicy)
        self.resetscaleBtn.setMinimumSize(QtCore.QSize(0, 10))
        self.resetscaleBtn.setMaximumSize(QtCore.QSize(100, 22))
        self.resetscaleBtn.setObjectName("resetscaleBtn")
        self.gridLayout.addWidget(self.resetscaleBtn, 6, 1, 1, 1)
        self.graphicsView = GraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 6, 1)
        self.abortBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.abortBtn.setEnabled(False)
        self.abortBtn.setObjectName("abortBtn")
        self.gridLayout.addWidget(self.abortBtn, 0, 2, 1, 1)
        self.btnAddToProj = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnAddToProj.sizePolicy().hasHeightForWidth())
        self.btnAddToProj.setSizePolicy(sizePolicy)
        self.btnAddToProj.setMinimumSize(QtCore.QSize(0, 10))
        self.btnAddToProj.setMaximumSize(QtCore.QSize(100, 22))
        self.btnAddToProj.setObjectName("btnAddToProj")
        self.gridLayout.addWidget(self.btnAddToProj, 6, 2, 1, 1)
        self.btnResetSMap = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnResetSMap.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnResetSMap.sizePolicy().hasHeightForWidth())
        self.btnResetSMap.setSizePolicy(sizePolicy)
        self.btnResetSMap.setMinimumSize(QtCore.QSize(0, 10))
        self.btnResetSMap.setMaximumSize(QtCore.QSize(100, 22))
        self.btnResetSMap.setObjectName("btnResetSMap")
        self.gridLayout.addWidget(self.btnResetSMap, 4, 2, 1, 1)
        self.btnSplitSeq = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnSplitSeq.sizePolicy().hasHeightForWidth())
        self.btnSplitSeq.setSizePolicy(sizePolicy)
        self.btnSplitSeq.setMinimumSize(QtCore.QSize(0, 10))
        self.btnSplitSeq.setMaximumSize(QtCore.QSize(100, 22))
        self.btnSplitSeq.setObjectName("btnSplitSeq")
        self.gridLayout.addWidget(self.btnSplitSeq, 4, 1, 1, 1)
        self.btnExport = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnExport.sizePolicy().hasHeightForWidth())
        self.btnExport.setSizePolicy(sizePolicy)
        self.btnExport.setMinimumSize(QtCore.QSize(0, 10))
        self.btnExport.setMaximumSize(QtCore.QSize(100, 22))
        self.btnExport.setObjectName("btnExport")
        self.gridLayout.addWidget(self.btnExport, 5, 2, 1, 1)
        self.btnConcatSeqs = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnConcatSeqs.sizePolicy().hasHeightForWidth())
        self.btnConcatSeqs.setSizePolicy(sizePolicy)
        self.btnConcatSeqs.setMinimumSize(QtCore.QSize(0, 10))
        self.btnConcatSeqs.setMaximumSize(QtCore.QSize(100, 22))
        self.btnConcatSeqs.setObjectName("btnConcatSeqs")
        self.gridLayout.addWidget(self.btnConcatSeqs, 5, 1, 1, 1)
        self.add_roi_Btn = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.add_roi_Btn.sizePolicy().hasHeightForWidth())
        self.add_roi_Btn.setSizePolicy(sizePolicy)
        self.add_roi_Btn.setMinimumSize(QtCore.QSize(0, 10))
        self.add_roi_Btn.setMaximumSize(QtCore.QSize(100, 22))
        self.add_roi_Btn.setIconSize(QtCore.QSize(16, 16))
        self.add_roi_Btn.setObjectName("add_roi_Btn")
        self.gridLayout.addWidget(self.add_roi_Btn, 3, 1, 1, 1)
        self.roiPlot = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roiPlot.sizePolicy().hasHeightForWidth())
        self.roiPlot.setSizePolicy(sizePolicy)
        self.roiPlot.setMinimumSize(QtCore.QSize(0, 40))
        self.roiPlot.setObjectName("roiPlot")
        self.MotionCorGroup = QtWidgets.QGroupBox(self.splitter_2)
        self.MotionCorGroup.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MotionCorGroup.sizePolicy().hasHeightForWidth())
        self.MotionCorGroup.setSizePolicy(sizePolicy)
        self.MotionCorGroup.setMinimumSize(QtCore.QSize(0, 150))
        self.MotionCorGroup.setObjectName("MotionCorGroup")
        self.layoutWidget2 = QtWidgets.QWidget(self.MotionCorGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 1101, 114))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.boxDecay = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxDecay.sizePolicy().hasHeightForWidth())
        self.boxDecay.setSizePolicy(sizePolicy)
        self.boxDecay.setDecimals(3)
        self.boxDecay.setObjectName("boxDecay")
        self.horizontalLayout_2.addWidget(self.boxDecay)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.boxIter = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxIter.sizePolicy().hasHeightForWidth())
        self.boxIter.setSizePolicy(sizePolicy)
        self.boxIter.setObjectName("boxIter")
        self.horizontalLayout_2.addWidget(self.boxIter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.rigMotCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rigMotCheckBox.setObjectName("rigMotCheckBox")
        self.verticalLayout_2.addWidget(self.rigMotCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.boxX = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxX.sizePolicy().hasHeightForWidth())
        self.boxX.setSizePolicy(sizePolicy)
        self.boxX.setObjectName("boxX")
        self.horizontalLayout.addWidget(self.boxX)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.boxY = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxY.sizePolicy().hasHeightForWidth())
        self.boxY.setSizePolicy(sizePolicy)
        self.boxY.setObjectName("boxY")
        self.horizontalLayout.addWidget(self.boxY)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.boxThreads = QtWidgets.QSpinBox(self.layoutWidget2)
        self.boxThreads.setMinimum(1)
        self.boxThreads.setObjectName("boxThreads")
        self.horizontalLayout.addWidget(self.boxThreads)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_batch_Btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.add_batch_Btn.setObjectName("add_batch_Btn")
        self.horizontalLayout_4.addWidget(self.add_batch_Btn)
        self.motcorr_now_Btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.motcorr_now_Btn.setObjectName("motcorr_now_Btn")
        self.horizontalLayout_4.addWidget(self.motcorr_now_Btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.elasMotCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.elasMotCheckBox.setEnabled(False)
        self.elasMotCheckBox.setObjectName("elasMotCheckBox")
        self.verticalLayout.addWidget(self.elasMotCheckBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.sliderStrides = QtWidgets.QSlider(self.layoutWidget2)
        self.sliderStrides.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStrides.setObjectName("sliderStrides")
        self.verticalLayout.addWidget(self.sliderStrides)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sliderOverlaps = QtWidgets.QSlider(self.layoutWidget2)
        self.sliderOverlaps.setOrientation(QtCore.Qt.Horizontal)
        self.sliderOverlaps.setObjectName("sliderOverlaps")
        self.horizontalLayout_3.addWidget(self.sliderOverlaps)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.boxUpsample = QtWidgets.QSpinBox(self.layoutWidget2)
        self.boxUpsample.setMinimum(1)
        self.boxUpsample.setObjectName("boxUpsample")
        self.horizontalLayout_3.addWidget(self.boxUpsample)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.boxMaxDev = QtWidgets.QSpinBox(self.layoutWidget2)
        self.boxMaxDev.setObjectName("boxMaxDev")
        self.horizontalLayout_3.addWidget(self.boxMaxDev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.BatchesLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.BatchesLayout.setContentsMargins(0, 0, 0, 0)
        self.BatchesLayout.setObjectName("BatchesLayout")
        self.batchLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.batchLabel.setObjectName("batchLabel")
        self.BatchesLayout.addWidget(self.batchLabel)
        self.batch_listw = QtWidgets.QListWidget(self.layoutWidget3)
        self.batch_listw.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.batch_listw.setObjectName("batch_listw")
        self.BatchesLayout.addWidget(self.batch_listw)
        self.motioncorrlistLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.motioncorrlistLabel.setObjectName("motioncorrlistLabel")
        self.BatchesLayout.addWidget(self.motioncorrlistLabel)
        self.motioncorr_listw = QtWidgets.QListWidget(self.layoutWidget3)
        self.motioncorr_listw.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.motioncorr_listw.setObjectName("motioncorr_listw")
        self.BatchesLayout.addWidget(self.motioncorr_listw)
        self.denoisedlistLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.denoisedlistLabel.setObjectName("denoisedlistLabel")
        self.BatchesLayout.addWidget(self.denoisedlistLabel)
        self.denoised_listw = QtWidgets.QListWidget(self.layoutWidget3)
        self.denoised_listw.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.denoised_listw.setObjectName("denoised_listw")
        self.BatchesLayout.addWidget(self.denoised_listw)
        self.saveBatchBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.saveBatchBtn.setEnabled(False)
        self.saveBatchBtn.setObjectName("saveBatchBtn")
        self.BatchesLayout.addWidget(self.saveBatchBtn)
        self.AddSelProjBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.AddSelProjBtn.setEnabled(False)
        self.AddSelProjBtn.setObjectName("AddSelProjBtn")
        self.BatchesLayout.addWidget(self.AddSelProjBtn)
        self.gridLayout_2.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.rigMotCheckBox.toggled['bool'].connect(self.elasMotCheckBox.setEnabled)
        self.batch_listw.itemClicked['QListWidgetItem*'].connect(self.saveBatchBtn.toggle)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openFileBtn.setText(_translate("Form", "Open file(s)"))
        self.mesfile_label.setText(_translate("Form", "MES file contents"))
        self.imgs_list_label.setText(_translate("Form", "Images/stacks"))
        self.imgs_list_label_2.setText(_translate("Form", "Splits of current sequence"))
        self.btnChangeSMap.setToolTip(_translate("Form", "Set a Stimulus Map for only the image currently open"))
        self.btnChangeSMap.setText(_translate("Form", "Change sMap"))
        self.resetscaleBtn.setText(_translate("Form", "Reset scale"))
        self.abortBtn.setText(_translate("Form", "Abort"))
        self.btnAddToProj.setText(_translate("Form", "Add to Project"))
        self.btnResetSMap.setToolTip(_translate("Form", "Reset the Stimulus Map to the one set for this mes file"))
        self.btnResetSMap.setText(_translate("Form", "Reset sMap"))
        self.btnSplitSeq.setText(_translate("Form", "Split seq"))
        self.btnExport.setText(_translate("Form", "Export view"))
        self.btnConcatSeqs.setText(_translate("Form", "Concat seqs"))
        self.add_roi_Btn.setText(_translate("Form", "+ ROI"))
        self.MotionCorGroup.setTitle(_translate("Form", "Motion correction parameters"))
        self.label.setText(_translate("Form", "decay time: "))
        self.label_2.setText(_translate("Form", " iterations: "))
        self.rigMotCheckBox.setText(_translate("Form", "Rigid correction"))
        self.label_7.setText(_translate("Form", "max shifts X: "))
        self.label_11.setText(_translate("Form", "max shifts Y: "))
        self.label_12.setText(_translate("Form", "threads: "))
        self.add_batch_Btn.setText(_translate("Form", "Add to batch"))
        self.motcorr_now_Btn.setText(_translate("Form", "Process now"))
        self.elasMotCheckBox.setText(_translate("Form", "Elastic correction"))
        self.label_4.setText(_translate("Form", "strides"))
        self.label_5.setText(_translate("Form", "overlaps"))
        self.label_8.setText(_translate("Form", "upsample:"))
        self.label_3.setText(_translate("Form", "max deviation:"))
        self.batchLabel.setText(_translate("Form", "Batch"))
        self.motioncorrlistLabel.setText(_translate("Form", "Motion Corrected"))
        self.denoisedlistLabel.setText(_translate("Form", "Denoised"))
        self.saveBatchBtn.setText(_translate("Form", "Save batch"))
        self.AddSelProjBtn.setText(_translate("Form", "Add selection to project"))

from ..widgets.GraphicsView import GraphicsView
from ..widgets.HistogramLUTWidget import HistogramLUTWidget
from ..widgets.PlotWidget import PlotWidget
