from enum import Enum


class Input(Enum):
    DTV = 0
    ANALOG = 1
    AV = 2
    COMPONENT = 4
    RGB = 6
    HDMI_1 = 7
    HDMI_2 = 8
    HDMI_3 = 9
    HDMI_4 = 10


def map_to_state(data: int):
    return Input(data)


class InputCommands(object):
    _command = "xb"

    def __init__(self, send_command):
        self._send_command = send_command

    async def get_state(self):
        return map_to_state(await self._send_command(self._command, 255))

    async def set_state(self, state: Input):
        return map_to_state(await self._send_command(self._command, state.value))
