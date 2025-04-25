import sys
import threading
import time

import pandas as pd
from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Controller, Button
from tabulate import tabulate

from util import clear_terminal, create_menu, color_text, get_window_title


class Clicker:
    """A class that simulates an auto clicker

    === Public Attributes ===
    mouse: a Controller object that defines a mouse
    TOGGLE_KEY: a KeyCode object that records the key being pressed to start
    the auto clicker.
    """
    mouse: Controller
    TOGGLE_KEY: KeyCode
    _clicking: bool

    def __init__(self, toggle_key: str) -> None:
        """Initializes the auto clicker.
        """
        # Defining mouse
        self.mouse = Controller()
        self._clicking = False
        self.TOGGLE_KEY = KeyCode.from_char(toggle_key)
        self.QUIT_KEY = KeyCode.from_char('q')
        self.click_interval = 0.5
        self.click_count = 0

        # Defining status log
        self.data = {"Target App": [get_window_title()],
                "Click Interval": [self.click_interval],
                "Total Clicks": [self.click_count],
                "Status": [self._clicking]}
        self.status_info = pd.DataFrame(self.data)

    def _clicker(self) -> None:
        """Performs multiple left clicks at a speed of <self.click_count>.
        """
        while True:
            if self._clicking:
                self.mouse.click(Button.left)
                self.click_count += 1
            time.sleep(self.click_interval)

    def display_status(self) -> None:
        self.status_info["Status"] = self.status_info["Status"].astype(str)
        clear_terminal()
        if self._clicking:
            self.status_info.at[0, "Status"] = color_text("Running", "green")
        else:
            self.status_info.at[0, "Status"] = color_text("Stopped", "red")

        self.status_info.at[0, "Total Clicks"] = self.click_count

        print('\r' + str(tabulate(self.status_info, headers = 'keys', tablefmt = 'fancy_grid')) + '\n', end='')

    def _on_press(self, key: KeyCode) -> None:
        """A central dispatcher for multiple keyboard related events.
        """
        if key == self.TOGGLE_KEY:
            self._clicking = not self._clicking
            self.display_status()
        elif key == self.QUIT_KEY:
            clear_terminal()
            create_menu("Quitting Auto Clicker", "Thank you and have a great day")
            time.sleep(0.5)
            sys.exit(0)

    def run(self) -> None:
        """Runs the auto clicker application.
        """
        clicker_thread = threading.Thread(target=self._clicker)
        clicker_thread.daemon = True # Continuously runs in the background from the main thread.
        clicker_thread.start()

        with Listener(on_press=self._on_press) as listener:
            listener.join()
