# Reversi (Othello) game
Implementation of Reversi console game in python with an AI player that is developed by Minimax algorithm.


## About Reversi
There are sixty-four identical game pieces called disks, which are light on one side and dark on the other. Players take turns placing disks on the board with their assigned color facing up. During a play, any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color. The objective of the game is to have the majority of disks turned to display one's color when the last playable empty square is filled [[Wiki](https://en.wikipedia.org/wiki/Reversi)].

<p align='center'>
  <img height="250" alt="genetic-example" src="README.imgs/board-image.jpg">
</p>


## Project structure
- ### 📂 directory [reversi_game]
    - #### 📄 file [base_reversi.py]
      This file contains `Reversi` class which is a model that implements all functionalities needed for the game independent of the user interface.
  
    - #### 📄 file [player.py]
      This file contains `Player` _abstract_ class which is the base class for any player in the game. 

    - #### 📄 file [player_ai.py]
      This file contains `AIPlayer` class that inherited from `Player` class. It uses **Minimax** algorithm to provide an action for player. 

    - #### 📄 file [player_human.py]
      This file contains `HumanPlayer` class that inherited from `Player` class. It uses console interface and asks for an action.

    - #### 📄 file [reversi_console.py]
      This file contains `ReversiConsoleUI` class which uses player classes and `Reversi` class to implement a console based reversi game. This class controls the flow of game and ask players for action. 

- ### 📄 file [main.py]
  These file is the starting point of game. This will start console game by asking for mode of game and the color of human player:

<p align='center'>
  <img width="300" alt="genetic-example" src="README.imgs/start.png">
</p>
