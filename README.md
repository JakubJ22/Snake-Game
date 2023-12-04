# Snake Game
This is a simple Snake Game built using Python's Turtle module. It was created for learning and training OOP.
The game consists of several components:
## Components
### 1. Food
#### File: food.py
#### Description: This module creates food for the snake to eat.
#### Attributes:
###### Shape: Circle
###### Color: Blue
#### Methods:
show_on_screen(): Randomizes the position of the food on the screen.
### 2. Snake
File: snake.py
Description: Defines the snake and its functionalities.
Attributes:
Initially consists of 3 segments.
Methods:
create_snake(): Creates a snake from segments.
extend_snake(): Extends the snake by adding a new segment.
move(): Moves the snake according to specified directions.
up(), down(), right(), left(): Changes the direction of the snake.
### 3. Score Board
File: score_board.py
Description: Manages and displays the game score.
Attributes:
Shows the player's score and the best score achieved.
Methods:
give_score(): Displays the current score.
counting(): Provides a countdown before starting the game.
exit_info(): Displays instructions on how to start a new game or close the window.
game_over(): Shows "GAME OVER" on the screen and updates the best score.
update_best_score(): Updates the best score if the current score exceeds it.
give_best_score(): Displays the best score achieved.
### 4. Main
File: main.py
Description: Contains the main game loop and integrates all components.
Functions:
game_on(): Initializes the game by setting up the screen and binding keys for movement.
next_round(): Allows starting a new game by pressing the spacebar.
Game Loop:
Controls the movement of the snake, checks collisions, updates the score, and handles game-over scenarios.

### How to Play
Run main.py.
Enter your name in the prompt window to start the game.
Control the snake's direction using the arrow keys or 'WASD'.
Collect food to increase your score.
Avoid collisions with walls or the snake's own tail.
Press 'Space' to start a new game or 'Escape' to close the window.
Have fun playing the Snake Game!