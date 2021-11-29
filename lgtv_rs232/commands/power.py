from enum import Enum


class Power(Enum):
    OFF = 0
    ON = 1


def map_to_state(data: int):
    return Power(data)


class PowerCommands(object):
    _command = "ka"

    def __init__(self, send_command):
        self._send_command = send_command

    async def get_state(self):
        return map_to_state(await self._send_command(self._command, 255))

    async def set_state(self, state: Power):
        return map_to_state(await self._send_command(self._command, state.value))

    def on(self):
        return self.set_state(Power.ON)

    def off(self):
        return self.set_state(Power.OFF)
