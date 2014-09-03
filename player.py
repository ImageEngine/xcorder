# =============================================================================
# Module: player.py
# Contacts: Edward Li (drawdeil@gmail.com)
# =============================================================================
"""___DESC___

"""

# =============================================================================
# IMPORTS
# =============================================================================
import subprocess

# =============================================================================
# CLASSES
# =============================================================================
class Player(object):

    # =========================================================================
    def __init__(self, filePath=None):

        self._filePath = filePath
        self._proc = None

    # =========================================================================
    def start(self):

        print(self.args)

    # =========================================================================
    def stop(self):

        print('stopped')

    '''
    # =========================================================================
    def startstop(self, signal=None):

        if signal == 'start' and not self.cmdProc:
            self.cmdProc = subprocess.Popen(self.playCmd, shell=True,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)

        elif signal == 'stop' and self.cmdProc:
            self.cmdProc.communicate(input='q')
            self.cmdProc = None

        else:
            return
    '''

    # =========================================================================
    @property
    def args(self):

        return 'ffplay {option}'.format(option=self._filePath)

# =============================================================================

