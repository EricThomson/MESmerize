#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 13 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ..core.common import ViewerInterface
from pyqtgraphCore.Qt import QtCore, QtGui, QtWidgets
from .pytemplates.caiman_motion_correction_pytemplate import *
import json
import numpy as np
from .batch_manager import ModuleGUI as BatchModuleGui
from common import configuration
from ..core.viewer_work_environment import ViewerWorkEnv
import caiman as cm
from pyqtgraphCore import LinearRegionItem


class ModuleGUI(QtWidgets.QDockWidget):
    def __init__(self, parent, viewer_reference):
        self.vi = ViewerInterface(viewer_reference)

        QtWidgets.QDockWidget.__init__(self, parent)
        if configuration.window_manager.batch_manager is None:
            QtWidgets.QMessageBox.question(self, 'No batch manager open',
                                           'The batch manager has not been initialized, '
                                           'you must choose a location for a new batch or create a new batch',
                                           QtWidgets.QMessageBox.Ok)
            configuration.window_manager.initialize_batch_manager()

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self.ui.btnAddToBatchRigid.clicked.connect(self.add_rig_corr_to_batch)
        self.ui.btnAddToBatchElastic.clicked.connect(self.add_elas_corr_to_batch)

        self.ui.btnShowQuilt.clicked.connect(self.draw_quilt)

        self.ui.sliderOverlaps.valueChanged.connect(self.draw_quilt)
        self.ui.sliderStrides.valueChanged.connect(self.draw_quilt)

        self.overlapsH = []
        self.overlapsV = []

    def draw_quilt(self):
        if self.ui.btnShowQuilt.isChecked() is False:
            self.remove_quilt()
            return
        if len(self.overlapsV) > 0:
            for overlap in self.overlapsV:
                self.vi.viewer.view.removeItem(overlap)
            for overlap in self.overlapsH:
                self.vi.viewer.view.removeItem(overlap)
            self.overlapsV = []
            self.overlapsH = []

        w = int(self.vi.viewer.view.addedItems[0].width())
        k = self.ui.sliderStrides.value()


        h = int(self.vi.viewer.view.addedItems[0].height())
        j = self.ui.sliderStrides.value()

        val = int(self.ui.sliderOverlaps.value())

        for i in range(1, int(w/k) + 1):
            linreg = LinearRegionItem(values=[i*k, i*k + val], brush=(255,255,255,80),
                                      movable=False, bounds=[i*k, i*k + val])
            self.overlapsV.append(linreg)
            self.vi.viewer.view.addItem(linreg)

        for i in range(1, int(h/j) + 1):
            linreg = LinearRegionItem(values=[i*j, i*j + val], brush=(255, 255, 255, 80),
                                      movable=False, bounds=[i*j, i*j + val],
                                      orientation=LinearRegionItem.Horizontal)
            self.overlapsH.append(linreg)
            self.vi.viewer.view.addItem(linreg)

    def remove_quilt(self):
        for o in self.overlapsV:
            self.vi.viewer.view.removeItem(o)
        for o in self.overlapsH:
            self.vi.viewer.view.removeItem(o)
        self.overlapsH = []
        self.overlapsV = []

    def _make_params_dict(self):
        d = {'max_shifts_x':    self.ui.spinboxX.value(),
             'max_shifts_y':    self.ui.spinboxY.value(),
             'iters_rigid':     self.ui.spinboxIterRigid.value(),
             'name_rigid':      self.ui.lineEditNameRigid.text(),
             'max_dev':         self.ui.spinboxMaxDev.value(),
             'strides':         self.ui.sliderStrides.value(),
             'overlaps':        self.ui.sliderOverlaps.value(),
             'upsample':        self.ui.spinboxUpsample.value(),
             'name_elas':       self.ui.lineEditNameElastic.text()
             }
        return d

    def add_rig_corr_to_batch(self):
        pass

    def add_elas_corr_to_batch(self):
        d = self._make_params_dict()

        self.vi.viewer.batch_manager.add_item(module='caiman_motion_correction',
                                               name=self.ui.lineEditNameElastic.text(),
                                               input_workEnv=self.vi.viewer.workEnv,
                                               input_params=d,
                                               info=d)

        self.ui.lineEditNameElastic.clear()
