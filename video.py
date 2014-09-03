# =============================================================================
# Module: video.py
# Contacts: Edward Li (drawdeil@gmail.com)
# =============================================================================
"""___DESC___

"""

# =============================================================================
# IMPORTS
# =============================================================================
import os
from PyQt4 import QtGui

# =============================================================================
# CLASSES
# =============================================================================
class Video(object):

    # =========================================================================
    def __init__(self):

        self._screens = list()
        self._screen = Screen()

        desktop = QtGui.QApplication.desktop()

        for screenIndex in range(desktop.screenCount()):
            geometry = desktop.screenGeometry(screenIndex)
            screen = Screen(geometry)

            if screen not in self._screens:
                self._screens.append(screen)

    # =========================================================================
    def screenSet(self, index):

        self._screen = self.screens[index]

    # =========================================================================
    @property
    def screens(self):

        return self._screens

    # =========================================================================
    @property
    def screen(self):

        return self._screen

# =============================================================================
class Screen(object):

    # =========================================================================
    def __init__(self, geometry=None):

        self._geometry = geometry

    # =========================================================================
    @property
    def source(self):

        return '{d}+{p}'.format(d=os.environ.get('DISPLAY'), p=self.position)

    # =========================================================================
    @property
    def position(self):

        return '{x},{y}'.format(x=self.x, y=self.y)

    # =========================================================================
    @property
    def size(self):

        return '{w}x{h}'.format(w=self.width, h=self.height)

    # =========================================================================
    @property
    def x(self):

        return self._geometry.x()

    # =========================================================================
    @property
    def y(self):

        return self._geometry.y()

    # =========================================================================
    @property
    def width(self):

        return self._geometry.width()

    # =========================================================================
    @property
    def height(self):

        return self._geometry.height()

# =============================================================================

