from random import randrange

def display_board(board):
    position = 1
    for row in range(3):
        # Print horizontal line
        print("+-------+-------+-------+")

        for col in range(3):
            # Print vertical line and cell content
            if board[row][col] == '':
                print(f"|   {position}   ", end='')
            else:
                print(f"|   {board[row][col]}   ", end='')
            position += 1
        # End the row with a vertical line
        print("|")

    # Print the last horizontal line
    print("+-------+-------+-------+")

def enter_move(board): #user's turn
    try:
        user_turn = int(input("Select a value from 1 to 9: "))
        if 1 <= user_turn <= 9:
            row_index = (user_turn - 1) // 3
            col_index = (user_turn - 1) % 3

            if board[row_index][col_index] == "":
                board[row_index][col_index] = user
                return True
            else:
                print(f"The position {user_turn} is already taken. Select another one.")
        else:
            print("Try another number between 1 and 9.")
    except ValueError:
        print("Input a valid number, not whatever character.")

def draw_move(board): #machine's turn
    computer_turn = randrange(1,10)
    if 1 <= computer_turn <= 9:
        row_index = (computer_turn - 1) // 3
        col_index = (computer_turn - 1) % 3

        if board[row_index][col_index] == "":
            board[row_index][col_index] = computer
            return True # This must be better implemented 
                        #'cause it will cause a lot of iterations until it finds 
                        #the correct number

def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '' or \
           board[0][i] == board[1][i] == board[2][i] != '':
            print("The winner is: ",sign)
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '' or \
       board[0][2] == board[1][1] == board[2][0] != '':
        print("The winner is: ",sign)
        return True

    # Check if its a Tie
    elif ("" not in board[0] and "" not in board[1] and "" not in board[2]):
        print("It's a Tie!")
        return True

    return False

user = "o"
computer = "x"


# board = [["o","o","x"],["x","x","o"],["o","","x"]] #list generated to simulate a Tie
board = [["","",""],["","x",""],["","",""]] #Game inizialize with an x in the position 11

currently_turn = 0
bucle = False

# display_board(board)

while not (bucle):
    display_board(board)
    if currently_turn == 0 and enter_move(board):
        if(victory_for(board,user)):
            bucle = True
        currently_turn = 1

    elif currently_turn == 1 and draw_move(board):
        if(victory_for(board,computer)):
            bucle = True
        currently_turn = 0
display_board(board)