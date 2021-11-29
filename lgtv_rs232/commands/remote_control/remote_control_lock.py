from enum import Enum


class RemoteControlLock(Enum):
    OFF = 0
    ON = 1


def map_to_state(data: int):
    return RemoteControlLock(data)


class RemoteControlLockCommands(object):
    _command = "km"

    def __init__(self, send_command):
        self._send_command = send_command

    async def get_state(self):
        return map_to_state(await self._send_command(self._command, 255))

    async def set_state(self, state: RemoteControlLock):
        return map_to_state(await self._send_command(self._command, state.value))

    def on(self):
        return self.set_state(RemoteControlLock.ON)

    def off(self):
        return self.set_state(RemoteControlLock.OFF)
