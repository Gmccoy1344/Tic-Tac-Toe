board = ['_'] * 9
first = True
second = True
game = True
game_played = True
count = 0
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def check():
    top = board[0] + board[1] + board[2]
    middle = board[3] + board[4] + board[5]
    bottom = board[6] + board[7] + board[8]
    left = board[0] + board[3] + board[6]
    up_mid = board[1] + board[4] + board[7]
    right = board[2] + board[5] + board[8]
    diag_l = board[0] + board[4] + board[8]
    diag_r = board[2] + board[4] + board[6]

    if top == 'XXX' or top == 'OOO':
        return True
    elif middle == 'XXX' or middle == 'OOO':
        return True
    elif bottom == 'XXX' or bottom == 'OOO':
        return True
    elif left == 'XXX' or left == 'OOO':
        return True
    elif up_mid == 'XXX' or up_mid == 'OOO':
        return True
    elif right == 'XXX' or right == 'OOO':
        return True
    elif diag_l == 'XXX' or diag_l == 'OOO':
        return True
    elif diag_r == 'XXX' or diag_r == 'OOO':
        return True

def check_moves():
    if count == 9:
        return True


print('Tic Tac Toe!')
print('This a game you play against another player to get 3 O\'s or X\'s in a row!')
print('In order to play this game you must choose which spot to place your symbol')
print('The board is numbered from 1 - 9 starting from the the top of the board ending at 9 in the bottom right of the board')
print('The first player will be X and the second player will be O')

while game_played == True:
    while game == True:
        
        while first == True:
            print_board()
            x = int(input('Player1\'s turn: '))
            x = x - 1
            if 0 > x > 8:
                print('Spot does not exist on board')
                continue
            if (0 <= x <= 8) and (board[x] == '_'):
                board[x] = 'X'
                count += 1
                check()
                check_moves()

                if check() == True:
                    print('\n'*30)
                    print_board()
                    print('Player1 Wins!')
                    game = False
                    break

                if check_moves() == True:
                    game = False
                    break

                first = False
                second = True
                print('\n'*30)
            else:
                print('That spot is taken')
            

        while second == True:
            print_board()
            o = int(input('Player2\'s turn: '))
            o = o - 1
            if 0 > o > 8:
                print('Spot does not exist on board')
      
            if (0 <= o <= 8) and (board[o] == '_'):
                board[o] = 'O'
                count += 1
                check()
                check_moves()

                if check() == True:
                    print('\n'*30)
                    print_board()
                    print('Player2 Wins!')
                    game = False
                    break

                if check_moves() == True:
                    game = False
                    break

                second = False
                first = True
                print('\n'*30)
            else:
                print('That spot is taken')

    answer = str(input('Play again?'))
    if (answer == 'Yes' or answer == 'yes'):
        board = ['_'] * 9
        count = 0
        game = True

                
    elif(answer == 'No' or answer == 'no'):
        game = False
        game_played = False 
        
          