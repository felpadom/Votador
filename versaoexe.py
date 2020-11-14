import time
import pyautogui

flag = 0
x = 0
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
time.sleep(0.15)

while x < 1000:

    xclick = pyautogui.locateOnScreen('procura2.png')
    try:
        yclick = pyautogui.center(xclick)
    except TypeError:
        xclick = pyautogui.locateOnScreen('procura1.png')
        yclick = pyautogui.center(xclick)

    pyautogui.click(yclick.x - 130, yclick.y)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write('dogao')
    time.sleep(0.1)
    xclick = pyautogui.locateOnScreen('dogao.png', region=(500, 0, 1000, 1080))
    try:
        yclick = pyautogui.center(xclick)
    except TypeError:
        print('cade o dogao?')
        pass

    pyautogui.click(yclick.x, yclick.y)
    time.sleep(0.01)

    while flag != 1:
        xclick = pyautogui.locateOnScreen('NotRobot.png')
        try:
            yclick = pyautogui.center(xclick)
            flag = 1
        except TypeError:
            pyautogui.press('pagedown')
            pass

    xclick = pyautogui.locateOnScreen('NotRobot.png')
    yclick = pyautogui.center(xclick)
    pyautogui.click(yclick.x, yclick.y)
    flag = 0
    while flag != 1:
        xclick = pyautogui.locateOnScreen('certinho.png')
        try:
            yclick = pyautogui.center(xclick)
            flag = 1
        except TypeError:
            pass

    flag = 0

    yclick = pyautogui.locateCenterOnScreen('votar.png')
    pyautogui.click(yclick.x, yclick.y)
    x += 1
    print('votos desde de o ultimo crash: ', x)
    time.sleep(1)
    yclick = pyautogui.locateCenterOnScreen('votardnv.png')
    pyautogui.click(yclick.x, yclick.y)
    time.sleep(0.1)
