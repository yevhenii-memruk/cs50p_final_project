from ctypes import windll
from ctypes import create_unicode_buffer
import time
import re


def window_title() -> str or None:
    """
    Obtain the title of foreground app.

    :var hwnd: Retrieve a window handle
    :var length: The maximum number of characters to copy to the buffer
    :var buffer: Create a mutable memory block containing unicode characters(text)

    :method .GetWindowTextW: Copies the text of the specified window's title bar into a buffer
    """

    hwnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buffer = create_unicode_buffer(length)

    windll.user32.GetWindowTextW(hwnd, buffer, length + 1)

    if buffer.value:
        return filter(buffer.value)
    else:
        return filter(None)
    

def filter(full_app_name: str) -> str or None:
    try:
        # Attempt to understand Telegram Window Handler
        if a := re.search(r".+[(]\d{5}\)$", full_app_name):
            return "Telegram"
        short = full_app_name.split("-")[-1].strip()
    except (AttributeError, TypeError):
        return None
    else:
        return short


if __name__ == "__main__":
    while True:
        time.sleep(1)
        print(window_title())