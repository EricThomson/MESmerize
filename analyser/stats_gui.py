#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 7 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
import sys
# sys.path.append('..')
from pyqtgraphCore.Qt import QtCore, QtGui, QtWidgets
from pyqtgraphCore.console import ConsoleWidget
from pyqtgraphCore import ColorButton
from pyqtgraphCore import PlotItem, PlotDataItem, PlotCurveItem
from pyqtgraphCore.widgets.MatplotlibWidget import MatplotlibWidget
if __name__ == '__main__':
    from stats_gui_pytemplate import *
    import DataTypes
    from HistoryWidget import HistoryTreeWidget
    from stats_plots import *
    from stim_plots_pytemplate import *
    from stats_peak_plots_pytemplate import *
else:
    from .stats_gui_pytemplate import *
    from . import DataTypes
    from .HistoryWidget import HistoryTreeWidget
    from .stats_plots import *
    from .stim_plots_pytemplate import *
    from .stats_peak_plots_pytemplate import *
import sys
import numpy as np
import scipy as scipy
import pandas as pd
from functools import partial
import pickle


class StatsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(StatsWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Mesmerize - Stats & Plots')
        self.actionSave_Statistics_DataFrame.triggered.connect(self._save_stats_transmission)
        self.actionOpen_Statistics_DataFrame.triggered.connect(self._open_stats_transmission)
        self.actionSave_Group_Transmissions.triggered.connect(self._save_groups)
        self.actionLoad_Groups.triggered.connect(self._open_groups)
        self.actionSave_Incoming_Transmissions.triggered.connect(self._save_raw_trans)
        self._dock_titles = ['Transmissions w/history', 'Peak Plot Controls',
                             'Stim Plot Controls', 'Violin Plot Controls', 'Box Plot Controls',
                             'Parallel Coor Plot Controls']
        self._init_plot_interface()

        ns = {'np': np,
              'pickle': pickle,
              'scipy': scipy,
              'pd': pd,
              'DataTypes': DataTypes,
              'main': self,
              'curr_tab': self.tabWidget.currentWidget
              }

        txt = "Namespaces:\n" \
              "pickle as pickle\n" \
              "numpy as 'np'\n" \
              "scipy as 'scipy'\n" \
              "pyplot as 'pyplot\n" \
              "dt as 'DataTypes'\n" \
              "self as 'main'\n\n" \
              "To access plots in current tab call curr_tab()\n" \
              "Example:\n" \
              "tab0 = curr_tab()\ntab0.p1.plot(x, np.sin(x))"

        self.dockConsole.setWidget(ConsoleWidget(namespace=ns, text=txt,
                                                 historyFile='./test_history.pik'))

        self.dockConsole.hide()

    """#########################################################################################
                                    Input Transmissions stuff
    ############################################################################################"""

    # Call by Peak_Features node in flowchart, constructs StatsTransmission from normal Transmissions
    def input_transmissions(self, transmissions_list):
        self.listwGroups.hide()
        if hasattr(self, 'lineEdGroupList'):
            if not QtGui.QMessageBox.question(self, 'Discard current data?',
                                              'You have data open in this window, would you '
                                              'like to discard them and load the new data?') == QtGui.QMessageBox.Yes:
                return

        self.transmissions_list = transmissions_list

        srcs_list = []
        for transmission in self.transmissions_list:
            srcs_list.append(transmission.src)

        self._set_history_widget(srcs_list)
        self._setup_group_entries(len(transmissions_list))

    def _save_raw_trans(self):
        if not hasattr(self, 'transmissions_list'):
            QtGui.QMessageBox.warning(self, 'Nothing to save', 'There are no raw transmissions to save')

        for i in range(len(self.transmissions_list)):
            path = QtGui.QFileDialog.getSaveFileName(None, 'Save Transmission ' + str(i), '', '(*.trn)')
            if path == '':
                return
            if path[0].endswith('.trn'):
                path = path[0]
            else:
                path = path[0] + '.trn'

            try:
                self.transmissions_list[i].to_pickle(path)
            except Exception as e:
                QtGui.QMessageBox.warning(self, 'File save Error', 'Unable to save the file\n' + str(e))

    def _set_history_widget(self, srcs):
        if len(self.stack_page_transmission_history.children()) > 0:
            for item in self.stack_page_transmission_history.children():
                if isinstance(item, HistoryTreeWidget):
                    item.fill_widget(srcs)
        else:
            layout = QtWidgets.QVBoxLayout(self.stack_page_transmission_history)
            history_widget = HistoryTreeWidget()
            layout.addWidget(history_widget)
            history_widget.fill_widget(srcs)
            history_widget.show()

        self.stackedWidget.setCurrentIndex(0)
        self.dockWidget.setWindowTitle(self._dock_titles[0])

    def _setup_group_entries(self, n):
        xpos = 10
        ypos = 10

        self.btnAutoList = []
        self.labelTransmissionList = []
        self.lineEdGroupList = []

        for i in range(0, n):
            btnAuto = QtWidgets.QPushButton(self.tabWidget.widget(0))
            btnAuto.setGeometry(xpos, ypos, 50, 26)
            btnAuto.setText('Auto')

            self.btnAutoList.append(btnAuto)
            btnAuto.clicked.connect(partial(self._auto_slot, i))

            labelTransmission = QtWidgets.QLabel(self.tabWidget.widget(0))
            labelTransmission.setGeometry(xpos + 60, ypos, 150, 26)
            labelTransmission.setText('Transmission ' + str(i) + ' :')

            self.labelTransmissionList.append(labelTransmission)

            lineEdGroup = QtWidgets.QLineEdit(self.tabWidget.widget(0))
            lineEdGroup.setGeometry(xpos + 65 + 100, ypos, 520, 26)
            lineEdGroup.setPlaceholderText('Group Names separated by commas ( , )')

            self.lineEdGroupList.append(lineEdGroup)

            ypos += 35

        btnSetGroups = QtWidgets.QPushButton(self.tabWidget.widget(0))
        btnSetGroups.setGeometry(xpos, ypos + 10, 75, 26)
        btnSetGroups.setText('Set Groups')
        btnSetGroups.clicked.connect(self._set_groups)
        btnSetGroups.clicked.connect(self._del_group_entries)
        btnSetGroups.clicked.connect(btnSetGroups.deleteLater)

    def _set_groups(self):
        i = 0
        self.gts = []
        for entry in self.lineEdGroupList:
            if entry.text() == '':
                if QtGui.QMessageBox.question(self, 'Empty entry', 'The entry for Transmission ' + str(i) + ' is empty '
                                            'would you like to skip this transmission and not annotate groups to it?',
                                              QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
                    return
            group_list = [e.strip() for e in entry.text().split(',')]
            gt = DataTypes.GroupTransmission.from_ca_data(self.transmissions_list[i], group_list)
            self.gts.append(gt)
            i += 1

        self.listwGroups.show()
        self.StatsData = DataTypes.StatsTransmission.from_group_trans(self.gts)
        self.listwGroups.addItems(self.StatsData.all_groups)
        self.set_data()

    def _del_group_entries(self):
        for item in self.btnAutoList:
            item.deleteLater()
        for item in self.labelTransmissionList:
            item.deleteLater()
        for item in self.lineEdGroupList:
            item.deleteLater()

    def set_data(self):
        if not hasattr(self, 'StatsData') and not hasattr(self, 'gts'):
            return
        self.listwGroups.clear()
        self.listwGroups.addItems(self.StatsData.all_groups)
        self.plot_all()

    def plot_all(self):
        group_colors = {}
        c = ['b', 'g', 'r', 'c', 'm', 'y']
        i = 0
        for group in self.StatsData.all_groups:
            group_colors.update({group: c[i%6]})
            i +=1

        self.plots_interface.set_data(df=self.StatsData.df, group_dict=group_colors)
        self.plots_interface.plot()

    def _init_plot_interface(self):
        self.plots_interface = PlotInterface(self)


    def _auto_slot(self, i):
        QtGui.QMessageBox.information(self, 'Error', 'Not implemented')
        pass

    def _set_stack_index(self, i):
        self.dockWidget.setWindowTitle(self._dock_titles[i])

    def _set_matplotlib_controls(self):
        xpos = 10
        ypos = 10
        labelGroupList = []
        btnColorList = []

        parent = self.stack_page_matplotlib

        for group in self.StatsData.all_groups:
            labelGroup = QtWidgets.QLabel(parent)
            labelGroup.setGeometry(xpos, ypos, 100, 26)
            labelGroup.setText(group)

            labelGroupList.append(labelGroup)

            btnColor = ColorButton(parent)
            btnColor.setGeometry(xpos + 120, ypos, 50, 26)

            btnColorList.append(btnColor)

            ypos += 35

    """#########################################################################################
                                    Saving & Loading files
    ############################################################################################"""

    def _save_stats_transmission(self):
        path = QtGui.QFileDialog.getSaveFileName(None, 'Save Stats Transmission as', '', '(*.strn)')
        if path == '':
            return

        if path[0].endswith('.strn'):
            path = path[0]
        else:
            path = path[0] + '.strn'

        try:
            self.StatsData.to_pickle(path)
        except Exception as e:
            QtGui.QMessageBox.warning(self, 'File save Error', 'Unable to save the file\n' + str(e))

    def _open_stats_transmission(self):
        if hasattr(self, 'StatsData'):
            if not QtGui.QMessageBox.question(self, 'Discard current data?',
                                              'You have data open in this window, would you '
                                              'like to discard them and load the new data?') == QtGui.QMessageBox.Yes:
                return

        path = QtGui.QFileDialog.getOpenFileName(None, 'Import Statistics object', '', '(*.strn)')
        if path == '':
            return
        try:
            self.StatsData = DataTypes.StatsTransmission.from_pickle(path[0])
        except Exception as e:
            QtGui.QMessageBox.warning(None, 'File open Error!', 'Could not open the chosen file.\n' + str(e))
            return

        self.set_data()

    def _open_groups(self):
        groups = []
        paths = QtGui.QFileDialog.getOpenFileNames(None, 'Import Group object', '', '(*.gtrn)')
        print(paths)
        if paths == '':
            return
        if paths[0] == []:
            return
        try:
            for path in paths[0]:
                groups.append(DataTypes.GroupTransmission.from_pickle(path))
        except Exception as e:
            QtGui.QMessageBox.warning(None, 'File open Error!', 'Could not open the chosen file.\n' + str(e))
            return

        if hasattr(self, 'StatsData'):
            l = [self.StatsData] + groups
            self.StatsData = DataTypes.StatsTransmission.merge([l])
        else:
            self.StatsData = DataTypes.StatsTransmission.from_group_trans(groups)
            self.gts += groups

    def _save_groups(self):
        if not hasattr(self, 'gts'):
            QtGui.QMessageBox.warning(self, 'Save Error', 'No open Groups to save!')
            return

        for i in range(len(self.gts)):
            path = QtGui.QFileDialog.getSaveFileName(None, 'Save Group Transmission ' + str(i), '', '(*.gtrn)')
            if path == '':
                return
            if path[0].endswith('.gtrn'):
                path = path[0]
            else:
                path = path[0] + '.gtrn'

            try:
                self.gts[i].to_pickle(path)
            except Exception as e:
                QtGui.QMessageBox.warning(self, 'File save Error', 'Unable to save the file\n' + str(e))



class MPLW(MatplotlibWidget):
    def __init__(self):
        MatplotlibWidget.__init__(self)

class Plots:
    def __init__(self, curve_plot, violin_plot):
        self.curve_plot = curve_plot
        self.violin_plot = violin_plot

    def setData(self, groups):
        print(groups)
        colors = ['b', 'g', 'r', 'c', 'm', 'y']
        ci = 0
        ax = self.curve_plot.fig.add_subplot(111)

        for group in groups:
            c = colors[ci]
            for ix, r in group.df.iterrows():
                if (r['peak_curve'] is not None) and (len(r['peak_curve']) > 0):
                    ax.plot(r['peak_curve']/min(r['peak_curve']), color=c)
            ci +=1

        self.curve_plot.canvas.draw()
        # self.violin_plot.draw()

    def setColor(self):
        pass

    def addGroup(self):
        pass

    def removeGroup(self):
        pass


class PlotInterface:
    def __init__(self, parent):
        assert isinstance(parent, StatsWindow)
        self.stims = StimPlots()
        parent.stim_plots_tab.layout().addWidget(self.stims)
        self.peaks = PeakPlots()
        parent.peak_plot_tab.layout().addWidget(self.peaks)

        self.plots = [self.stims, self.peaks]

    def set_data(self, df, group_dict):
        self.stims.set_data(df, group_dict)
        self.peaks.set_data(df, group_dict)

    def set_colors(self):
        pass

    def plot(self):
        self.stims.plot_all()
        self.peaks.plot_all()


class PeakPlots(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_stats_peak_plots_template()
        self.ui.__init__()
        self.ui.setupUi(self)
        self.gplots = []

    def set_data(self, df, groups_dict):
        self.df = df
        self.groups_dict = groups_dict

    def plot_all(self):
        self.plot_overlaps()
        self.plot_group_subplots()

    def plot_overlaps(self):
        self.ui.curve_plot_all_group_peaks.clear()
        self.ymax = 0.0
        for key in self.groups_dict.keys():
            for ix, r in self.df.loc[self.df[key] == True].iterrows():
                a = r['peak_curve']
                if a.size == 0:
                    continue
                ma = np.max(a)
                self.ymax = np.maximum(ma, self.ymax)

                if not hasattr(self, 'ymin'):
                    self.ymin = self.ymax

                mi = np.min(a)
                self.ymin = np.minimum(mi, self.ymin)

                xs = np.linspace(0 - (a.size / 2), a.size / 2, num=a.size)
                self.ui.curve_plot_all_group_peaks.plot(x=xs, y=a, pen=self.groups_dict[key])



    def plot_group_subplots(self):
        for item in self.gplots:
            self.ui.curve_plot_group_peaks.removeItem(item)
        self.ui.curve_plot_group_peaks.clear()
        self.gplots = []

        for key in self.groups_dict.keys():
            self.gplots.append(self.ui.curve_plot_group_peaks.addPlot(title=key))
            for ix, r in self.df.loc[self.df[key] == True].iterrows():
                # try:
                a = r['peak_curve']
                xs = np.linspace(0 - (a.size / 2), a.size / 2, num=a.size)

                self.gplots[-1].plot(x=xs, y=a, pen=self.groups_dict[key])

                # except:
                #     pass

            self.gplots[-1].setYRange(self.ymin, self.ymax)


    def plot_headmaps(self):
        pass


class StimPlots(QtWidgets.QWidget):#, Ui_stim_plots_template):
    def __init__(self): #, flags, parent=None, *args, **kwargs):
        #super().__init__()#flags, parent, *args, **kwargs)
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_stim_plots_template()
        self.ui.__init__()
        self.ui.setupUi(self)
        self.gplots = []

    def set_data(self, df, groups_dict):
        self.df = df
        self.groups_dict = groups_dict

    def plot_all(self):
        self.plot_overlaps()
        self.plot_group_subplots()
        self.plot_heatmaps()

    def plot_overlaps(self, update_subplots=True):
        self.ui.stim_plots_overlays.clear()
        self.ymax = 0.0
        for key in self.groups_dict.keys():
            for ix, r in self.df.loc[self.df[key] == True].iterrows():
                a = r['raw_curve']
                ma = np.max(a)
                self.ymax = np.maximum(ma, self.ymax)

                if not hasattr(self, 'ymin'):
                    self.ymin = self.ymax

                mi = np.min(a)
                self.ymin = np.minimum(mi, self.ymin)

                self.ui.stim_plots_overlays.plot(a, pen=self.groups_dict[key])


    def plot_group_subplots(self):
        for item in self.gplots:
            self.ui.stim_plots_groups.removeItem(item)

        self.ui.stim_plots_groups.clear()
        self.gplots = []

        for key in self.groups_dict.keys():
            self.gplots.append(self.ui.stim_plots_groups.addPlot(title=key))

            for ix, r in self.df.loc[self.df[key] == True].iterrows():
                self.gplots[-1].plot(r['raw_curve'], pen=self.groups_dict[key])

            self.gplots[-1].setYRange(self.ymin, self.ymax)

    def plot_heatmaps(self):
        pass


class ViolinPlots():
    pass


class BoxPlots():
    pass


class ParaCorPlots():
    pass

if __name__ == '__main__':
    t1 = DataTypes.Transmission.from_pickle('/home/kushal/Sars_stuff/github-repos/MESmerize/test_raw_trans_stats_plots_gui/t1.trn')
    t2 = DataTypes.Transmission.from_pickle('/home/kushal/Sars_stuff/github-repos/MESmerize/test_raw_trans_stats_plots_gui/t2.trn')
    t3 = DataTypes.Transmission.from_pickle('/home/kushal/Sars_stuff/github-repos/MESmerize/test_raw_trans_stats_plots_gui/t3.trn')
    
    app = QtWidgets.QApplication([])
    sw = StatsWindow()
    sw.input_transmissions([t1, t2, t3])
    sw.lineEdGroupList[0].setText('A')
    sw.lineEdGroupList[1].setText('B')
    sw.lineEdGroupList[2].setText('C')
    sw.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()