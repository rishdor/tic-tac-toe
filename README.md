# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game using Python and Tkinter.

## Features

- Customizable board size and win condition.
- Graphical user interface using Tkinter.
- Scoreboard to keep track of wins for each player.

## Classes

- `Scoreboard`: This class handles the scoreboard display and updates.
- `GameFlow`: This class handles the game logic and user interface.

## Usage

To start a game, create an instance of the `GameFlow` class and call the `start_game` method:

```python
game = GameFlow(size=5, win_length=3)
game.start_game()
```

In this example, size=5 sets the size of the board to 5x5, and win_length=3 sets the win condition to 3 consecutive symbols.

## Future Improvements

* Add AI opponent.
* Add multiplayer support over network.
