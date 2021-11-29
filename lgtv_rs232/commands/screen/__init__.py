from .aspect_ratio import AspectRatioCommands, AspectRatio
from .auto_tune import AutoTuneCommands
from .backlight import BacklightCommand
from .brightness import BrightnessCommands
from .color import ColorCommands
from .color_temperature import ColorTemperatureCommands
from .energy_saving import EnergySavingCommands, EnergySaving
from .screen_mute import ScreenMuteCommands, ScreenMute
from .sharpness import SharpnessCommands
from .tint import TintCommands


class ScreenCommands(object):

    def __init__(self, send_command):
        self.aspect_ratio = AspectRatioCommands(send_command)
        self.auto_tune = AutoTuneCommands(send_command)
        self.backlight = BacklightCommand(send_command)
        self.brightness = BrightnessCommands(send_command)
        self.color = ColorCommands(send_command)
        self.color_temperature = ColorTemperatureCommands(send_command)
        self.energy_saving = EnergySavingCommands(send_command)
        self.screen_mute = ScreenMuteCommands(send_command)
        self.sharpness = SharpnessCommands(send_command)
        self.ting = TintCommands(send_command)
