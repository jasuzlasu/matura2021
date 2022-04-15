from winsound import Beep
import keyboard
from pynput.keyboard import Key, Listener
import pygame
OKTAWA = {'c': 261.6,
          'd': 293.7,
          'e': 329.6,
          'f': 349.2,
          'g': 391.9,
          'a': 440.0,
          'h': 493.9,
          'c2': 523.2}

DLUGOSCI = {'nuta': 500,
            'polnuta': 250}

UTWOR = [['g', 'nuta'],
         ['e', 'nuta'],
         ['e', 'nuta'],
         ['f', 'nuta'],
         ['d', 'nuta'],
         ['d', 'nuta'],
         ['c', 'polnuta'],
         ['e', 'polnuta'],
         ['g', 'polnuta']
         ]


def graj(nuta: str, dlugosc: int) -> None:
    Beep(int(OKTAWA[nuta]), DLUGOSCI[dlugosc])


def graj_wlazl_kotek(UTWOR):
    for nuta, dlugosc in UTWOR:
        graj(nuta, dlugosc)


def main() -> None:
    graj_wlazl_kotek(UTWOR)


def main_2():
    while True:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            Beep(440, 50)
        elif (keys[pygame.K_RIGHT]):
            Beep(600, 50)
        elif (keys[pygame.K_UP]):
            Beep(400, 50)
        elif (keys[pygame.K_DOWN]):
            Beep(550, 50)



if __name__ == '__main__':
    # main()
    main_2()
