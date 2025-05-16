import pygame
import time


class Sound:
    def __init__(self, sound) -> None:
        self.sound = sound
        pygame.mixer.init()

    def play(self) -> None:
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

    def stop(self) -> None:
        pygame.mixer.music.stop()
