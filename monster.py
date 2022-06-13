#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import random
from getch1 import *


class Monster:
    """define your monster class here"""

    def __init__(self, type=random.randint(1, 3)):

        self.monster_type = type                            # the type of monster

        self.thief_success_rate = random.randint(50, 100)   # thief monster success rate - between 50 an 100%
        self.coins_to_steal = random.randint(10, 100)       # the number of coins to be stolen - between 10 and 100

        self.fighter_success_rate = random.randint(30, 60)  # the fighter monster success rate - between 30 and 60%
        self.health_to_steal = random.randint(1, 30)        # the health points to be stolen - between 1 and 30

        self._coordX = random.randint(1, 16)                # generates the x coordinate
        self._coordY = random.randint(1, 16)                # generates the y coordinate

        self.player_choice = ""                             # helping variable for the RPS game

        self.meetings = []                                  # helping variable for the game termination

    def get_coord_x(self):              # method to return X coordinate
        return self._coordX

    def get_coord_y(self):              # method to return Y coordinate
        return self._coordY

    def initial_position(self):         # method to return initial coordinates
        return self._coordX, self._coordY

    def new_initial_position(self):     # method to generate new initial coordinates if necessary
        self._coordX = random.randint(1, 16)
        self._coordY = random.randint(1, 16)

        return self._coordX, self._coordY

    def number_type(self):              # method to return the monster number type - 1 to 3
        return self.monster_type

    def maze_value(self):               # method to return the monster maze value
        if self.monster_type == 1:
            return 3
        elif self.monster_type == 2:
            return 4
        else:
            return 5

    def type_of_monster(self):          # method to return the monster type in words
        monster_type = self.number_type()

        if monster_type == 1:
            return "thief monster"
        elif monster_type == 2:
            return "fighter monster"
        else:
            return "gamer monster"

    def ability(self):                  # method to return the monster ability
        type = self.number_type()
        if type == 1:
            return f"({self.get_coins_to_steal()}, {self.get_thief_success_rate()}%)"
        elif type == 2:
            return f"({self.get_health_to_steal()}, {self.get_fighter_success_rate()}%)"
        else:
            return f"({self.get_coins_to_steal()}, {self.get_health_to_steal()})"

    def print_position(self):           # method to display the monster coordinates and ability
        monster_type = self.type_of_monster()
        return f"There is a {monster_type} at position ({self._coordX}; {self._coordY}) with ability" \
               f" {self.ability()}"

    def get_thief_success_rate(self):       # method to return the thief monster success rate
        return self.thief_success_rate

    def get_fighter_success_rate(self):     # method to return the fighter monster success rate
        return self.fighter_success_rate

    def get_coins_to_steal(self):           # method to return the coins to be stolen
        return self.coins_to_steal

    def get_health_to_steal(self):          # method to return the health points to be stolen
        return self.health_to_steal

    def stealing(self, gold_coins):         # method for possible stealing of coins
        self.meetings += "thief"

        coefficient = random.randint(1, 100)
        success_rate = self.get_thief_success_rate()
        coins_to_steal = self.get_coins_to_steal()

        if coefficient <= success_rate:
            gold_coins -= coins_to_steal

        return gold_coins

    def fighting(self, health):             # method of possible stealing of health points
        self.meetings += "fighter"

        coefficient = random.randint(1, 100)
        success_rate = self.get_fighter_success_rate()
        health_to_steal = self.get_health_to_steal()

        if coefficient <= success_rate:
            health -= health_to_steal

        return health

    def rock_paper_scissors_gold_coins(self, gold_coins):       # additional method for RPS
        gold_coins_to_steal = self.get_coins_to_steal()
        gold_coins -= gold_coins_to_steal
        return gold_coins

    def rock_paper_scissors_health_score(self, health):         # additional method for RPS
        health_points_to_steal = self.get_health_to_steal()
        health -= health_points_to_steal
        return health

    def rock_paper_scissors(self, coins, health_score):         # method RPS
        self.meetings += "gamer"
        result = "DRAW"
        tools = ["R", "P", "S"]
        gold_coins = coins
        health = health_score
        self.player_choice = 0
        symbol_value = 0

        print("Please select a game mode: PRESS 'A' for AUTOMATIC or 'I' for INTERACTIVE: ")
        game_mode = getch()
        while ord(game_mode) != 97 and ord(game_mode) != 41 and ord(game_mode) != 105 and ord(game_mode) != 73:
            print("Please enter a valid input: 'A' for AUTOMATIC Mode or 'I' for INTERACTIVE: ")
            game_mode = getch()

        while result == "DRAW":
            if ord(game_mode) == 97 or ord(game_mode) == 41:
                self.player_choice = random.choice(tools)
            elif ord(game_mode) == 105 or ord(game_mode) == 73:
                print("Please, select a tool: rock, paper or scissors? "
                      "Press 'R' for rock, 'P' for paper or 'S' for scissors: ")

                self.player_choice = getch()
                symbol_value = ord(self.player_choice)
                while symbol_value != 114 and symbol_value != 82 and symbol_value != 112 \
                        and symbol_value != 80 and symbol_value != 115 and symbol_value != 83:

                    print("Invalid input! Please select between 'R' for rock, 'P' for paper or 'S' for scissors: ")
                    self.player_choice = getch()

            monster_choice = random.choice(tools)

            if symbol_value == 114 or symbol_value == 82:
                print("Your choice is ROCK.")
                if monster_choice.upper() == "R":
                    print("The gamer monster choice is ROCK.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")
                elif monster_choice.upper() == "P":
                    print("The gamer monster choice is PAPER.")
                    result = "LOSE"
                    print(f"You {result}! The gamer monster wins!")

                    gold_coins = self.rock_paper_scissors_gold_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)
                else:
                    print("The gamer monster choice is SCISSORS.")
                    result = "WIN"
                    print(f"You {result}!")

            elif symbol_value == 112 or symbol_value == 80:
                print("Your choice is PAPER.")
                if monster_choice.upper() == "R":
                    print("The gamer monster choice is ROCK.")
                    result = "WIN"
                    print(f"You {result}!")
                elif monster_choice.upper() == "P":
                    print("The gamer monster choice is PAPER.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")
                else:
                    print("The gamer monster choice is SCISSORS.")
                    result = "LOSE"
                    print(f"You {result}! The gamer monster wins!")

                    gold_coins = self.rock_paper_scissors_gold_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

            else:
                print("Your choice is SCISSORS.")
                if monster_choice.upper() == "R":
                    print("The gamer monster choice is ROCK.")
                    result = "LOSE"
                    print(f"You {result}! The gamer monster wins!")

                    gold_coins = self.rock_paper_scissors_gold_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

                elif monster_choice.upper() == "P":
                    print("The gamer monster choice is PAPER.")
                    result = "WIN"
                    print(f"You {result}!")
                else:
                    print("The gamer monster choice is SCISSORS.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")

        return gold_coins, health






