from pyautogui import *
import pyautogui
from time import sleep
import keyboard
import random
from win32api import SetCursorPos, mouse_event
import win32con


WINDOW_REGION: tuple[int, int, int, int] = (0, 130, 2560, 1400)
CLASS_LIST_REGION = (0, 539, 2560, 480)

def click(x, y) -> None:
    SetCursorPos((x, y))
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(3)

enrolled = False

while not enrolled:
    refresh_location = None
    proceed_location = None
    finish_location = None
    add_location = None
    open_location = None

    try:
        refresh_location = locateOnScreen(r".\assets\refresh.png", confidence=0.95)
    except Exception as e:
        print(e)

    i = 0
    while open_location is None and i <= 60:
        if keyboard.is_pressed("esc"):
            break
        try:
            open_location = locateOnScreen(r".\assets\open.png", confidence=0.95, region=CLASS_LIST_REGION)
        except Exception as e:
            print(e)
        finally:
            i += 1
            click(*center(refresh_location))

    try:
        proceed_location = locateOnScreen(r".\assets\proceed.png", confidence=0.95, region=WINDOW_REGION)
    except Exception as e:
        print(e)

    if proceed_location is not None:
        click(*center(proceed_location))

    try:
        finish_location = locateOnScreen(r".\assets\finish.png", confidence=0.95, region=WINDOW_REGION)
    except Exception as e:
        print(e)

    if finish_location is not None:
        click(*center(finish_location))

    try:
        add_location = locateOnScreen(r".\assets\add.png", confidence=0.95, region=WINDOW_REGION)
    except Exception as e:
        print(e)

    if add_location is not None:
        click(*center(add_location))

    if keyboard.is_pressed("esc"):
        break
