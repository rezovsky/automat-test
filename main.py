import socket
from time import sleep

import pyautogui
from pywinauto import keyboard, Desktop
from pywinauto.application import Application
import configparser


def open_app(action_key, link, links, count, chrome_app, js):
    app = Application().start(chrome_app)
    app = Application(backend="win32").connect(title_re='Новая', timeout=5)

    chrome = get_apps('.*Google Chrome.*')[0]
    chrome.move_window(0, 0, 1920, 1080)

    keyboard.send_keys(link.get('links', links) + "{ENTER}", pause=0.0001)
    keyboard.send_keys("{F11}")

    actions = link.get('actions', links).split(",")
    for action in actions:
        find_img(action.strip())

    sleep(2)
    keyboard.send_keys("{F12}")
    sleep(2)
    find_img("console")
    keyboard.send_keys(js + "{ENTER}", pause=0.0001)
    sleep(2)
    keyboard.send_keys("{F12}")
    sleep(2)

    if count > 0:
        keyboard.send_keys("{VK_SHIFT down}{LWIN down}" + action_key + "{LWIN up}{VK_SHIFT up}")

    return app


def find_img(img):
    if img.split(":")[0] == "m":
        pyautogui.moveTo(10, 10)
        img = img.split(":")[1]

    while True:
        try:
            pos = pyautogui.locateOnScreen(f"img/{img}.png", confidence=.98, grayscale=True)
            break
        except:
            pass
    pyautogui.click(pos)


def close_chrome():
    chromes = Desktop(backend="win32").windows(title_re=".* Google Chrome$")
    if len(chromes) == 0:
        return
    for chrome in chromes:
        chrome.close()


def press_reload(windows):
    while True:
        try:
            pos = pyautogui.locateOnScreen(f"img/reload.png", confidence=.98, grayscale=True)
            left = windows.left + (pos.left + pos.width / 2)
            top = windows.top + (pos.top + pos.height / 2)
            pyautogui.click(left, top)
            pyautogui.moveTo((windows.left + windows.right) / 2, 10)
            break
        except:
            pass


def main():
    print(socket.gethostname())
    actions = {'g': '{LEFT}', 'v': '{UP}'}
    re_actions = {'g': '{RIGHT}', 'v': '{DOWN}'}

    close_chrome()

    settings = configparser.ConfigParser()
    settings.read('settings.ini')
    link = configparser.ConfigParser()
    link.read('links.ini')

    monitors_count = int(settings.get('settings', 'monitors'))
    reloat_time = int(settings.get('settings', 'reload'))
    title_pattern = settings.get('settings', 'title_pattern')
    js = settings.get('settings', 'js')
    orientation = settings.get('settings', 'orientation')
    chrome_app = settings.get('settings', 'chrome')

    links = settings.get('links', 'links').split(',')

    for count in range(monitors_count):
        open_app(actions[orientation], link, links[count], count, chrome_app, js)

    keyboard.send_keys("%{TAB}")

    reload_counter = 0

    while True:
        apps = get_apps(title_pattern)
        if not len(apps) == monitors_count:
            break

        sleep(1)
        reload_counter += 1
        if reload_counter == reloat_time:
            reload_counter = 0
            for app in apps:
                windows = app.rectangle()
                # press_reload(windows)


def get_apps(title_pattern):
    apps = Desktop(backend="win32").windows(title_re=title_pattern)
    return apps


if __name__ == '__main__':
    while True:
        main()
