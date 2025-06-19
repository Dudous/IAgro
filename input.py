from pynput.keyboard import Key, Controller
import time

# Create a keyboard controller object
keyboard = Controller()

while True:

    keyboard.press(Key.space)

    time.sleep(0.1)

    keyboard.release(Key.space)