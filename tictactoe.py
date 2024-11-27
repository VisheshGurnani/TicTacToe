def display_menu(board):
    for i,row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--+---+--")
        
def x_or_o(): #prompt the user to pick either X or O
    option = 'None'
    while option == 'None':
        player_pick = input("Player 1, X or O? ")
        if player_pick == 'X':
            player1 = 'X'
            player2 = 'O'
            option = 'Done'
        elif player_pick == 'O':
            player1 = 'O'
            player2 = 'X'
            option = 'Done'

    return player1,player2


def position_pick(current_player, player1, player2, board): #Checks which position the user wants to pick
    position_map = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }

    def is_valid_position(pos): #is it valid? is that spot already taken?
        if pos not in position_map:
            return False
        row, col = position_map[pos]
        return board[row][col] == " "

    def get_position_input(): #take the input if valid
        while True:
            pos = input(f"Player {current_player}, pick a position in range (1-9) to place {'X' if player1 == 'X' and current_player == 1 or player2 == 'X' and current_player == 2 else 'O'}: ")
            if is_valid_position(pos):
                return pos
            print("Invalid position or spot already taken. Try again.")

    placed_pos = get_position_input()
    row, col = position_map[placed_pos]
    board[row][col] = 'X' if (player1 == 'X' and current_player == 1) or (player2 == 'X' and current_player == 2) else 'O'

    return board, placed_pos
def check_win(board, player1, player2): #check if X or O is 3 in a row
    def is_winner(mark):
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],

            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],

            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]
        return [mark, mark, mark] in win_conditions

    if is_winner('X'):
        print("Player 1 wins!")
        return True
    if is_winner('O'):
        print("Player 2 wins!")
        return True

    return False
    

def game_loop(): #run the game
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    display_menu(board)
    
    player1, player2 = x_or_o()
    
    current_player = 1
    while True:
        display_menu(board)
        board, _ = position_pick(current_player, player1, player2, board)
        
        if check_win(board, player1, player2):
            display_menu(board)
            break
        
        #check for a draw if all instances are returned, True
        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            display_menu(board)
            break
        
        current_player = 2 if current_player == 1 else 1

game_loop()