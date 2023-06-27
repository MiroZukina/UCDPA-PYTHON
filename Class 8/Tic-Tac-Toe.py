

board = [[' ' for _ in range(3)] for _ in range(3)]


def display_board():
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')


def check_win(player):
  
    for row in board:
        if all(cell == player for cell in row):
            return True


    for col in range(3):
        if all(row[col] == player for row in board):
            return True

  
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()

        row = int(input("Player {}, enter the row number (0-2): ".format(current_player)))
        col = int(input("Player {}, enter the column number (0-2): ".format(current_player)))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_win(current_player):
            display_board()
            print("Player", current_player, "wins!")
            game_over = True
    
        elif check_draw():
            display_board()
            print("It's a draw!")
            game_over = True
    
        else:
            current_player = 'O' if current_player == 'X' else 'X'
play_game()
