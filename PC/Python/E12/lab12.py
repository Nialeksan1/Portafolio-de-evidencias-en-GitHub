import pyautogui, subprocess, time, random, faker, pyperclip


def respuestas():
    time.sleep(60)
    screeWidth, screenHeight = pyautogui.size()
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(screeWidth/2,screenHeight/5)
    pyautogui.click()
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    rand = random.randint(1,10)
    for _ in range(rand):
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyperclip.copy('á')
    pyautogui.typewrite('"Todo lo que se hace por amor, se hace m')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite('s all')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite(' del bien y del mal" -Friedrich Nietzsche')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    rand = random.randint(0,11)
    for _ in range(rand):
        pyautogui.press('down')
    for _ in range(rand):
        pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    mail = faker.Faker().free_email()
    for letter in mail:
        if letter == '@':
            pyperclip.copy('@')
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.typewrite(letter)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)

subprocess.Popen(['start', 'msedge', 'https://forms.office.com/r/S8Jy6Jsvmh'], shell=True)
respuestas()
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
respuestas()
