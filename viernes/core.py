# Created by Henry Matarrita - March 2026

from viernes.personality import Personality
from viernes.brain import Brain


class Viernes:
    def __init__(self):
        self.personality = Personality()
        self.brain = Brain(self.personality)

        print(self.personality.boot_message())

    def run(self):
        print("Sistema en línea.")

        while True:
            command = input(">> ")

            if command.lower() == "exit":
                print(self.personality.shutdown_message())
                break

            response = self.brain.process(command)
            print(response)