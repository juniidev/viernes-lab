# Created by Henry Matarrita - March 2026

from viernes.personality import Personality
from viernes.brain import Brain
from viernes.system import System


class Viernes:
    def __init__(self):
        self.personality = Personality()
        self.system = System()
        self.brain = Brain(self.personality, self.system)

        print(self.personality.boot_message())

    def run(self):
        print("Viernes iniciado. Esperando comandos.")

        while True:
            command = input(">> ")

            if command.lower().strip() == "salir":
                print("Apagando sistema.")
                break

            response = self.brain.process(command)
            print(response)