from random import randrange

def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + (board[0][0]) + '   |   ' + (board[0][1]) + '   |   ' + (board[0][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + str(board[1][0]) + '   |   ' + str(board[1][1]) + '   |   ' + str(board[1][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + str(board[2][0]) + '   |   ' + str(board[2][1]) + '   |   ' + str(board[2][2]) + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')  

def enter_move(board):
    while True:
        move = int(input("Please pick a number within the range of squares (1-9): "))
        if move < 1 or move > 9:
            print("Please enter a number from 1 through 9: ")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print("Sorry, that square is already taken. Please selecte another square: ")
            continue
        for row in range(3):
            for cell in range(3):
                if board[row][cell] == str(move):
                    board[row][cell] = "O"
        break
def make_list_free_fields(board):
    global free_squares # we need this for computer move func to we make it global
    free_squares = []
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == "X" or board[row][cell] == "O":
                pass
            else:
                free_squares.append(([row],[cell]))
    print(free_squares)
    
def victory(board, sign):
    if sign == 'O':
        print("Checking to see if you won:")
    else:
        print("Checking to see if computer won")
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        print("No winner yet")
        
def computer_move(board):
    while True:
        row = randrange(3)
        cell = randrange(3)       
        
        if ([row], [cell]) not in free_squares:
            continue
        else:
            board[row][cell] = "X"
            return
        
        
board = [['1','2','3'], ['4',"X",'6'], ['7','8','9']]
number_of_moves = 1 # computer always goes first as X is placed in square 5 on game board
user = 'O'
computer = 'X'
print("Welcome to Tic-Tact-Toe the Pythonic Way")
print("Here is the current status of the game board")
display_board(board)
print()

while number_of_moves < 9:
    # user turn each round
    enter_move(board)
    number_of_moves += 1
    display_board(board)
    if victory(board, user):
        print("You won!")
        break
    else:
        print("Here is the list of open cells and the board itself")
        make_list_free_fields(board)
        print()
        display_board(board)

    # Computer Turn now
    print()
    print("Computer move now")
    computer_move(board)
    number_of_moves += 1
    display_board(board)
    print()
    
    if victory(board, computer) == True:
        print("Computer wins. You suck at tic-tac-toe")
        break
    else:
        print("Here is the list of open cells and the board itself")
        make_list_free_fields(board)
        print()
        display_board(board)
else:
    print("Tie game")       
    # computer move    
    print()
    
print("Thanks for playing")







