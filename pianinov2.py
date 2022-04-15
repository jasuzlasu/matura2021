from winsound import Beep
import keyboard
TIME = 1000

def main():
    while True:

        if keyboard.read_key() == "a":
            Beep(261, TIME)
        if keyboard.read_key() == "s":
            Beep(294, TIME)
        if keyboard.read_key() == "d":
            Beep(330, TIME)
        if keyboard.read_key() == "f":
            Beep(349, TIME)
        if keyboard.read_key() == "g":
            Beep(392, TIME)
        if keyboard.read_key() == "h":
            Beep(440, TIME)
        if keyboard.read_key() == "j":
            Beep(494, TIME)
        if keyboard.read_key() == "k":
            Beep(523, TIME)

if __name__ == '__main__':
    main()
