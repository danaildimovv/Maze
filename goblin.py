#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import random
from getch1 import *


class Goblin:
    def __init__(self, type=random.randint(1, 3)):
        self.goblin_type = type

        self.wealth_goblin_success_rate = random.randint(40, 70)    # wealth goblin success rate - between 40 and 70%
        self.wealth_coins_to_give = random.randint(50, 200)         # coins to be given - between 50 and 200

        self.health_goblin_success_rate = random.randint(60, 80)    # health goblin success rate - between 60 and 80%
        self.health_points_to_give = random.randint(40, 100)        # health points to be given - between 40 and 100

        self._coordX = random.randint(1, 16)                        # random X coordinate
        self._coordY = random.randint(1, 16)                        # random Y coordinate

        self.player_choice = ""                                     # helping variable for the RPS game

    def get_coord_x(self):          # method to return X coordinate
        return self._coordX

    def get_coord_y(self):          # method to return Y coordinate
        return self._coordY

    def initial_position(self):         # method to return goblin initial coordinates
        return self._coordX, self._coordY

    def new_initial_position(self):     # method to generate new initial position if the first gen place is not free
        self._coordX = random.randint(1, 16)
        self._coordY = random.randint(1, 16)
        return self._coordX, self._coordY

    def number_type(self):              # method to return the goblin type in number from 1 to 3
        return self.goblin_type

    def maze_value(self):
        if self.goblin_type == 1:       # method to return the goblin value in the maze
            return 6
        elif self.goblin_type == 2:
            return 7
        else:
            return 8

    def type_of_goblin(self):           # method to return the goblin type in words
        goblin_type = self.number_type()

        if goblin_type == 1:
            return "wealth goblin"
        elif goblin_type == 2:
            return "health goblin"
        else:
            return "gamer goblin"

    def get_wealth_goblin_success_rate(self):   # method to return the wealth goblin success rate
        return self.wealth_goblin_success_rate

    def get_wealth_coins_to_give(self):         # method to return the coins that the wealth goblin would give
        return self.wealth_coins_to_give

    def get_health_goblin_success_rate(self):   # method to return the health goblin success rate
        return self.health_goblin_success_rate

    def get_health_points_to_give(self):        # method to return the health points that the health goblin would give
        return self.health_points_to_give

    def ability(self):                          # method to return the goblin ability
        type = self.number_type()
        if type == 1:
            return f"({self.get_wealth_coins_to_give()}, {self.get_wealth_goblin_success_rate()}%)"
        elif type == 2:
            return f"({self.get_health_points_to_give()}, {self.get_health_goblin_success_rate()}%)"
        else:
            return f"({self.get_wealth_coins_to_give()}, {self.get_health_points_to_give()})"

    def print_position(self):                   # method to display the goblin coordinates and ability
        goblin_type = self.type_of_goblin()
        return f"There is a {goblin_type} at position ({self._coordX}; {self._coordY}) with ability {self.ability()}"

    def wealth_coins_giving(self, gold_coins):  # method for possible giving of coins
        coefficient = random.randint(1, 100)
        success_rate = self.get_wealth_goblin_success_rate()
        wealth_coins_to_give = self.get_wealth_coins_to_give()

        if coefficient <= success_rate:
            gold_coins += wealth_coins_to_give
        return gold_coins

    def health_points_giving(self, health):     # method for possible giving of health points
        coefficient = random.randint(1, 100)
        success_rate = self.get_health_goblin_success_rate()
        health_points_to_give = self.get_health_points_to_give()

        if coefficient <= success_rate:
            health += health_points_to_give
        return health

    def rock_paper_scissors_wealth_coins(self, gold_coins):     # additional method to RPS
        wealth_coins_to_give = self.get_wealth_coins_to_give()
        gold_coins += wealth_coins_to_give
        return gold_coins

    def rock_paper_scissors_health_score(self, health):         # additional method to RPS
        health_points_to_give = self.get_health_points_to_give()
        health += health_points_to_give
        return health

    def rock_paper_scissors(self, coins, health_score):         # RPS method
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
                    print("The gamer goblin choice is ROCK.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")
                elif monster_choice.upper() == "P":
                    print("The gamer goblin choice is PAPER.")
                    result = "LOSE"
                    print(f"You {result}! The gamer goblin wins!")
                else:
                    print("The gamer goblin choice is SCISSORS.")
                    result = "WIN"

                    gold_coins = self.rock_paper_scissors_wealth_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

                    print(f"You {result}!")

            elif symbol_value == 112 or symbol_value == 80:
                print("Your choice is PAPER.")
                if monster_choice.upper() == "R":
                    print("The gamer goblin choice is ROCK.")
                    result = "WIN"

                    gold_coins = self.rock_paper_scissors_wealth_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

                    print(f"You {result}!")

                elif monster_choice.upper() == "P":
                    print("The gamer goblin choice is PAPER.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")
                else:
                    print("The gamer goblin choice is SCISSORS.")
                    result = "LOSE"
                    print(f"You {result}! The gamer monster wins!")

            else:
                print("Your choice is SCISSORS.")
                if monster_choice.upper() == "R":
                    print("The gamer monster choice is ROCK.")
                    result = "LOSE"
                    print(f"You {result}! The gamer monster wins!")

                    gold_coins = self.rock_paper_scissors_wealth_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

                elif monster_choice.upper() == "P":
                    print("The gamer monster choice is PAPER.")
                    result = "WIN"

                    gold_coins = self.rock_paper_scissors_wealth_coins(coins)
                    health = self.rock_paper_scissors_health_score(health_score)

                    print(f"You {result}!")
                else:
                    print("The gamer monster choice is SCISSORS.")
                    result = "DRAW"
                    print(f"It's a {result}! You will play again!\n")

        return gold_coins, health
