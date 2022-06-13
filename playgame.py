from hero import Hero
from monster import Monster
from goblin import Goblin
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
import random
import os

WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"
MONSTER_CHAR = "M"
GOBLIN_CHAR = "G"


class _Environment:
    """Environment includes Maze+Monster+Goblin"""
    def __init__(self, maze):
        self._environment = deepcopy(maze)

    def set_coord(self, x, y, val):
        self._environment[x][y] = val

    def get_coord(self, x, y):
        return self._environment[x][y]

    def print_environment(self):
        """print out the environment in the terminal"""
        print("---------------------------------------------------")
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", WALL_CHAR)           # replace the wall character
            row_str = row_str.replace("0", SPACE_CHAR)          # replace the space character
            row_str = row_str.replace("2", HERO_CHAR)           # replace the hero character
            row_str = row_str.replace("3", MONSTER_CHAR)        # replace the monster character
            row_str = row_str.replace("4", MONSTER_CHAR)
            row_str = row_str.replace("5", MONSTER_CHAR)
            row_str = row_str.replace("6", GOBLIN_CHAR)         # replace the goblin character
            row_str = row_str.replace("7", GOBLIN_CHAR)
            row_str = row_str.replace("8", GOBLIN_CHAR)

            print("".join(row_str))

        print("---------------------------------------------------")


class Game:

    _count = 0

    def __init__(self):
        self.myHero = Hero()

        # all the creatures
        self.thief_monster = self.myHero.get_thief_monster()
        self.fighter_monster = self.myHero.get_fighter_monster()
        self.gamer_monster = self.myHero.get_gamer_monster()
        self.random_monster_1 = self.myHero.get_random_monster_1()
        self.random_monster_2 = self.myHero.get_random_monster_2()
        self.monsters_initial_positions = []

        self.wealth_goblin = self.myHero.get_wealth_goblin()
        self.health_goblin = self.myHero.get_health_goblin()
        self.gamer_goblin = self.myHero.get_gamer_goblin()
        self.random_goblin_1 = self.myHero.get_random_goblin_1()
        self.random_goblin_2 = self.myHero.get_random_goblin_2()
        self.goblins_initial_positions = []

        self.maze = make_maze_recursion(17, 17)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self._count = 0

    def hero_initialisation(self, initial_coordinates):
        x = initial_coordinates[0]
        y = initial_coordinates[1]

        while self.MyEnvironment._environment[x][y] != 0:
            initial_coordinates = self.myHero.new_initial_position()
            x = initial_coordinates[0]
            y = initial_coordinates[1]

        self.MyEnvironment._environment[x][y] = 2

    def creature_initialisation(self, creature_type, creature_initial_positions, value):
        creature_initial_coordinates = creature_type.initial_position()
        x = creature_initial_coordinates[0]
        y = creature_initial_coordinates[1]

        while self.MyEnvironment._environment[x][y] != 0:
            creature_initial_coordinates = creature_type.new_initial_position()
            x = creature_initial_coordinates[0]
            y = creature_initial_coordinates[1]

        creature_initial_positions.append(creature_type.print_position())
        self.MyEnvironment._environment[x][y] = value

    def play(self):

        hero_initial_coordinates = self.myHero.initial_position()
        self.hero_initialisation(hero_initial_coordinates)

        # methods for initial coordinates of the creatures
        self.creature_initialisation(self.thief_monster, self.monsters_initial_positions, 3)
        self.creature_initialisation(self.fighter_monster, self.monsters_initial_positions, 4)
        self.creature_initialisation(self.gamer_monster, self.monsters_initial_positions, 5)
        self.creature_initialisation(self.random_monster_1, self.monsters_initial_positions, self.random_monster_1.maze_value())
        self.creature_initialisation(self.random_monster_2, self.monsters_initial_positions, self.random_monster_2.maze_value())

        self.creature_initialisation(self.wealth_goblin, self.goblins_initial_positions, 6)
        self.creature_initialisation(self.health_goblin, self.goblins_initial_positions, 7)
        self.creature_initialisation(self.gamer_goblin, self.goblins_initial_positions, 8)
        self.creature_initialisation(self.random_goblin_1, self.goblins_initial_positions, self.random_goblin_1.maze_value())
        self.creature_initialisation(self.random_goblin_2, self.goblins_initial_positions, self.random_goblin_2.maze_value())

        os.system("cls")
        self.MyEnvironment.print_environment()
        self.myHero.print_position()
        print("MONSTERS: ")
        print(" \n".join(self.monsters_initial_positions), "\n")
        print("GOBLINS: ")
        print(" \n".join(self.goblins_initial_positions), "\n")
        print("You can move the hero by using the keyboard arrows.\n")
        print("Press the 'H' key the available operations.")
        print("Press the 'M' key to see the current map and positions.")

        print("===============================\nPress 'Esc' if you want to quit\n===============================\n\n")

        while True:
            if self.myHero.move(self.MyEnvironment):
                # if self.myHero.move_debug(self.MyEnvironment):# #   # this works in debug mode
                self.MyEnvironment.print_environment()
                self._count += 1
                self.myHero.steps_limit(self._count)
                self.myHero.decrease_health()
                self.myHero.show_gold_coins()
                self.myHero.print_position()
                print(f"Number of steps: {self._count}")
                print(f"===============================\nPress 'Esc' if you want to quit\n"
                      f"===============================\n")


if __name__ == "__main__":

    myGame = Game()
    myGame.play()
