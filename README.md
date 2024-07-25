# Pong Wars

Pong Wars is a simple game created using Pygame, where two balls compete to capture squares on a grid. The game features a day and night theme, with each ball representing a different time of day.

## Features

- Two balls, one representing day and the other representing night, bounce around the screen
- The balls change the color of the squares they touch to their respective color
- The score is displayed in the top-left corner, showing the number of squares captured by each ball
- The balls bounce off the walls and each other, with some randomness added to the bounce

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install Pygame using pip:
   ```
   pip install pygame
   ```

## Usage

1. Save the provided code in a file with a `.py` extension, for example, `pong_wars.py`.
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using the following command:
   ```
   python pong_wars.py
   ```
4. The game window will open, and you can watch the balls compete to capture squares.
5. The game will continue running until you close the window.

## Controls

There are no user controls in this version of the game. The balls move automatically, and the game ends when you close the window.

## Customization

You can customize the game by modifying the following variables in the code:

- `screen_width` and `screen_height`: Change the size of the game window.
- `SQUARE_SIZE`: Adjust the size of the squares on the grid.
- `DAY_COLOR` and `NIGHT_COLOR`: Modify the colors used for the day and night themes.
- `DAY_BALL_COLOR` and `NIGHT_BALL_COLOR`: Change the colors of the day and night balls.
- `dx1`, `dy1`, `dx2`, and `dy2`: Adjust the initial velocities of the balls.
