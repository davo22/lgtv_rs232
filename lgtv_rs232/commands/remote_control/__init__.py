from .remote_control_lock import RemoteControlLockCommands, RemoteControlLock
from .send_key import SendKeyCommands, Key


class RemoteControlCommands(object):

    def __init__(self, send_command):
        self.remote_control_lock = RemoteControlLockCommands(send_command)
        self.send_key = SendKeyCommands(send_command)
