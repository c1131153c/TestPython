import win32api
import pyautogui as pag
import time
import keyboard

while True:

    if keyboard.is_pressed('esc'):
        break
    else:
        time.sleep(0.5)
        #x, y = win32api.GetCursorPos()
        x, y = pag.position()
        print('( x=', x, "y=", y, ")")