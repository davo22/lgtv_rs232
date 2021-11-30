import asyncio
from connector import LgTvRs232Connector
from commands.power import PowerCommands, Power
from commands.screen import ScreenCommands, AspectRatio, ScreenMute
from commands.sound import SoundCommands
from commands.osd_select import OSDSelectCommands
from commands.remote_control import RemoteControlCommands


class LgTvRs232Client(LgTvRs232Connector):
    """LG TV RS-232 client."""

    def __init__(self, port: str, device_id=0):
        """Initialize the LG TV client."""
        super().__init__(port, device_id)
        self.power = PowerCommands(self._send_command)
        self.screen = ScreenCommands(self._send_command)
        self.sound = SoundCommands(self._send_command)
        self.osd_select = OSDSelectCommands(self._send_command)
        self.remote_control = RemoteControlCommands(self._send_command)
