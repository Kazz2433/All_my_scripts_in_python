# import subprocess
import pyautogui
import time

pyautogui.click(1915, 1057)
pyautogui.click(109, 231)
pyautogui.click()
time.sleep(3)
oi = pyautogui.getActiveWindow()
pyautogui.click(oi.left + 20, oi.top + 180)
# subprocess.call([])
