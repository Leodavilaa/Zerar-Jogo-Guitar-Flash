import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1185,665,(0,152,0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1272,666,(255,0,0)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1363,669,(244,244,2)):
        pyautogui.press('j')
        sleep(0.05)