from clicker import Clicker
from util import clear_terminal, create_menu

if __name__ == '__main__':
    auto_clicker = Clicker('t')

    # Clear the screen and hide the cursor.
    clear_terminal()
    print("\x1b[?25l", end='')

    #Create the menu and run the auto clicker application
    menu_title = "Auto Clicker Application"
    menu_description = "Press [T] to toggle the clicker on/off. Press [Q] to quit."
    create_menu(menu_title, menu_description)
    auto_clicker.run()
