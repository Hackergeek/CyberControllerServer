from pymouse import PyMouse
from pykeyboard import PyKeyboard

mouse = PyMouse()
keyboard = PyKeyboard()

# keyboard.type_string("Hello, World")
# keyboard.press_keys(['Command', 'shift', '3'])
keyboard.press_key('Command')
keyboard.tap_key('tab')
keyboard.tap_key('tab')
# keyboard.release_key('Command')
