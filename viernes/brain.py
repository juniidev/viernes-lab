# Created by Henry Matarrita - March 2026

class Brain:

    def __init__(self, personality, system):
        self.personality = personality
        self.system = system
        self.commands = {
            "hola": {
                "handler":self._greet,
                "description": "Saluda al usuario"
            },
            "estado":{
                "handler": self._status,
                "description": "Muestra el estado del sistema"
            },
            "hora":{
                "handler": self._datetime,
                "description": "Muestra la hora actual"
            },
            "ayuda": {
                "handler": self._help,
                "description": "Muestra lista de comandos"
            }
        }

    def process(self, command: str) -> str:
        command = command.lower().strip()   
        command_data = self.commands.get(command)

        if command_data:
            return command_data["handler"]()

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
    
    def _help(self) -> str:
        lines = ["Comandos disponibles:\n"]

        for cmd, info in self.commands.items():
            lines.append(f"{cmd} → {info['description']}")

        return "\n".join(lines)