# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_window_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.btnViewer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnViewer.sizePolicy().hasHeightForWidth())
        self.btnViewer.setSizePolicy(sizePolicy)
        self.btnViewer.setMinimumSize(QtCore.QSize(131, 118))
        self.btnViewer.setMaximumSize(QtCore.QSize(131, 118))
        self.btnViewer.setAutoFillBackground(True)
        self.btnViewer.setText("")
        self.btnViewer.setFlat(False)
        self.btnViewer.setObjectName("btnViewer")
        self.verticalLayout_3.addWidget(self.btnViewer)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.btnFlowchart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFlowchart.sizePolicy().hasHeightForWidth())
        self.btnFlowchart.setSizePolicy(sizePolicy)
        self.btnFlowchart.setMinimumSize(QtCore.QSize(131, 118))
        self.btnFlowchart.setMaximumSize(QtCore.QSize(131, 118))
        self.btnFlowchart.setAutoFillBackground(True)
        self.btnFlowchart.setText("")
        self.btnFlowchart.setFlat(False)
        self.btnFlowchart.setObjectName("btnFlowchart")
        self.verticalLayout_4.addWidget(self.btnFlowchart)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayoutProjectBrowser = QtWidgets.QVBoxLayout()
        self.verticalLayoutProjectBrowser.setObjectName("verticalLayoutProjectBrowser")
        self.labelProjectBrowser = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProjectBrowser.sizePolicy().hasHeightForWidth())
        self.labelProjectBrowser.setSizePolicy(sizePolicy)
        self.labelProjectBrowser.setObjectName("labelProjectBrowser")
        self.verticalLayoutProjectBrowser.addWidget(self.labelProjectBrowser)
        self.btnProjectBrowser = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProjectBrowser.sizePolicy().hasHeightForWidth())
        self.btnProjectBrowser.setSizePolicy(sizePolicy)
        self.btnProjectBrowser.setMinimumSize(QtCore.QSize(131, 118))
        self.btnProjectBrowser.setMaximumSize(QtCore.QSize(131, 118))
        self.btnProjectBrowser.setAutoFillBackground(True)
        self.btnProjectBrowser.setText("")
        self.btnProjectBrowser.setFlat(False)
        self.btnProjectBrowser.setObjectName("btnProjectBrowser")
        self.verticalLayoutProjectBrowser.addWidget(self.btnProjectBrowser)
        self.horizontalLayout.addLayout(self.verticalLayoutProjectBrowser)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelOpenProject = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOpenProject.sizePolicy().hasHeightForWidth())
        self.labelOpenProject.setSizePolicy(sizePolicy)
        self.labelOpenProject.setObjectName("labelOpenProject")
        self.verticalLayout_2.addWidget(self.labelOpenProject)
        self.btnOpenProject = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenProject.sizePolicy().hasHeightForWidth())
        self.btnOpenProject.setSizePolicy(sizePolicy)
        self.btnOpenProject.setMinimumSize(QtCore.QSize(131, 118))
        self.btnOpenProject.setMaximumSize(QtCore.QSize(131, 118))
        self.btnOpenProject.setAutoFillBackground(True)
        self.btnOpenProject.setText("")
        self.btnOpenProject.setFlat(False)
        self.btnOpenProject.setObjectName("btnOpenProject")
        self.verticalLayout_2.addWidget(self.btnOpenProject)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNewProj = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNewProj.sizePolicy().hasHeightForWidth())
        self.labelNewProj.setSizePolicy(sizePolicy)
        self.labelNewProj.setObjectName("labelNewProj")
        self.verticalLayout.addWidget(self.labelNewProj)
        self.btnNewProject = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewProject.sizePolicy().hasHeightForWidth())
        self.btnNewProject.setSizePolicy(sizePolicy)
        self.btnNewProject.setMinimumSize(QtCore.QSize(131, 118))
        self.btnNewProject.setMaximumSize(QtCore.QSize(131, 118))
        self.btnNewProject.setAutoFillBackground(True)
        self.btnNewProject.setText("")
        self.btnNewProject.setFlat(False)
        self.btnNewProject.setObjectName("btnNewProject")
        self.verticalLayout.addWidget(self.btnNewProject)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelRecentProjects = QtWidgets.QLabel(self.centralwidget)
        self.labelRecentProjects.setObjectName("labelRecentProjects")
        self.verticalLayout_6.addWidget(self.labelRecentProjects)
        self.listWidgetRecentProjects = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetRecentProjects.setObjectName("listWidgetRecentProjects")
        self.verticalLayout_6.addWidget(self.listWidgetRecentProjects)
        self.treeViewFlowcharts = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewFlowcharts.setObjectName("treeViewFlowcharts")
        self.verticalLayout_6.addWidget(self.treeViewFlowcharts)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelProjectPlots = QtWidgets.QLabel(self.centralwidget)
        self.labelProjectPlots.setObjectName("labelProjectPlots")
        self.verticalLayout_5.addWidget(self.labelProjectPlots)
        self.treeViewProjectPlots = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewProjectPlots.setObjectName("treeViewProjectPlots")
        self.verticalLayout_5.addWidget(self.treeViewProjectPlots)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 30))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProject_Configuration = QtWidgets.QAction(MainWindow)
        self.actionProject_Configuration.setEnabled(False)
        self.actionProject_Configuration.setObjectName("actionProject_Configuration")
        self.actionSystem_Configuration = QtWidgets.QAction(MainWindow)
        self.actionSystem_Configuration.setObjectName("actionSystem_Configuration")
        self.actionShow_all_windows = QtWidgets.QAction(MainWindow)
        self.actionShow_all_windows.setObjectName("actionShow_all_windows")
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setCheckable(True)
        self.actionConsole.setObjectName("actionConsole")
        self.actionViewer_linker = QtWidgets.QAction(MainWindow)
        self.actionViewer_linker.setObjectName("actionViewer_linker")
        self.actionDocs_homepage = QtWidgets.QAction(MainWindow)
        self.actionDocs_homepage.setObjectName("actionDocs_homepage")
        self.actionNew_Project_Docs = QtWidgets.QAction(MainWindow)
        self.actionNew_Project_Docs.setObjectName("actionNew_Project_Docs")
        self.actionSystem_Configuration_Docs = QtWidgets.QAction(MainWindow)
        self.actionSystem_Configuration_Docs.setObjectName("actionSystem_Configuration_Docs")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setText("")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.action_version.setFont(font)
        self.action_version.setObjectName("action_version")
        self.actionReport_issue_bug = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionReport_issue_bug.setFont(font)
        self.actionReport_issue_bug.setObjectName("actionReport_issue_bug")
        self.actionQuestions_discussion = QtWidgets.QAction(MainWindow)
        self.actionQuestions_discussion.setObjectName("actionQuestions_discussion")
        self.menuConfiguration.addAction(self.actionProject_Configuration)
        self.menuConfiguration.addAction(self.actionSystem_Configuration)
        self.menuView.addAction(self.actionShow_all_windows)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionConsole)
        self.menuTools.addAction(self.actionViewer_linker)
        self.menuHelp.addAction(self.actionReport_issue_bug)
        self.menuHelp.addAction(self.actionQuestions_discussion)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDocs_homepage)
        self.menuHelp.addAction(self.actionNew_Project_Docs)
        self.menuHelp.addAction(self.actionSystem_Configuration_Docs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_version)
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Viewer"))
        self.label_5.setText(_translate("MainWindow", "Flowchart"))
        self.labelProjectBrowser.setText(_translate("MainWindow", "Project Browser"))
        self.labelOpenProject.setText(_translate("MainWindow", "Open Project"))
        self.labelNewProj.setText(_translate("MainWindow", "New Project"))
        self.labelRecentProjects.setText(_translate("MainWindow", "Recent projects"))
        self.labelProjectPlots.setText(_translate("MainWindow", "Project plots"))
        self.label.setText(_translate("MainWindow", "Console"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Confi&guration"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuTools.setTitle(_translate("MainWindow", "Too&ls"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionProject_Configuration.setText(_translate("MainWindow", "&Project Configuration"))
        self.actionSystem_Configuration.setText(_translate("MainWindow", "&System Configuration"))
        self.actionShow_all_windows.setText(_translate("MainWindow", "&Show all windows"))
        self.actionConsole.setText(_translate("MainWindow", "&Console"))
        self.actionViewer_linker.setText(_translate("MainWindow", "&Viewer linker"))
        self.actionDocs_homepage.setText(_translate("MainWindow", "&Docs homepage"))
        self.actionNew_Project_Docs.setText(_translate("MainWindow", "&New Project help"))
        self.actionSystem_Configuration_Docs.setText(_translate("MainWindow", "&System Config help"))
        self.actionReport_issue_bug.setText(_translate("MainWindow", "Report issue/bug"))
        self.actionQuestions_discussion.setText(_translate("MainWindow", "Questions/discussion"))

