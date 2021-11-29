from .balance import BalanceCommands
from .bass import BassCommands
from .treble import TrebleCommands
from .volume_control import VolumeControlCommands
from .volume_mute import VolumeMuteCommands, VolumeMute


class SoundCommands(object):

    def __init__(self, send_command):
        self.balance = BalanceCommands(send_command)
        self.bass = BassCommands(send_command)
        self.treble = TrebleCommands(send_command)
        self.volume_control = VolumeControlCommands(send_command)
        self.volume_mute = VolumeMuteCommands(send_command)

