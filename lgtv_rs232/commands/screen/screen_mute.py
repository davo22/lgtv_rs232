from enum import Enum


class ScreenMute(Enum):
    SCREEN_MUTE_OFF = 0
    SCREEN_MUTE_ON = 1
    VIDEO_MUTE_ON = 16


def map_to_state(data: int):
    return ScreenMute(data)


class ScreenMuteCommands(object):
    command = "kd"

    def __init__(self, send_command):
        self.send_command = send_command

    async def get_state(self):
        return map_to_state(await self.send_command(self.command, 255))

    async def set_state(self, state: ScreenMute):
        return map_to_state(await self.send_command(self.command, state.value))
