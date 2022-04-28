from pynput.keyboard import Key, Controller
from ai-main import action
import time
keyboard = Controller()
def control(action):
# Press and release key
  keyboard.press(Key.action)
  keyboard.release(Key.action)
