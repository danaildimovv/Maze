#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
import sys
import random
from monster import Monster
from goblin import Goblin
import os


class Hero:
    """this is the hero class, further define it please"""
    def __init__(self):
        """set the coordinate of the hero in the maze"""
        self._coordX = random.randint(1, 16)
        self._coordY = random.randint(1, 16)
        self._health = 100
        self._coins = 1000  # gold coins the hero have.
        self._gem = 3

        self.scores = []
        self.names = []

        self.meetings = []

        self.thief_monster = Monster(1)
        self.fighter_monster = Monster(2)
        self.gamer_monster = Monster(3)
        self.random_monster_1 = Monster()
        self.random_monster_2 = Monster()
        self.monsters_initial_positions = [self.thief_monster, self.fighter_monster, self.gamer_monster, self.random_monster_1, self.random_monster_2]

        self.wealth_goblin = Goblin(1)
        self.health_goblin = Goblin(2)
        self.gamer_goblin = Goblin(3)
        self.random_goblin_1 = Goblin()
        self.random_goblin_2 = Goblin()
        self.goblin_initial_positions = [self.wealth_goblin, self.health_goblin, self.gamer_goblin, self.get_random_goblin_1(), self.random_goblin_2]

    def steps_limit(self, plays_number):        # method for limit of the steps
        if plays_number == 100:
            print("You reached the maximum steps limit. You lost the game")
            quit()

    def get_thief_monster(self):        # methods for the monsters
        return self.thief_monster

    def get_fighter_monster(self):
        return self.fighter_monster

    def get_gamer_monster(self):
        return self.gamer_monster

    def get_random_monster_1(self):
        return self.random_monster_1

    def get_random_monster_2(self):
        return self.random_monster_2

    def get_wealth_goblin(self):            # methods for the goblins
        return self.wealth_goblin

    def get_health_goblin(self):
        return self.health_goblin

    def get_gamer_goblin(self):
        return self.gamer_goblin

    def get_random_goblin_1(self):
        return self.random_goblin_1

    def get_random_goblin_2(self):
        return self.random_goblin_2

    def new_initial_position(self):         # methods for hero initial position(s)
        self._coordX = random.randrange(1, 17)
        self._coordY = random.randrange(1, 17)
        return self._coordX, self._coordY

    def initial_position(self):
        return self._coordX, self._coordY

    def decrease_health(self):          # method for decrease health points
        self._health -= 1
        print(f"Health points: {self._health}")

    def show_gold_coins(self):          # method showing gold coins
        print(f"Gold coins: {self._coins}")

    def print_position(self):           # method for printing coordinates
        print(f"The HERO is at position ({self._coordX}; {self._coordY})\n")

    def monster_interaction(self, environment, value_x, value_y):       # method for creature interaction
        check_next = environment.get_coord(self._coordX + value_x, self._coordY + value_y)
        current = environment.get_coord(self._coordX, self._coordY)
        if check_next == 0:
            if current == 3 or current == 4 or current == 5:
                environment.set_coord(self._coordX, self._coordY, current)
                self._coordX += value_x
                self._coordY += value_y
                environment.set_coord(self._coordX, self._coordY, 2)

            else:
                environment.set_coord(self._coordX, self._coordY, 0)
                self._coordX += value_x
                self._coordY += value_y
                environment.set_coord(self._coordX, self._coordY, 2)
        elif check_next == 1:
            self._coordX = self._coordX
            self._coordY = self._coordY
            print("You can not go through the wall.")
        else:
            if check_next == 3:
                if self._coordX + value_x == self.thief_monster.get_coord_x() and self._coordY + value_y == self.thief_monster.get_coord_y():
                    thief = self.thief_monster
                    self.meetings.append("thief")
                elif self._coordX + value_x == self.random_monster_1.get_coord_x() and self._coordY + value_y == self.random_monster_1.get_coord_y():
                    thief = self.random_monster_1
                    self.meetings.append("random 1")
                else:
                    thief = self.random_monster_2
                    self.meetings.append("random 2")

                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)
                remember = self._coordX, self._coordY

                self._coordX += value_x
                self._coordY += value_y

                print(f"The hero meets thief monster with the ability {thief.ability()}, at coordinate ({self._coordX}, {self._coordY}). "
                      f"There will be a fight between them and this means that there is"
                      f" a probability of {thief.get_thief_success_rate()}% for the hero to lose. If he "
                      f"lose, {thief.get_coins_to_steal()} of his gold coins will be stolen by the thief monster!")

                coins_before_fight = self._coins
                self._coins = thief.stealing(self._coins)

                outcome = "lost"
                lost_coins = thief.get_coins_to_steal()
                if coins_before_fight == self._coins:
                    outcome = "won"
                    lost_coins = 0

                print(f"The hero fought with a thief monster at coordinate ({self._coordX}, {self._coordY}) "
                      f"and {outcome} the fight. {lost_coins} gold coins were lost, the current hero's "
                      f"status is (health: {self._health}, coins: {self._coins}).")
                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) behind a monster after"
                      f" an interaction with a"
                      f" thief monster. Choose the hero's next position: ")

            elif check_next == 4:

                if self._coordX + value_x == self.fighter_monster.get_coord_x() and self._coordY + value_y == self.fighter_monster.get_coord_y():
                    fighter = self.fighter_monster
                    self.meetings.append("fighter")
                elif self._coordX + value_x == self.random_monster_1.get_coord_x() and self._coordY + value_y == self.random_monster_1.get_coord_y():
                    fighter = self.random_monster_1
                    self.meetings.append("random 1")
                else:
                    fighter = self.random_monster_2
                    self.meetings.append("random 2")

                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)

                self._coordX += value_x
                self._coordY += value_y

                print(f"The hero meets fighter monster with the ability ({fighter.get_health_to_steal()}, "
                      f"{fighter.get_fighter_success_rate()}%) at coordinate ({self._coordX}, {self._coordY}). "
                      f"There will be a fight between them and this means that there is a probability of "
                      f"{fighter.get_fighter_success_rate()}% for the hero to "
                      f"lose. If he lose the fight, {fighter.get_health_to_steal()} health points of hero's health "
                      f"score will be stolen by the fighter monster!")

                health_before_fight = self._health
                self._health = fighter.fighting(self._health)

                outcome = "lost"
                lost_health = fighter.get_health_to_steal()
                if health_before_fight == self._health:
                    outcome = "won"
                    lost_health = 0

                print(f"The hero fought with a fighter monster at coordinate ({self._coordX}, {self._coordY}) and "
                      f"{outcome} the fight. {lost_health} health points were lost,"
                      f" the current hero's status is (health: {self._health}, coins: {self._coins}).")
                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) behind a monster"
                      f" after a fight against "
                      f"a fighter monster. Choose the hero's next position: ")

            elif check_next == 5:

                if self._coordX + value_x == self.gamer_monster.get_coord_x() and self._coordY + value_y == self.gamer_monster.get_coord_y():
                    gamer = self.gamer_monster
                    self.meetings.append("gamer")
                elif self._coordX + value_x == self.random_monster_1.get_coord_x() and self._coordY + value_y == self.random_monster_1.get_coord_y():
                    gamer = self.random_monster_1
                    self.meetings.append("random 1")
                else:
                    gamer = self.random_monster_2
                    self.meetings.append("random 2")

                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)

                self._coordX += value_x
                self._coordY += value_y

                print(f"The hero meets gamer monster with the ability ({gamer.get_coins_to_steal()}, "
                      f"{gamer.get_health_to_steal()}) at coordinate ({self._coordX}, {self._coordY})."
                      f" There will be a rock-paper-scissors game between them. If the hero loses the game he will lose"
                      f" {gamer.get_coins_to_steal()} gold coins and {gamer.get_health_to_steal()} health points.")

                health_before_game = self._health
                coins_before_game = self._coins

                result = gamer.rock_paper_scissors(self._coins, self._health)
                self._coins = result[0]
                self._health = result[1]

                outcome = "lost"
                lost_coins = gamer.get_coins_to_steal()
                lost_health = gamer.get_health_to_steal()
                if health_before_game == self._health and coins_before_game == self._coins:
                    outcome = "won"
                    lost_coins = 0
                    lost_health = 0

                print(f"The hero played a game of rock-paper-scissors against the gamer monster at coordinate "
                      f"({self._coordX}, {self._coordY}) and {outcome} the fight. {lost_coins} gold "
                      f"coins were lost and {lost_health} health points were lost, the current hero's "
                      f"status is (health: {self._health}, coins: {self._coins}).")

                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) behind a monster"
                      f" after a rock-paper-scissors game "
                      f"against a gamer monster. Choose the hero's next position: ")

            elif check_next == 6:
                if self._coordX + value_x == self.wealth_goblin.get_coord_x() and self._coordY + value_y == self.wealth_goblin.get_coord_y():
                    wealth_goblin = self.wealth_goblin
                elif self._coordX + value_x == self.random_goblin_1.get_coord_x() and self._coordY + value_y == self.random_goblin_1.get_coord_y():
                    wealth_goblin = self.random_goblin_1
                else:
                    wealth_goblin = self.random_goblin_2

                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)

                self._coordX += value_x
                self._coordY += value_y
                environment.set_coord(self._coordX, self._coordY, 2)

                print(f"The hero meets wealth goblin with the ability {wealth_goblin.ability()} at coordinate "
                      f"({self._coordX}, {self._coordY}). "
                      f"This means that the hero has a chance of {wealth_goblin.get_wealth_goblin_success_rate()}% "
                      f"to win {wealth_goblin.get_wealth_coins_to_give()} gold coins.")

                coins_before_meeting = self._coins
                self._coins = wealth_goblin.wealth_coins_giving(self._coins)

                outcome = "lucky"
                won_coins = wealth_goblin.get_wealth_coins_to_give()
                if coins_before_meeting == self._coins:
                    outcome = "not lucky"
                    won_coins = 0

                print(f"The hero met a wealth goblin at coordinate ({self._coordX}, {self._coordY}). The hero was"
                      f"{outcome} and won {won_coins} coins after the meeting. The current hero's status is (health: "
                      f"{self._health}, coins: {self._coins})")

                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) after an interaction with a"
                      f" wealth goblin. Choose the hero's next position: ")

            elif check_next == 7:
                if self._coordX + value_x == self.health_goblin.get_coord_x() and self._coordY + value_y == self.health_goblin.get_coord_y():
                    health_goblin = self.health_goblin
                elif self._coordX + value_x == self.random_goblin_1.get_coord_x() and self._coordY + value_y == self.random_goblin_1.get_coord_y():
                    health_goblin = self.random_goblin_1
                else:
                    health_goblin = self.random_goblin_2
                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)
                self._coordX += value_x
                self._coordY += value_y
                environment.set_coord(self._coordX, self._coordY, 2)

                print(f"The hero meets health goblin with the ability {health_goblin.ability()} at coordinate ({self._coordX}, {self._coordY}). "
                      f"This means that the hero has a chance of {health_goblin.get_health_goblin_success_rate()}% to win "
                      f"{health_goblin.get_health_points_to_give()} health points.")

                health_before_meeting = self._health
                health_won = health_goblin.get_health_points_to_give()
                self._health = health_goblin.health_points_giving(self._health)

                outcome = "lucky"
                if health_before_meeting == self._health:
                    outcome = "unlucky"
                    health_won = 0

                print(f"The hero met a health goblin at coordinate ({self._coordX}, {self._coordY}). The hero was "
                      f"{outcome} and won {health_won} health points after the meeting. The current hero's status is "
                      f"(health: {self._health}, coins: {self._coins}).")

                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) after an interaction with a"
                      f" health goblin. Choose the hero's next position: ")

            elif check_next == 8:
                if self._coordX + value_x == self.gamer_goblin.get_coord_x() and self._coordY + value_y == self.gamer_goblin.get_coord_y():
                    gamer_goblin = self.gamer_goblin
                elif self._coordX + value_x == self.random_goblin_1.get_coord_x() and self._coordY + value_y == self.random_goblin_1.get_coord_y():
                    gamer_goblin = self.random_goblin_1
                else:
                    gamer_goblin = self.random_goblin_2
                if current == 3 or current == 4 or current == 5:
                    environment.set_coord(self._coordX, self._coordY, current)
                else:
                    environment.set_coord(self._coordX, self._coordY, 0)
                self._coordX += value_x
                self._coordY += value_y
                environment.set_coord(self._coordX, self._coordY, 2)

                print(f"The hero meets gamer goblin with the ability {gamer_goblin.ability()} at coordinate"
                      f" ({self._coordX}, {self._coordY}). "
                      f"This means that they will play a rock-paper-scissors game and if the hero wins the game "
                      f"he will win"
                      f" {gamer_goblin.get_wealth_coins_to_give()} gold coins and"
                      f"{gamer_goblin.get_health_points_to_give()} health points.")

                coins_before_game = self._coins
                health_before_game = self._health
                won_coins = gamer_goblin.get_wealth_coins_to_give()
                won_health = gamer_goblin.get_health_points_to_give()
                result = gamer_goblin.rock_paper_scissors(self._coins, self._health)
                self._coins = result[0]
                self._health = result[1]

                outcome = "won"
                if coins_before_game == self._coins and health_before_game == self._health:
                    outcome = "didn't won"
                    won_coins = 0
                    won_health = 0

                print(f"The hero played a rock-paper-scissors game against a gamer goblin at coordinate "
                      f"({self._coordX}, {self._coordY}). The hero {outcome} the game and won {won_coins} coins and "
                      f"{won_health} health points. The current hero's status is (health: {self._health}, coins "
                      f"{self._coins}).")

                print(f"Now the hero stays at position ({self._coordX}; {self._coordY}) after an interaction with a"
                      f" health goblin. Choose the hero's next position: ")

            else:
                environment.print_environment()
                print("You cannot go trough the wall!\n==============================\nChoose new position\n"
                      "===================================================\n")

    def checking_options(self, direction, direction_text, checking_options):        # method for available options
        if direction == 0:
            checking_options.append(f"{direction_text}- FREE SPACE: NO WORRIES")
        elif direction == 3:
            checking_options.append(f"{direction_text}- THIEF MONSTER: YOU CAN LOSE GOLD COINS!")
        elif direction == 4:
            checking_options.append(f"{direction_text}- FIGHTER MONSTER: YOU CAN LOSE HEALTH POINTS!")
        elif direction == 5:
            checking_options.append(f"{direction_text}- GAMER MONSTER: YOU CAN LOSE BOTH GOLD COINS AND HEALTH POINTS!")
        elif direction == 6:
            checking_options.append(f"{direction_text}- WEALTH GOBLIN: YOU CAN WIN GOLD COINS!")
        elif direction == 7:
            checking_options.append(f"{direction_text}- HEALTH GOBLIN: YOU CAN WIN HEALTH POINTS!")
        elif direction == 8:
            checking_options.append(f"{direction_text}- GAMER GOBLIN: YOU CAN WIN BOTH GOLD COINS AND HEALTH POINTS!")

    def move(self, environment):
        """move in the maze, it is noted this function may not work in the debug mode"""
        ch2 = getch()
        if ch2 == b'H' or ch2 == "A":
            # the up arrow key was pressed
            os.system("cls")
            print("UP KEY PRESSED")
            self.monster_interaction(environment, -1, 0)
            return True

        elif ch2 == b'P' or ch2 == "B":
            # the down arrow key was pressed
            os.system("cls")
            print("DOWN KEY PRESSED")
            self.monster_interaction(environment, 1, 0)
            return True

        elif ch2 == b'K' or ch2 == "D":
            # the left arrow key was pressed
            os.system("cls")
            print("LEFT KEY PRESSED")
            self.monster_interaction(environment, 0, -1)
            return True

        elif ch2 == b'M' or ch2 == "C":
            # the right arrow key was pressed
            os.system("cls")
            print("RIGHT KEY PRESSED")
            self.monster_interaction(environment, 0, 1)
            return True

        elif ord(ch2) == 109 or ord(ch2) == 77:                           # checks for m
            os.system("cls")
            print(f"The HERO is at position ({self._coordX}, {self._coordY})\n")

            print("MONSTERS: ")
            for monster in self.monsters_initial_positions:
                monster_positions = monster.print_position()
                print(monster_positions)

            print("\n")

            print("GOBLINS: ")
            for goblin in self.goblin_initial_positions:
                goblin_positions = goblin.print_position()
                print(goblin_positions)
            return True

        elif ord(ch2) == 27:                           # checks for escape to quit
            os.system("cls")
            quit()
        elif ord(ch2) == 104 or ord(ch2) == 72:
            check_left = environment.get_coord(self._coordX, self._coordY - 1)
            check_right = environment.get_coord(self._coordX, self._coordY + 1)
            check_up = environment.get_coord(self._coordX - 1, self._coordY)
            check_down = environment.get_coord(self._coordX + 1, self._coordY)
            options = []
            printing_options = "\n                       "

            if check_left != 1:
                self.checking_options(check_left, "GOING LEFT(LEFT ARROW)", options)

            if check_right != 1:
                self.checking_options(check_right, "GOING RIGHT(RIGHT ARROW)", options)

            if check_up != 1:
                self.checking_options(check_up, "GOING UP(UP ARROW)", options)

            if check_down != 1:
                self.checking_options(check_down, "GOING DOWN(DOWN ARROW)", options)

            printing_options = printing_options.join(options)
            print(f"You have {len(options)} option(s): ", printing_options)

        if self._health <= 0:
            print("Your health score is less than or equal to zero. You lost the game!")
            quit()
        if "thief" in self.meetings and "fighter" in self.meetings and \
                "gamer" in self.meetings and "random 1" in self.meetings and "random 2" in self.meetings:
            print("The hero met all the monsters at least once. ")
            if self._health > 0:
                print("It was a successful game!")
                score = self._coins
                name = input("Please write your name to record your result: ")

                self.scores.append(score)
                self.scores.sort()

                self.names.append(name)
                print("Result: \n")
                for i in range(len(self.scores)):
                    print(f"{self.names[i]}|{str(self.scores[i])} points")

                quit()
            else:
                print("You lost the game. You won't be recorded in the league table.")
                quit()
        return False

    def move_debug(self, environment):

        """move in the maze, you need to press the enter key after keying in
        direction, and this works in the debug mode"""

        ch2 = sys.stdin.read(1)

        if ch2 == "w":
            # the up arrow key was pressed
            print("up key pressed")
            return True

        elif ch2 == "s":
            # the down arrow key was pressed
            print("down key pressed")
            return True

        elif ch2 == "a":
            # the left arrow key was pressed
            print("left key pressed")
            return True

        elif ch2 == "d":
            # the right arrow key was pressed
            print("right key pressed")
            return True

        return False


