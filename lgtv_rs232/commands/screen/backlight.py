from ..exceptions import InvalidArgumentException


class BacklightCommand(object):
    command = "mg"

    def __init__(self, send_command):
        self.send_command = send_command

    def get_state(self):
        return self.send_command(self.command, 255)

    def set_state(self, state: int):
        if state > 100 or state < 0:
            raise InvalidArgumentException('Backlight state must be an int value between 0 and 100')

        return self.send_command(self.command, state)
