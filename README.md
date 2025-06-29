# Tic-Tac-Toe

A modern, standalone desktop Tic-Tac-Toe game built with Python and Tkinter. Play against another human or challenge an AI with three difficulty levels. Packaged as a one-file Windows executable for easy distribution.

## Features

* **Single Player vs. Computer**

  * Three difficulty levels: Easy (random moves), Medium (mixed random/optimal), Hard (minimax algorithm).
  * AI move delay and board highlight on win/draw.
* **Two-Player Mode**

  * Local multiplayer with alternating turns.
* **Customizable First Move**

  * Choose who starts each game (Player/X always starts by default).
* **Game Over Dialog**

  * Shows result, highlights the winning line, and lets you pick who starts next before restarting.
* **Scoreboard**

  * Tracks wins for each side across games without resetting on restart.
* **Modern UI**

  * Dark-themed color scheme, hover effects, centered window, and custom fonts.
* **Standalone Executable**

  * Packaged via PyInstaller to produce a single `.exe` (no Python install required).

## Installation

 Clone the repository using command prompt:

   ```bash
   git clone https://github.com/PS-RANASINGHE/TIC_TAC_TOE-application-game
   ```
Or

+ Go to the Repo `https://github.com/PS-RANASINGHE/TIC_TAC_TOE-application-game/tree/main`
+ Click on the `Code` button which is in green colour
+ Click on `Download Zip`
+ Unzip the file
+ Enjoy the play 

## Usage

Double-click the generated executable (`dist/game_tic_tac_toe.exe`).


## Code Overview

The main logic resides in `game_tic_tac_toe.py`, centered around the `TicTacToe` class:

* **Initialization (`__init__`)**

  * Sets up the Tkinter window, game state variables, board matrix, and UI buttons.
* **Menus**

  * **Main Menu**: Choose Single Player or Two Players.
  * **Symbol & Order Menu**: Pick X or O and who goes first; select AI difficulty when in single-player mode.
* **Board Creation (`create_board`)**

  * Builds a 3×3 grid of Tkinter Buttons with hover effects and binds click events.
* **Move Handling (`make_move`, `computer_move`, `place_and_check`)**

  * Enforces turn order, prevents invalid clicks, places symbols, and updates the board.
  * **AI (`computer_move`)**: Chooses a move based on selected difficulty, using the Minimax algorithm for optimal play.
* **Game End (`end_game`)**

  * Highlights the winning line, shows a dialog with the result, and presents options to restart or return to menu. Also lets you pick the next starting player.
* **Restart Logic (`restart_game`)**

  * Resets the board but preserves scores and applies the user’s chosen starter for the next round.

### Minimax Algorithm

The AI’s Hard difficulty uses a classic minimax recursion:

1. **Terminal Check**: Return +1 if the computer has won, -1 if the player has won, and 0 on draw.
2. **Maximizing** (Computer’s turn): Explore all empty cells, recursively evaluate, and choose the move with the highest score.
3. **Minimizing** (Player’s turn): Similarly, choose the move with the lowest score.


## Acknowledgments

* Built with Python’s built-in Tkinter GUI toolkit.
* Minimax algorithm inspired by classical AI tutorials.

## Unit Test

Created unit test to test the functionality of the game. The results are as follows. The tests are mentioned in the file `unittest_tictactoe.py`


```bash

PS D:\pycharm installed\procject\.venv\Scripts> python .\test_tictactoe.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.005s

OK
```


## Game play 
https://github.com/user-attachments/assets/9a4518c7-ed5b-4147-b103-64fc40909a7f







