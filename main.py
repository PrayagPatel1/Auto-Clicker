import os

from clicker import Clicker, clear

def auto_clicker_menu(title: str, description: str) -> None:
    """
    Creates a menu for the auto clicker application
    :param title: the title of the application.
    :param description: a short description of the application
    :return: None
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

if __name__ == '__main__':
    auto_clicker = Clicker('t')

    # Clear the screen and hide the cursor.
    clear()
    print("\x1b[?25l", end='')

    #Create the menu and run the auto clicker application
    menu_title = "Auto Clicker Application"
    menu_description = "Press [T] to toggle the clicker on/off. Press [Q] to quit."
    auto_clicker_menu(menu_title, menu_description)
    auto_clicker.run()
