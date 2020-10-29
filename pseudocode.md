
# Functions
- tictactoe()
    this function creates and keeps track of the board structure
- winner()
    this function keeps track if there is a winner
- playeroneturn()
    this function prompts player one to play, and adds their value to the dictionary
- playertwoturn()
    this function prompts player two to play, and adds their value to the dictionary

# Pre-defined Values
- board
    board is the dictionary that keeps track of where X's and O's are placed
- options
    options is a dictionary that keeps track of which spaces are a valid input for the next player
- x = 0
    x exists to keep track of when there is a winner. if there is a winner, x = 1, and the game should break out of its while loop

# Breakdown
- tictactoe board is printed
- player one is prompted to change the value of one key in the dictionary, to place their X
- player two is prompted, restricted by options
- ...
- after 5 turns, their is a chance of a winner, so winner function is called
    - if a winner exists, the game will print so, and quit
    - if a winner does not exist, the game will carry on
- ...
- if no winner exists by the end of 9 turns, the game will print so, and end


