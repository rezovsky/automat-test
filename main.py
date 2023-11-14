from pywinauto import keyboard, Desktop
from pywinauto.application import Application
import configparser


def open_app(type, link, links):
    if type == "g":
        action_key = "{RIGHT}"
    if type == "v":
        action_key = "{UP}"
    app = Application().start(chrome_app)
    app = Application(backend="uia").connect(title_re='Новая', timeout=5)
    keyboard.send_keys(link.get('links', links) + "{ENTER}")
    keyboard.send_keys("{VK_SHIFT down}{LWIN down}" + action_key + "{LWIN up}{VK_SHIFT up}{F11}^{F5}")


def close_chrome():
    chromes = Desktop(backend="uia").windows(title_re=".* Google Chrome$")
    if len(chromes) == 0:
        return
    for chrome in chromes:
        chrome.set_focus()
        keyboard.send_keys("%{F4}")


if __name__ == '__main__':
    close_chrome()

    settings = configparser.ConfigParser()
    settings.read('settings.ini')
    link = configparser.ConfigParser()
    link.read('links.ini')

    monitors_count = int(settings.get('settings', 'monitors'))
    orientation = settings.get('settings', 'orientation')
    chrome_app = settings.get('settings', 'chrome')

    links = settings.get('links', 'links').split(',')
    for count in range(monitors_count):
        open_app(orientation, link, links[count])
