import pyautogui
import time
import keyboard


pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

#pyautogui.moveTo(1364,752,2)
pyautogui.click()
pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.hotkey('enter')
pyautogui.write('C0ntabil')
time.sleep(0.5)
fw = pyautogui.getActiveWindow()
a= fw.topleft
pyautogui.click(a)
time.sleep(0.5)
pyautogui.click(510,463)
time.sleep(1)
#pyautogui.click(509, 461)
pyautogui.hotkey('enter')
time.sleep(1)
#pyautogui.hotkey('tab')
#pyautogui.hotkey('enter')
pyautogui.click(809, 598)
time.sleep(1)
pyautogui.hotkey('tab')
pyautogui.press('enter')
time.sleep(1)
sucess = pyautogui.getActiveWindow()
b= sucess.topleft
pyautogui.click(b)
time.sleep(0.8)
pyautogui.click(774,446)
