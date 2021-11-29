from enum import Enum


class OSD(Enum):
    OFF = 0
    ON = 1


def map_to_state(data: int):
    return OSD(data)


class OSDSelectCommands(object):
    _command = "kl"

    def __init__(self, send_command):
        self._send_command = send_command

    async def get_state(self):
        return map_to_state(await self._send_command(self._command, 255))

    async def set_state(self, state: OSD):
        return map_to_state(await self._send_command(self._command, state.value))

    def on(self):
        return self.set_state(OSD.ON)

    def off(self):
        return self.set_state(OSD.OFF)
