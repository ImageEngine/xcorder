# =============================================================================
# Module: gui.py
# Contacts: Edward Li (drawdeil@gmail.com)
# =============================================================================
"""___DESC___

"""

# =============================================================================
# IMPORTS
# =============================================================================
import os
import time
from PyQt4 import QtCore, QtGui
from audio import Audio
from video import Video
from exporter import Exporter
from recorder import Recorder

scriptDir = os.path.dirname(os.path.realpath(__file__))

# =============================================================================
# CLASSES
# =============================================================================
class Gui(QtGui.QWidget):

    # =========================================================================
    def __init__(self, parent=None):

        super(Gui, self).__init__(parent)

        self.videoComboBox = QtGui.QComboBox(self)
        self.videoComboBox.currentIndexChanged.connect(self.videoIndexChanged)

        self.audioComboBox = QtGui.QComboBox(self)
        self.audioComboBox.currentIndexChanged.connect(self.audioIndexChanged)

        self.recordPushButton = QtGui.QPushButton(self)
        self.recordPushButton.setCheckable(True)
        self.recordPushButton.clicked.connect(self.recordClicked)

        separator = QtGui.QFrame(self)
        separator.setFrameStyle(QtGui.QFrame.HLine|QtGui.QFrame.Sunken)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.videoComboBox)
        layout.addWidget(self.audioComboBox)
        layout.addWidget(separator)
        layout.addWidget(self.recordPushButton)

        self.setLayout(layout)
        self.resetToDefault()

    # =========================================================================
    def resetToDefault(self):

        self.video = Video()
        self.audio = Audio()

        self.populateVideoComboBox()
        self.populateAudioComboBox()

        self.recordPushButton.setIcon(QtGui.QIcon(os.path.join(scriptDir, 'rec_btn_off.svg')))
        self.recordPushButton.setChecked(False)
        self.recordPushButton.setEnabled(False)

    # =========================================================================
    def populateVideoComboBox(self):

        self.videoComboBox.clear()
        self.videoComboBox.addItem('Select video screen...')

        for screen in self.video.screens:
            comboBoxItem = 'Screen {i}, size {s}'.format(
                    i=self.videoComboBox.count(), s=screen.size)

            self.videoComboBox.addItem(comboBoxItem)

    # =========================================================================
    def populateAudioComboBox(self):

        self.audioComboBox.clear()
        self.audioComboBox.addItem('Select audio device...')

        for device in self.audio.devices:
            comboBoxItem = '{d}'.format(d=device.description)
            self.audioComboBox.addItem(comboBoxItem)

    # =========================================================================
    def videoIndexChanged(self, index):

        if index:
            self.video.screenSet(index - 1)

        self.checkEnableRecord()

    # =========================================================================
    def audioIndexChanged(self, index):

        if index:
            self.audio.deviceSet(index - 1)

        self.checkEnableRecord()

    # =========================================================================
    def recordClicked(self):

        if self.recordPushButton.isChecked():
            self.videoComboBox.setEnabled(False)
            self.audioComboBox.setEnabled(False)
            self.recordPushButton.setIcon(QtGui.QIcon(os.path.join(scriptDir, 'rec_btn_on.svg')))

            self.startRecorder()
        else:
            self.videoComboBox.setEnabled(True)
            self.audioComboBox.setEnabled(True)
            self.recordPushButton.setIcon(QtGui.QIcon(os.path.join(scriptDir, 'rec_btn_off.svg')))

            self.stopRecorder()

    # =========================================================================
    def checkEnableRecord(self):

        if self.videoComboBox.currentIndex() and \
                self.audioComboBox.currentIndex():

            self.recordPushButton.setEnabled(True)
        else:
            self.recordPushButton.setEnabled(False)

    # =========================================================================
    def startRecorder(self):

        strftime = time.strftime('%Y%m%d%H%M%S')
        self.workdir = '/tmp/xcorder/{s}/'.format(s=strftime)

        if not os.path.isdir(self.workdir):
            os.makedirs(self.workdir)

        self.recorder = Recorder(
                self.video.screen, self.audio.device, self.workdir)

        self.recorder.start()

    # =========================================================================
    def stopRecorder(self):

        self.recorder.stop()
        filename = QtGui.QFileDialog.getSaveFileName(
                None, 'Save As:', '', '*.mov ;; *.*')

        if filename:
            if not str(filename).lower().endswith('.mov'):
                filename += '.mov'

            self.exporter = Exporter(self.workdir, filename)
            self.exporter.start()

            print('\nFile saved {f}\n'.format(f=filename))

    # =========================================================================
    def infoDialog(self, message):

        messageBox = QtGui.QMessageBox( QtGui.QMessageBox.Information,
                'Message', message, QtGui.QMessageBox.Ok, parent=self)

        messageBox.show()

# =============================================================================

