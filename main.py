import sys

from clicker import Clicker

auto_clicker = Clicker('t')

def auto_clicker_menu(title: str, description: str) -> None:
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

menu_title = "Auto Clicker Application"
menu_description = "Press [T] to toggle the clicker on/off. Press [Q] to quit."
auto_clicker_menu(menu_title, menu_description)
auto_clicker.run()
