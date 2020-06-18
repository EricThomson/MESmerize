#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 23 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ..core.common import ViewerUtils
from .pytemplates.cnmf_pytemplate import *
from ...common import get_window_manager
from ...common.qdialogs import *


class ModuleGUI(QtWidgets.QDockWidget):
    def __init__(self, parent, viewer_reference):
        self.vi = ViewerUtils(viewer_reference)

        QtWidgets.QDockWidget.__init__(self, parent)

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self.ui.btnAddToBatchCNMF.clicked.connect(self.add_to_batch_cnmf)

    @present_exceptions()
    def get_params(self, *args, group_params: bool = False) -> dict:
        """
        Get a dict of the set parameters.
        If the work environment was loaded from a motion correction batch item it put the bord_px in the dict.
        Doesn't use any arguments

        :return: parameters dict
        :rtype: dict
        """
        if self.vi.viewer.workEnv.imgdata.meta['fps'] == 0:
            raise KeyError('No framerate for current image sequence!',
                           'You must set a framerate for the current image sequence. '
                           'You can set it manually in the console like this:\nget_meta()["fps"] = <framerate>')

        # Get width of border that is NaN, usually happens due ot motion correction
        history_trace = self.vi.viewer.workEnv.history_trace
        try:
            bord_px = next(d for ix, d in enumerate(history_trace) if 'caiman_motion_correction' in d)['caiman_motion_correction']['bord_px']
        except StopIteration:
            bord_px = 0

        # CNMF kwargs
        cnmf_kwargs = \
            {
                'p': self.ui.spinBoxP.value(),
                'gnb': self.ui.spinBoxGnb.value(),
                'merge_thresh': self.ui.doubleSpinBoxMergeThresh.value(),
                'rf': self.ui.spinBoxRf.value(),
                'stride': self.ui.spinBoxStrideCNMF.value(),
                'k': self.ui.spinBoxK.value(),
                'gSig': [
                            self.ui.spinBox_gSig_x.value(),
                            self.ui.spinBox_gSig_y.value()
                        ],
                'ssub': self.ui.spinBox_ssub.value(),
                'tsub': self.ui.spinBox_tsub.value(),
                'method_init': self.ui.comboBox_method_init.currentText(),
                'border_pix': bord_px,
            }

        # Any additional cnmf kwargs set in the text entry
        if self.ui.groupBox_cnmf_kwargs.isChecked():
            try:
                _kwargs = self.ui.plainTextEdit_cnmf_kwargs.toPlainText()
                cnmf_kwargs_add = eval(f"dict({_kwargs})")
                cnmf_kwargs.update(cnmf_kwargs_add)
            except:
                raise ValueError("CNMF kwargs not formatted properly.")

        # Component evaluation kwargs
        eval_kwargs = \
            {
                'min_SNR': self.ui.doubleSpinBoxMinSNR.value(),
                'rval_thr': self.ui.doubleSpinBoxRvalThr.value(),
                'min_cnn_thr': self.ui.doubleSpinBoxCNNThr.value(),
                'cnn_lowest': self.ui.doubleSpinBox_cnn_lowest.value(),
                'decay_time': self.ui.spinBoxDecayTime.value(),
                'name_cnmf': self.ui.lineEdName.text(),
                'refit': self.ui.checkBoxRefit.isChecked(),
                'fr': self.vi.viewer.workEnv.imgdata.meta['fps']
            }

        # Any additional eval kwargs set in the text entry
        if self.ui.groupBox_eval_kwargs.isChecked():
            try:
                _kwargs = self.ui.plainTextEdit_eval_kwargs.toPlainText()
                eval_kwargs_add = eval(f"dict{_kwargs}")
                eval_kwargs.update(eval_kwargs_add)
            except:
                raise ValueError("Evaluation kwargs not formatted properly.")

        # Make the output dict
        d = \
            {
                'item_name': self.ui.lineEdName.text(),
                'refit': self.ui.checkBoxRefit.isChecked(),
                'border_pix': bord_px
            }

        # Group the kwargs of the two parts seperately
        if group_params:
            d.update(
                {
                    'cnmf_kwargs': cnmf_kwargs,
                    'eval_kwargs': eval_kwargs
                }
            )

        # or not
        else:
            d.update(
                {
                    **cnmf_kwargs,
                    **eval_kwargs
                }
            )

        return d

    def set_params(self, d: dict):
        """
        Set all parameters from a dict. All keys must be present in the dict.

        :param d: parameters dict
        """
        if ('cnmf_kwargs' in d.keys()) and ('eval_kwargs' in d.keys()):
            p = {**d['cnmf_kwargs'], **d['eval_kwargs']}
        else:
            p = d

        self.ui.spinBoxP.setValue(p['p'])
        self.ui.spinBoxGnb.setValue(p['gnb'])
        self.ui.doubleSpinBoxMergeThresh.setValue(p['merge_thresh'])
        self.ui.spinBoxRf.setValue(p['rf'])
        self.ui.spinBoxStrideCNMF.setValue(p['stride_cnmf'])
        self.ui.spinBoxK.setValue(p['k'])

        self.ui.spinBox_gSig_x.setValue(p['gSig'][0])
        self.ui.spinBox_gSig_x.setValue(p['gSig'][1])

        self.ui.spinBox_ssub.setValue([p['ssub']])
        self.ui.spinBox_tsub.setValue([p['tsub']])

        ix = self.ui.comboBox_method_init.findText(p['method_init'])
        if ix == -1:
            raise ValueError('Invalid method_init param')
        self.ui.comboBox_method_init.setCurrentIndex(ix)

        self.ui.doubleSpinBoxMinSNR.setValue(p['min_SNR'])
        self.ui.doubleSpinBoxRvalThr.setValue(p['rval_thr'])
        self.ui.doubleSpinBoxCNNThr.setValue(p['cnn_thr'])
        self.ui.doubleSpinBox_cnn_lowest.setValue(p['cnn_lowest'])
        self.ui.spinBoxDecayTime.setValue(p['decay_time'])
        self.ui.lineEdName.setText(p['item_name'])
        self.ui.checkBoxRefit.setChecked(p['refit'])

    def add_to_batch_cnmf(self):
        """
        Add a CNMF batch item with the currently set parameters and the current work environment.
        """
        if self.vi.viewer.workEnv.isEmpty:
            QtWidgets.QMessageBox.warning(self, 'Empty work environment', 'The work environment is empty, '
                                                                          'nothing to add to batch')
            return

        input_workEnv = self.vi.viewer.workEnv

        d = self.get_params(group_params=True)

        name = d['item_name']
        self.vi.viewer.status_bar_label.showMessage('Please wait, adding CNMF: ' + name + ' to batch...')

        batch_manager = get_window_manager().get_batch_manager()
        u = batch_manager.add_item(
            module='CNMF',
            name=name,
            input_workEnv=input_workEnv,
            input_params=d,
            info=self.get_params()
        )

        if u is None:
            self.vi.viewer.status_bar_label.clearMessage()
            return

        self.vi.viewer.status_bar_label.showMessage('Done adding CNMF: ' + name + ' to batch!')
        self.ui.lineEdName.clear()
