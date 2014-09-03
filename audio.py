# =============================================================================
# Module: audio.py
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
class Audio(object):

    # =========================================================================
    def __init__(self):

        self._devices = list()
        self._device = Device()

        args = 'pacmd list-sources'
        popen = subprocess.Popen(args, shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        device = Device()
        for line in popen.stdout:
            line = line.strip()

            if line.startswith('name: '):
                device.name = line.split(':', 1)[1].strip()

            elif line.startswith('device.api = '):
                device.api = line.split('=', 1)[1].strip().strip('"')

            elif line.startswith('alsa.subdevice = '):
                device.subdevice = line.split('=', 1)[1].strip().strip('"')

            elif line.startswith('alsa.card = '):
                device.card = line.split('=', 1)[1].strip().strip('"')

            elif line.startswith('device.description = '):
                device.description = line.split('=', 1)[1].strip().strip('"')

                if device.name.startswith('<alsa_input.') and \
                        device.api and device.subdevice and device.card and \
                        device.description:

                    if device not in self._devices:
                        self._devices.append(device)

                device = Device()

    # =========================================================================
    def deviceSet(self, index):

        self._device = self.devices[index]

    # =========================================================================
    @property
    def devices(self):

        return self._devices

    # =========================================================================
    @property
    def device(self):

        return self._device

# =============================================================================
class Device(object):

    # =========================================================================
    def __init__(self, name=None, api=None, subdevice=None, card=None,
            description=None):

        self._name = name
        self._api = api
        self._subdevice = subdevice
        self._card = card
        self._description = description

    # =========================================================================
    @property
    def source(self):

        return 'plughw:{c},{s}'.format(c=self.card, s=self.subdevice)

    # =========================================================================
    @property
    def name(self):

        return self._name

    # =========================================================================
    @name.setter
    def name(self, value):

        self._name = value

    # =========================================================================
    @property
    def api(self):

        return self._api

    # =========================================================================
    @api.setter
    def api(self, value):

        self._api = value

    # =========================================================================
    @property
    def subdevice(self):

        return self._subdevice

    # =========================================================================
    @subdevice.setter
    def subdevice(self, value):

        self._subdevice = value

    # =========================================================================
    @property
    def card(self):

        return self._card

    # =========================================================================
    @card.setter
    def card(self, value):

        self._card = value

    # =========================================================================
    @property
    def description(self):

        return self._description

    # =========================================================================
    @description.setter
    def description(self, value):

        self._description = value

# =============================================================================

