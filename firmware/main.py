import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# TODO! add full functions when get it physically.
# in the same physical order
PINS = [
    board.D0, board.D1, board.D2,
    board.D3, board.D4, board.D5,
    board.D6, board.D7, board.D8,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, 
)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I,
    ]
]

if __name__ == '__main__':
    keyboard.go()
