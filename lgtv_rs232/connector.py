from typing import Iterator
from typing import Tuple
from string import Template
from serial import Serial, PARITY_NONE, EIGHTBITS, STOPBITS_ONE


def join_data_string(data: Iterator[str]):
    string = ''
    for idx, item in enumerate(data):
        if not idx == 0:
            string += ' '
        string = string + item
    return string


def int2hex(data: int):
    return hex(data)[2:].upper().zfill(2)


def hex2int(data: str):
    return int(data, 16)


def serialize_request(command: str, data: Tuple[int], device_id: int):
    return command_template.substitute(
        command=command,
        device_id=int2hex(device_id),
        data=join_data_string(map(int2hex, data))
    )


def deserialize_response(response: str):
    status = response[5:7]
    data = hex2int(response[7:-1])

    if not status == "OK":
        raise Exception('Device responded with error. Returned data: ' + str(data))

    return data


command_template = Template('$command $device_id $data\r')


class LgTvRs232Connector(object):

    def __init__(self, port: str, device_id: int):
        self.device_id = device_id
        self.serial = Serial(port=port, baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE)

    async def _send_command(self, command: str, *data: int):
        prepared_command = serialize_request(command, data, self.device_id)
        print("sending command: " + prepared_command)
        self.serial.write(prepared_command.encode())

        print("waiting for command response...")

        response = self.serial.read_until(expected='x')
        print("received command response: " + response)
        return deserialize_response(response)
