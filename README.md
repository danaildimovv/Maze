# Maze

The maze is a game presented in the terminal with characters. In the game a hero will explore the maze, fighting with monsters and interacting with goblins. First, a maze with size 17 * 17 s is randomly generated and positions of the hero, 5 s monsters and 5 goblins are randomly generated. The hero is represented by the symbol “H”, the monsters by “M” and the goblins by “G”. The maze is closed with no entrance and exit. The “#” symbol represents the walls, whereas the “-“ is for the free spaces. The initial positions of the hero, the monsters and the goblins are displayed with the maze in the beginning of the game.
There is only one hero in the game. You can move him by using the keyboard arrows: up, down, left and right. The hero cannot go through the walls and if he tries to do it he stays at the same position.
There are three types of monsters – thief, fighter and gamer monster, and three types of goblins – wealth, health and gamer goblin, all with various abilities, which are random generated in a particular range of numbers. For example a thief number can have an ability (45, 90%) which means that he will steal 45 gold coins from the hero with a success rate of 90%. Before and after each interaction between the hero and the monsters and the goblins there is a message displayed in the terminal.
The monsters are the hero enemies and the only can steal from him. After a fight with a monster the hero is at the same position and stays behind the monster, so he cannot be seen in that moment. In spite of this, his coordinates are displayed on the screen – he can be easily found.
The goblins are hero’s friends and they can give him some coins or health points. After an interaction with a goblin, it will disappear (the goblin).
The hero starts with 100 health points and 1000 gold coins. He dies if the health points drop to zero. He wins if he meets all the monsters at least once and still survives – having health points more than zero.
The main purpose of the game is to find the right strategy in order to win as many gold coins possible and lose as little health score as possible!


# Run Instructions

Navigate to the game directory and run "python playgame.py" in the console
Enjoy !
