# Created by Henry Matarrita - March 2026

class Brain:

    def __init__(self, personality, system):
        self.personality = personality
        self.system = system
        self.commands = {
            "hola": self._greet,
            "estado": self._status,
            "hora": self._datetime
        }

    def process(self, command: str) -> str:
        command = command.lower().strip()
        handler = self.commands.get(command)

        if handler:
            return handler()

        return self._unknown()

    def _greet(self) -> str:
        return self.personality.respond("greeting")

    def _status(self) -> str:
        return self.personality.respond("status")

    def _unknown(self) -> str:
        return self.personality.respond("unknown")
    
    def _datetime(self) -> str:
        time = self.system.get_time()
        return self.personality.respond("time", time)