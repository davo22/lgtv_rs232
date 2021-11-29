class AutoTuneCommands(object):
    _command = "ju"

    def __init__(self, send_command):
        self._send_command = send_command

    async def call(self):
        return await self._send_command(self._command, 1)
