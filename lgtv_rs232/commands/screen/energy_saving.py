from enum import Enum


class EnergySaving(Enum):
    OFF = 0
    MINIMUM = 1
    MEDIUM = 2
    MAXIMUM = 3
    AUTO = 4
    SCREEN_OFF = 5


def map_to_state(data: int):
    return EnergySaving(data)


class EnergySavingCommands(object):
    _command = "jq"

    def __init__(self, send_command):
        self._send_command = send_command

    async def get_state(self):
        return map_to_state(await self._send_command(self._command, 255))

    async def set_state(self, state: EnergySaving):
        return map_to_state(await self._send_command(self._command, state.value))
