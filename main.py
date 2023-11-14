from time import sleep

from pywinauto import keyboard
from pywinauto.application import Application

chrome_app = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

monitors_count = 3

links = ('https://vk.com', 'https://sima-land.com', 'https://youtube.com')


def open_app(count, type="g"):
    if type == "g":
        action_key = "{RIGHT}"
    if type == "v":
        action_key = "{UP}"
    app = Application(backend="uia").start(chrome_app)
    sleep(.5)
    keyboard.send_keys(links[count] + "{ENTER}")
    keyboard.send_keys(
        "{VK_SHIFT down}{LWIN down}" + action_key + "{LWIN up}{VK_SHIFT up}{F11}"
    )


if __name__ == '__main__':
    for count in range(monitors_count):
        open_app(count, "g")
