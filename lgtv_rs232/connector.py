import logging
from typing import Iterator

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def join_data_string(data: Iterator[str]):
    string = ''
    for idx, item in enumerate(data):
        if not idx == 0:
            string += ' '
        string = string + item
    return string


def int2hex(data: int):
    return hex(data)[2:].upper().zfill(2)


class LgTvRs232Connector(object):

    def __init__(self, port):
        self.port = port

    async def _send_command(self, command: str, *data: int):
        _LOGGER.debug("sending command: {" + command + "} with data: {" + str(join_data_string(map(int2hex, data))) + "} to port: {" + self.port + "}")
        return 1

