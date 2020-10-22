# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

board = {'TL',' ', 'TM',' ', 'TR',' ', 'ML',' ', 'MM',' ', 'MR',' ', 'BL',' ', 'BM',' ', 'BR',' '}

def tictactoe(board):
    print((board['TL']) + "|" + (board['TM']) + "|" + (board['TL']))
    print("-+-+-")
    print((board['ML']) + "|" + (board['MM']) + "|" + (board['ML']))
    print("-+-+-")
    print((board['BL']) + "|" + (board['BM']) + "|" + (board['BR']))

tictactoe(board)
options = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']

a = str(input(print("Player One, where would you like to place your first X? Your options are " + options + " : ")))
if a == 'TL':
    board.update({'TL':'X'})
if a == 'TM':
    board.update({'TM':'X'})
if a == 'TR':
    board.update({'TR':'X'})
if a == 'ML':
    board.update({'ML':'X'})
if a == 'MM':
    board.update({'MM':'X'})
if a == 'MR':
    board.update({'MR':'X'})
if a == 'BL':
    board.update({'BL':'X'})
if a == 'BM':
    board.update({'BM':'X'})
if a == 'BR':
    board.update({'BR':'X'})

options.remove(a)

tictactoe(board)

