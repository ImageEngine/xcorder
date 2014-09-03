# =============================================================================
# Module: exporter.py
# Contacts: Edward Li (drawdeil@gmail.com)
# =============================================================================
"""___DESC___

"""

# =============================================================================
# IMPORTS
# =============================================================================
import glob
import subprocess

# =============================================================================
# CLASSES
# =============================================================================
class Exporter(object):

    # =========================================================================
    def __init__(self, workDir=None, exportFile=None):

        self._workDir = workDir
        self._exportFile = exportFile
        self._proc = None

    # =========================================================================
    def start(self):

        self.makeFileList()
        if not self._proc:
            self._proc = subprocess.Popen(self.args, shell=True,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
            self._proc.communicate()
        else:
            print('Error: An exporting process is already running.')

    # =========================================================================
    def stop(self):

        if self._proc:
            self._proc.communicate(input='q')
            self._proc = None
        else:
            print('Error: There is no existing recording process to stop.')

    # =========================================================================
    def makeFileList(self):

        segmentFiles = glob.glob('{d}recording.*.mov'.format(d=self._workDir))
        segmentFiles.sort()

        with open(self.fileList, 'w') as fileList:
            for segmentFile in segmentFiles:
                fileList.write("file '{f}'\n".format(f=segmentFile))

    # =========================================================================
    @property
    def args(self):

        return 'ffmpeg {option}'.format(option=self.optionArgs)

    # =========================================================================
    @property
    def optionArgs(self):

        return '-f concat ' + \
               '-i {i} '.format(i=self.fileList) + \
               '-codec copy ' + \
               '-y ' + \
               self._exportFile

    # =========================================================================
    @property
    def fileList(self):

        return '{d}recording.list'.format(d=self._workDir)

# =============================================================================

