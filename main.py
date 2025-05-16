from pynput import keyboard
from core.sound import Sound
import pygame


sounds = {
    "1": Sound("assets/audio/clap.wav"),
    "2": Sound("assets/audio/drum.wav"),
    "3": Sound("assets/audio/bell.wav"),
    "4": Sound("assets/audio/applause.wav"),
    "5": Sound("assets/audio/laugh.wav"),
}


def on_press(key):
    try:
        char = key.char.lower()
        if char in sounds:
            print(f"Playing {char} sound")
            sounds[char].play()
        elif char == "s":
            print("Stopping sound")
            pygame.mixer.music.stop()
    except AttributeError:
        pass


print("Press keys: 1 (clap), 2 (drum), 3 (bell), 4 (applause), s (stop)")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
