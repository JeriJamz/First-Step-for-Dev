import pprint

theBoard = {'top-L':'','top-M':'','top-R':'','mid-L':'','mid-M':'','mid-R':'','low-L':'','low-M':'','low-R':''}

def printBoard(board):
    print(board['top-L'] +  '|'  + board['top-M'] +  '|'  + board['top-R'])
    print('-----')
    print(board['mid-L'] +  '|'  + board['mid-M'] +  '|'  + board['mid-R'])
    print('-----')
    print(board['low-L'] +  '|'  + board['low-M'] +  '|'  + board['low-R'])


#call the tik tak toe board by using n/ printBorad(theBoard)

print('This is only the data structure for a Tic-Tac-Toe board \n to print the board type "printBoard(theBoard)"')

printBoard(theBoard)
