"""
Main game loop for CLI RPG.
"""

from core.logic import Character
from cli.interface import clear_screen, show_menu, battle_menu, turn_number


def main():
    """
    Runs the game.
    """
    # Create hero and enemies.
    hero = Character("Zeril", 100, 15, 20, 30)
    enemy_1 = Character("Troll", 80, 10, 25, 0)
    enemy_2 = Character("Knight", 90, 12, 25, 0)
    enemy_3 = Character("Dragon", 100, 15, 25, 0)

    # Store enemies in a dictionary.
    enemies = {1: enemy_1, 2: enemy_2, 3: enemy_3}

    while True:
        try:
            show_menu()  # Show enemy menu.
            while True:

                try:
                    enemy_choice = int(input("Choose your opponent (1–3): "))
                    print("")
                    if enemy_choice in enemies:
                        opponent = enemies[enemy_choice]
                        break
                except ValueError:
                    print("Invalid choice, try again.")

            turn = 0
            actions = {
                1: lambda: hero.attack(opponent=opponent),
                2: lambda: hero.heal(),
            }

            battle_menu(hero, opponent)

            # Main battle loop.
            while hero.hp > 0 and opponent.hp > 0:
                print("1. Attack | 2. Heal")

                try:
                    action = int(input("Choose your action: "))
                    print("\n===============================================")
                    turn = turn_number(turn)
                    if action in actions:
                        actions[action]()
                        if opponent.hp > 0:
                            opponent.attack(hero)
                    print("===============================================")
                except ValueError:
                    print("Invalid choice, try again.")

            # Show result.
            if hero.hp <= 0:
                print(f"\n{hero.name} has been defeated. You lost.\n")
            elif opponent.hp <= 0:
                print(f"\n{opponent.name} has been defeated. Victory!\n")

            # Reset characters and clear screen.
            hero.reset()
            for enemy in enemies.values():
                enemy.reset()
            clear_screen()

        except KeyboardInterrupt:
            print("\nProgram interrupted...")
            break


if __name__ == "__main__":
    main()
