import os


def clear_screen() -> None:
    """
    Clears the terminal after each battle.
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_menu() -> None:
    """
    Displays the main menu with a list of available enemies.
    """
    print("+---------------------------+")
    print("|     Welcome to CLI RPG    |")
    print("+---------------------------+")
    print("|     Available Enemies:    |")
    print("+---------------------------+")
    print("| 1. Troll (easy)           |")
    print("| 2. Knight (medium)        |")
    print("| 3. Dragon (hard)          |")
    print("+---------------------------+")
    print("| Press Ctrl + C to exit    |")
    print("+---------------------------+")


def battle_menu(hero: str, opponent: str) -> None:
    """
    Displays the start of every battle between the hero and the opponent.
    """
    print("==================================================================")
    print(f"The battle has started between {hero} and {opponent}")
    print("==================================================================\n")


def turn_number(turn: int) -> int:
    """
    Increments and displays the current turn number.
    """
    turn += 1
    print(f"                  Turn: {turn}")
    return turn
