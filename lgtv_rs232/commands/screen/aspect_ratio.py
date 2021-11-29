from enum import Enum


class AspectRatio(Enum):
    NORMAL_SCREEN_4_3 = 1
    WIDE_SCREEN_16_9 = 2
    ZOOM = 4
    ORIGINAL = 6
    WIDE_SCREEN_14_9 = 7
    PIXEL_1_1 = 9
    FULL_WIDE = 11
    CINEMA_ZOOM_1 = 16
    CINEMA_ZOOM_2 = 17
    CINEMA_ZOOM_3 = 18
    CINEMA_ZOOM_4 = 19
    CINEMA_ZOOM_5 = 20
    CINEMA_ZOOM_6 = 21
    CINEMA_ZOOM_7 = 22
    CINEMA_ZOOM_8 = 23
    CINEMA_ZOOM_9 = 24
    CINEMA_ZOOM_10 = 25
    CINEMA_ZOOM_11 = 26
    CINEMA_ZOOM_12 = 27
    CINEMA_ZOOM_13 = 28
    CINEMA_ZOOM_14 = 29
    CINEMA_ZOOM_15 = 30
    CINEMA_ZOOM_16 = 31


def map_to_state(data: int):
    return AspectRatio(data)


class AspectRatioCommands(object):
    command = "kc"

    def __init__(self, send_command):
        self.send_command = send_command

    async def get_state(self):
        return map_to_state(await self.send_command(self.command, 255))

    async def set_state(self, state: AspectRatio):
        return map_to_state(await self.send_command(self.command, state.value))
