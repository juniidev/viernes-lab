# Created by Henry Matarrita - March 2026

class Personality:

    def boot_message(self) -> str:
        return "Inicializando VIERNES... Sistemas estables. Por ahora."

    def shutdown_message(self) -> str:
        return "Apagando sistema. Intenta no romper nada mientras no estoy."

    def respond(self, type_: str, data: str | None = None):
        responses = {
            "greeting": "Hola. Espero que tengas algo interesante que decir.",
            "status": "Todos los sistemas operativos. Nivel de sarcasmo: 3%.",
            "unknown": "Comando no reconocido. Intenta algo menos creativo.",
            "time": f"Son exactamente las {data}. No es que el tiempo sea relativo, pero tú sí vas tarde."
    }

        return responses.get(type_, "Error interno. Curioso.")