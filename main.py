from time import sleep

from pywinauto import keyboard
from pywinauto.application import Application

import configparser


chrome_app = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def open_app(type, link, links):
    if type == "g":
        action_key = "{RIGHT}"
    if type == "v":
        action_key = "{UP}"
    app = Application().start(chrome)
    app = Application(backend="uia").connect(title_re='Новая', timeout=5)
    keyboard.send_keys(link.get('links', links) + "{ENTER}")
    keyboard.send_keys(
        "{VK_SHIFT down}{LWIN down}" + action_key + "{LWIN up}{VK_SHIFT up}{F11}"
    )


if __name__ == '__main__':
    settings = configparser.ConfigParser()
    settings.read('settings.ini')
    link = configparser.ConfigParser()
    link.read('links.ini')

    monitors_count = int(settings.get('settings', 'monitors'))
    orientation = settings.get('settings', 'orientation')
    chrome = settings.get('settings', 'chrome')

    links = settings.get('links', 'links').split(',')
    for count in range(monitors_count):
        open_app(orientation, link, links[count])
