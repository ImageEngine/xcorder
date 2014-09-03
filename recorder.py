# =============================================================================
# Module: recorder.py
# Contacts: Edward Li (drawdeil@gmail.com)
# =============================================================================
"""___DESC___

"""

# =============================================================================
# IMPORTS
# =============================================================================
import os
import subprocess
import tempfile

# =============================================================================
# CLASSES
# =============================================================================
class Recorder(object):

    # =========================================================================
    def __init__(self, videoScreen=None, audioDevice=None, workDir=None):

        self._videoScreen = videoScreen
        self._audioDevice = audioDevice
        self._workDir = workDir
        self._proc = None

    # =========================================================================
    def start(self):

        print(self.args)
        if not self._proc:
            outputFile = tempfile.NamedTemporaryFile()
            self._proc = subprocess.Popen(self.args, shell=True,
                    stdin=subprocess.PIPE, stdout=outputFile,
                    stderr=subprocess.STDOUT, bufsize=1, close_fds=True)
            print('\nRecording started...\n')
        else:
            print('Error: A recording process is already running.')

    # =========================================================================
    def stop(self):

        if self._proc:
            self._proc.communicate(input='q')
            self._proc = None
            print('\nRecording stopped.\n')
        else:
            print('Error: There is no existing recording process to stop.')

   # =========================================================================
    @property
    def args(self):

        return 'ffmpeg {video}{audio}{output}'.format(
               video=self.videoArgs,
               audio=self.audioArgs,
               output=self.outputArgs)

   # =========================================================================
    @property
    def videoArgs(self):

        return '-f x11grab ' + \
               '-s {s} '.format(s=self._videoScreen.size) + \
               '-r 24 ' + \
               '-i {i} '.format(i=self._videoScreen.source)

    # =========================================================================
    @property
    def audioArgs(self):

        return '-f {f} '.format(f=self._audioDevice.api) + \
               '-ac 1 ' + \
               '-ar 48000 ' + \
               '-i {i} '.format(i=self._audioDevice.source)

    # =========================================================================
    @property
    def outputArgs(self):

        return '-map 0:0 ' + \
               '-map 1:0 ' + \
               '-vcodec mpeg4 ' + \
               '-qscale:v 1 ' + \
               '-acodec pcm_s16be ' + \
               '-qscale:a 1 ' + \
               '-f segment ' + \
               '-segment_time 300 ' + \
               '{d}recording.%04d.mov '.format(d=self._workDir)

# =============================================================================

