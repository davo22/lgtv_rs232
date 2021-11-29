from enum import Enum


class Key(Enum):
    POWER_SAVING = 149
    POWER = 8
    INPUT = 11
    _3D = 220
    TV_RAD = 240
    QUICK_MENU = 69
    MENU = 67
    GUIDE = 171
    UP = 64
    DOWN = 65
    LEFT = 7
    RIGHT = 6
    OK = 68
    BACK = 40
    EXIT = 91
    INFO = 170
    AV_MODE = 48
    VOLUME_UP = 2
    VOLUME_DOWN = 3
    FAV = 30
    MUTE = 9
    CHANNEL_PAGE_UP = 0
    CHANNEL_PAGE_DOWN = 1
    NUMBER_0 = 16
    NUMBER_1 = 17
    NUMBER_2 = 18
    NUMBER_3 = 19
    NUMBER_4 = 20
    NUMBER_5 = 21
    NUMBER_6 = 22
    NUMBER_7 = 23
    NUMBER_8 = 24
    NUMBER_9 = 25
    LIST = 83
    QUICK_VIEW = 26
    RED = 114
    GREEN = 113
    YELLOW = 99
    BLUE = 97
    TEXT = 32
    T_OPT = 32
    SUBTITLE = 39
    SIMPLINK = 126
    AD = 145
    STOP = 177
    PLAY = 176
    PAUSE = 186
    REWIND = 143
    FAST_FORWARD = 142
    NETCAST = 89
    AT = 88
    APP = 159


def map_to_state(data: int):
    return Key(data)


class SendKeyCommands(object):
    _command = "mc"

    def __init__(self, send_command):
        self._send_command = send_command

    async def call(self, key: Key):
        return map_to_state(await self._send_command(self._command, key.value))
