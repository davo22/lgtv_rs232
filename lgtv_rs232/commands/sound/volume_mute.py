from enum import Enum


class VolumeMute(Enum):
    ON = 0
    OFF = 1


def map_to_state(data: int):
    return VolumeMute(data)


class VolumeMuteCommands(object):
    command = "ke"

    def __init__(self, send_command):
        self.send_command = send_command

    async def get_state(self):
        return map_to_state(await self.send_command(self.command, 255))

    async def set_state(self, state: VolumeMute):
        return map_to_state(await self.send_command(self.command, state.value))
