from clicker import Clicker
from util import clear_terminal, create_menu

if __name__ == '__main__':
    # Clear the screen.
    clear_terminal()
    print("\x1b[?25l", end='')  # hide the cursor.

    #Create the main menu
    menu_title = "Terminal Auto Clicker Application"
    menu_description = "Press [T] to toggle the clicker on/off. Press [Q] to quit."
    create_menu(menu_title, menu_description)

    while True:
        try:
            click_interval_input = float(input("Enter click interval in seconds, "
                                               "press [Enter], and press [T] to start: "))
            auto_clicker = Clicker('t', click_interval_input)
            auto_clicker.run()
            break
        except ValueError:
            print("Invalid input. PLease try again.")
