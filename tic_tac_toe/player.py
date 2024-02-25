import random

class Player:
    """Base class for Tic Tac Toe players."""
    def __init__(self, letter):
        """Initialize the player with a given letter."""
        self.letter = letter

    def get_move(self, game):
        """Get the player's move."""
        pass

class RandomComputerPlayer(Player):
    """A Tic Tac Toe player that makes random moves."""
    def get_move(self, game):
        """Get a random available move."""
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    """A Tic Tac Toe player that takes input from the human user."""
    def get_move(self, game):
        """Get the human player's move."""
        valid_square = False

        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError("Invalid square. Please enter a number between 0 and 8.")
                
                valid_square = True
            
            except ValueError as e:
                print(e)

        return val