# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

boardd = {'TL',' ', 'TM',' ', 'TR',' ', 'ML',' ', 'MM',' ', 'MR',' ', 'BL',' ', 'BM',' ', 'BR',' '}

def tictactoe(boardd):
    print((boardd['TL']) + "|" + (boardd['TM']) + "|" + (boardd['TL']))
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")

tictactoe(boardd)
