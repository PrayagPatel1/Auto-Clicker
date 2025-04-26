import os
import sys

import win32gui


def clear_terminal() -> None:
    """
    Clear the terminal screen
    :return: None
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def create_menu(title: str, description: str) -> None:
    """
        Displays a formatted main menu section with a title and description.

        Args:
            title (str): The main heading of the menu.
            description (str): A short description or subtitle displayed beneath the title.

        Returns:
            None
    """
    lines = [title, "", description]

    # Calculate the max width and height for the border and the padding
    max_length = 0
    for line in lines:
        max_length = max(len(line), max_length)
    padding = 6
    box_width = max_length + padding

    # Define border characters
    border_char = {"t_left": '┌',
                   "t_right": '┐',
                   "b_left": '└',
                   "b_right": '┘',
                   "vertical": '|',
                   "horizontal": '-'}

    # Create the border
    print(border_char["t_left"] + border_char["horizontal"] * box_width + border_char["t_right"])

    for line in lines:
        spaces = box_width - len(line)
        left_padding = padding // 2
        right_padding = spaces - left_padding
        print(border_char["vertical"] + " " * left_padding + line + " " * right_padding + border_char["vertical"])

    print(border_char["b_left"] + border_char["horizontal"] * box_width + border_char["b_right"])

def color_text(text: str, color: str) -> str:
    """
        Returns <text> in a new color by using <color>

        Args:
            text (str): a piece of text to the change the color of.
            color (str): the color that the text changes to.

        Returns:
            None
    """
    colors = {'red': '\x1b[1;31m',
              'green': '\x1b[1;32m',
              'yellow': '\x1b[1;33m',
              'blue': '\x1b[1;34m',}

    return f"{colors.get(color, '')}{text}\x1b[0m"

def get_window_title() -> str:
    """
        Gets the title of the window that is currently active

        Returns:
            str
    """
    if os.name != 'nt':
        return "Unsupported OS"

    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except Exception:
        return "Unknown"

def flush_input() -> None:
    """
        Clears the pynput keyboard buffer.

        Returns:
            None
    """
    try:
        import msvcrt as ms
        while ms.kbhit():
            ms.getch()
    except ImportError:
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
