#Tic-Tac-Toe Game
#Cecelia Pendell

def main():
    sign_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
    print_board(sign_list)
    players_turn(sign_list)

def print_board(sign_list):
    print(f""" 
 {sign_list[0]} | {sign_list[1]} | {sign_list[2]}
---+---+---
 {  sign_list[3]} | {sign_list[4]} | {sign_list[5]}
---+---+---
 {  sign_list[6]} | {sign_list[7]} | {sign_list[8]}
    """)

def players_turn(sign_list):
    game = True
    while game:
        signs = ["X", "O"]
        for sign in signs:
            get_player_input(sign, sign_list)
            print_board(sign_list)
            game = not game_done(sign_list, True)
            if game == False:
                break

def get_player_input(sign, sign_list):
    sign_input = input(f"{sign}> ")
    if str.isdigit(sign_input) != True or sign_list[int(sign_input) -1] != " ":
        if str.isdigit(sign_input) != True:
            print("sign_input is not an int")
        else:
            print("Choose a blank space to put your sign.")
        get_player_input(sign, sign_list)
    else:
        sign_input = int(sign_input)
        sign_list[(sign_input-1)] = sign
        return

def game_done(board, message=False):
    BLANK = " "
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False

main()