# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

board = {'TL':' ', 'TM':' ', 'TR':' ', 'ML':' ', 'MM':' ', 'MR':' ', 'BL':' ', 'BM':' ', 'BR':' '}

def tictactoe(board):
    print((board['TL']) + "|" + (board['TM']) + "|" + (board['TR']))
    print("-+-+-")
    print((board['ML']) + "|" + (board['MM']) + "|" + (board['MR']))
    print("-+-+-")
    print((board['BL']) + "|" + (board['BM']) + "|" + (board['BR']))

def winner(board):
    if board['TL'] == board['TM'] == board['TR']:
        if board['TL'] == 'X':
            print("Player One Wins")
        if board['TL'] == 'O':
            print("Player Two Wins")

def playeroneturn(board):

def playertwoturn(board):

tictactoe(board)
options = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']

print("Player One, where would you like to place your first X? Your options are " , options , " : ")
a = input()
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

print("Player Two, where would you like to place your first O? Your options are " , options , " : ")
a = input()
if a == 'TL':
    board.update({'TL':'O'})
if a == 'TM':
    board.update({'TM':'O'})
if a == 'TR':
    board.update({'TR':'O'})
if a == 'ML':
    board.update({'ML':'O'})
if a == 'MM':
    board.update({'MM':'O'})
if a == 'MR':
    board.update({'MR':'O'})
if a == 'BL':
    board.update({'BL':'O'})
if a == 'BM':
    board.update({'BM':'O'})
if a == 'BR':
    board.update({'BR':'O'})

options.remove(a)

tictactoe(board)

print("Player One, where would you like to place your next X? Your options are " , options , " : ")
a = input()
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

print("Player Two, where would you like to place your next O? Your options are " , options , " : ")
a = input()
if a == 'TL':
    board.update({'TL':'O'})
if a == 'TM':
    board.update({'TM':'O'})
if a == 'TR':
    board.update({'TR':'O'})
if a == 'ML':
    board.update({'ML':'O'})
if a == 'MM':
    board.update({'MM':'O'})
if a == 'MR':
    board.update({'MR':'O'})
if a == 'BL':
    board.update({'BL':'O'})
if a == 'BM':
    board.update({'BM':'O'})
if a == 'BR':
    board.update({'BR':'O'})

options.remove(a)

tictactoe(board)

print("Player One, where would you like to place your next X? Your options are " , options , " : ")
a = input()
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

winner(board)

print("Player Two, where would you like to place your next O? Your options are " , options , " : ")
a = input()
if a == 'TL':
    board.update({'TL':'O'})
if a == 'TM':
    board.update({'TM':'O'})
if a == 'TR':
    board.update({'TR':'O'})
if a == 'ML':
    board.update({'ML':'O'})
if a == 'MM':
    board.update({'MM':'O'})
if a == 'MR':
    board.update({'MR':'O'})
if a == 'BL':
    board.update({'BL':'O'})
if a == 'BM':
    board.update({'BM':'O'})
if a == 'BR':
    board.update({'BR':'O'})

options.remove(a)

tictactoe(board)

print("Player One, where would you like to place your next X? Your options are " , options , " : ")
a = input()
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

print("Player Two, where would you like to place your next O? Your options are " , options , " : ")
a = input()
if a == 'TL':
    board.update({'TL':'O'})
if a == 'TM':
    board.update({'TM':'O'})
if a == 'TR':
    board.update({'TR':'O'})
if a == 'ML':
    board.update({'ML':'O'})
if a == 'MM':
    board.update({'MM':'O'})
if a == 'MR':
    board.update({'MR':'O'})
if a == 'BL':
    board.update({'BL':'O'})
if a == 'BM':
    board.update({'BM':'O'})
if a == 'BR':
    board.update({'BR':'O'})

options.remove(a)

tictactoe(board)

print("Player One, where would you like to place your next X? Your options are " , options , " : ")
a = input()
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

