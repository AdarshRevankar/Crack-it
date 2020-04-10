import pyautogui
import time


def move_mouse(x, y):
    pyautogui.moveRel(x, y, duration=10)
    print(x, y)
    time.sleep(100)
    move_mouse(x, y)


move_mouse(10, 10)
