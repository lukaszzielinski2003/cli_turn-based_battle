import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
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


def battle_menu(hero, opponent):
    print("==================================================================")
    print(f"The battle has started between {hero} and {opponent}")
    print("==================================================================\n")


def turn_number(turn):
    turn += 1
    print(f"                  Turn: {turn}")
    return turn
