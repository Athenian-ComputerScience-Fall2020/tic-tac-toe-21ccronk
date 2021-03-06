# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Megan
#  I asked Ryan a question at one point
# A note on style: Dictionaries can be defined before or after functions.

board = {'TL':' ', 'TM':' ', 'TR':' ', 'ML':' ', 'MM':' ', 'MR':' ', 'BL':' ', 'BM':' ', 'BR':' '}
options = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']
x = 0


def tictactoe(board):
    print((board['TL']) + "|" + (board['TM']) + "|" + (board['TR']))
    print("-+-+-")
    print((board['ML']) + "|" + (board['MM']) + "|" + (board['MR']))
    print("-+-+-")
    print((board['BL']) + "|" + (board['BM']) + "|" + (board['BR']))


def winner(board, x):
    if board['TL'] == board['TM'] == board['TR']:
        if board['TL'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TL'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['ML'] == board['MM'] == board['MR']:
        if board['ML'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['ML'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['BL'] == board['BM'] == board['BR']:
        if board['BL'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['BL'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['TL'] == board['ML'] == board['BL']:
        if board['TL'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TL'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['TM'] == board['MM'] == board['BM']:
        if board['TM'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TM'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['TR'] == board['MR'] == board['BR']:
        if board['TR'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TR'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['TL'] == board['MM'] == board['BR']:
        if board['TL'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TL'] == 'O':
            print("Player Two Wins")
            x = x + 1
    if board['TR'] == board['MM'] == board['BL']:
        if board['TR'] == 'X':
            print("Player One Wins")
            x = x + 1
        elif board['TR'] == 'O':
            print("Player Two Wins")
            x = x + 1
    return x

def playeroneturn(board, options):
    print("Player One, where would you like to place an X? Your options are " , options , " : ")
    a = input()
    if a in options:
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
        return True
    
    elif a not in options: 
        print("That space is not valid. Please try again.")
        return False

def playertwoturn(board, options):
    print("Player Two, where would you like to place an O? Your options are " , options , " : ")
    a = input()
    if a in options:
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
        return True
        
    elif a not in options: 
        print("That space is not valid. Please try again.")
        return False




tictactoe(board)
while x < 1:
    y = playeroneturn(board, options)
    while y == False:
        y = playeroneturn(board,options)
    y = playertwoturn(board, options)
    while y == False:
        y = playertwoturn(board,options)
    y = playeroneturn(board, options)
    while y == False:
        y = playeroneturn(board,options)
    y = playertwoturn(board, options)
    while y == False:
        y = playertwoturn(board,options)
    y = playeroneturn(board, options)
    while y == False:
        y = playeroneturn(board,options)
    x = winner(board,x) 
    if x > 0:
        break
    y = playertwoturn(board, options)
    while y == False:
        y = playertwoturn(board,options)
    x = winner(board,x)
    if x > 0:
        break
    y = playeroneturn(board, options)
    while y == False:
        y = playeroneturn(board,options)
    x = winner(board,x)
    if x > 0:
        break
    y = playertwoturn(board, options)
    while y == False:
        y = playertwoturn(board,options)
    x = winner(board,x)
    if x > 0:
        break
    y = playeroneturn(board, options)
    while y == False:
        y = playeroneturn(board,options)
    x = winner(board,x)
    if x > 0:
        break
    print("No one won this game")
    break






