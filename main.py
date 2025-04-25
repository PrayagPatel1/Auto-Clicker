import os

from clicker import Clicker

auto_clicker = Clicker('t')

def auto_clicker_menu() -> None:
    os.system("cls")
    print("=== Auto Clicker Application ===\n"
          "Press [T] to toggle the clicker on/off. Press [Q] to quit.\n"
          "Below is going to be a status table highlighting whether the auto clicker is active or not.\n")

auto_clicker_menu()
auto_clicker.run()
