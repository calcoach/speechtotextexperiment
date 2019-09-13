from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def minimice():
# Press and release space
  with keyboard.pressed(Key.cmd):
    keyboard.press('d')
    keyboard.release('d')



def open(app):

    if(app._contains_('navegador')):
        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)

        keyboard.type("Chrome")
        time.sleep(0.12)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


