from IPython.display import clear_output

def display_board(board):
    # print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')
    clear_output()

def player_input():
    xoubola = ''

    while not (xoubola == 'X' or xoubola == 'O'):
        xoubola = input('Player X ou O?: ').upper()
    if xoubola == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, xoubola, position):
    board[position] = xoubola
    

def win_check(board, xoubola):
    return(  
    (board[9] == xoubola and board [8] == xoubola and board [7] == xoubola) or #vitória por cima
    (board[6] == xoubola and board [5] == xoubola and board [4] == xoubola) or #vitória por meio
    (board[3] == xoubola and board [2] == xoubola and board [1] == xoubola) or #vitória por baixo
    (board[1] == xoubola and board [4] == xoubola and board [7] == xoubola) or #Vitória por esquerda
    (board[3] == xoubola and board [6] == xoubola and board [9] == xoubola) or #Vitória por direita
    (board[7] == xoubola and board [5] == xoubola and board [3] == xoubola) or #vitória Diagonal esquerda p direita
    (board[9] == xoubola and board [5] == xoubola and board [1] == xoubola) or #vitória Diagonal direita p esquerda
    (board[8] == xoubola and board [5] == xoubola and board [2] == xoubola))  #vitoria pelo meio vertical

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9): ')
    return int(position)

def replay():
    return input('Quer jogar novamente? SIM ou NÃO: ').lower().startswith('s')

print('Bem vindo ao jogo da velha')

while True:
    theboard = [' '] * 10
    turn = choose_first()
    print(turn + ' Começa!')
    player1_xoubola, player2_xoubola = player_input()
    game_on = True

    while game_on:
        #Jogador 1
        
        if turn == 'Player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player1_xoubola, position)
            
        
        #Checa vitoria
        if win_check(theboard, player1_xoubola):
            display_board(theboard)
            print('Parabéns! Você venceu')
            game_on = False
        else:
            if full_board_check(theboard):
                display_board(theboard)
                print('Empate :|')
                break
            else:
                turn = 'Player 2'

    #Jogador 2
        
        if turn == 'Player 2':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player2_xoubola, position)
            
        
        #Checa vitoria
        if win_check(theboard, player2_xoubola):
            display_board(theboard)
            print('Parabéns! Você venceu')
            game_on = False
        else:
            if full_board_check(theboard):
                display_board(theboard)
                print('Empate :|')
                break
            else:
                turn = 'Player 1'
    if not replay():
        break