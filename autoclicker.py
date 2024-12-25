import time
import random
from pynput.mouse import Controller, Button, Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
from threading import Thread

mouse = Controller()

clicking = False
running = True
def on_key_press(key):
    global running
    try:
        if key.char == '\\':
            running = False
            return False
    except AttributeError:
        pass
def clicker():
    while running:
        if clicking:
            
            interval = random.uniform(0.02, 0.081)
            mouse.press(Button.left)
            time.sleep(random.uniform(0.0165, 0.019))
            mouse.release(Button.left)
            time.sleep(interval)
        else:
            time.sleep(0.1)

def on_click(x, y, button, pressed):
    global clicking
    if button == Button.middle: 
        clicking = pressed  

click_thread = Thread(target=clicker, daemon=True)
click_thread.start()

mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

with KeyboardListener(on_press=on_key_press) as keyboard_listener:
    keyboard_listener.join()

mouse_listener.stop()