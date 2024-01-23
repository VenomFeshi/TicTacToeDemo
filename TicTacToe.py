from random import randrange

def inizialize_game(board):
    position = 1
    for row in range(3):
        column = []
        for col in range(3):
            column.append(position)
            position+=1
        board.append(column)
    board[1][1] = computer #Computer always make the first move on the middle of the table
    display_board(board)
    return board, position

def display_board(board):
    for i in range(3):
        # Print horizontal line
        print("+-------+-------+-------+")

        for j in range(3):
            # Print vertical line and cell content
            print(f"|   {board[i][j]}   ", end='')

        # End the row with a vertical line
        print("|")

    # Print the last horizontal line
    print("+-------+-------+-------+")

def enter_move(board): #user's turn
    position = 1
    try:
        user_turn = int(input("Select a value from 1 to 9: "))
        if user_turn < 0 or user_turn > 9:
            print("Select a valid number between 1 and 9")
            enter_move(board)
        for row in range(3):
            for col in range(3):
                if position == user_turn and (board[row][col] !=computer and board[row][col] !=user):
                    board[row][col] = user
                    # display_board(board)
                    if(victory_for(board, user)):
                        return True # Here is the solution.
                    # break
                elif position == user_turn and (board[row][col] ==computer or board[row][col] ==user):
                    display_board(board)
                    print("The position is already selected, please try another position.")
                    enter_move(board)
                position+=1
    except ValueError:
        print("Enter a valid character between 1 and 9")
        enter_move(board)

def draw_move(board): #machine's turn
    position = 1
    computer_turn = randrange(1,10)
    for row in range(3):
        for col in range(3):
            if position == computer_turn and (board[row][col] !=computer and board[row][col] !=user):
                board[row][col] = computer
                # display_board(board)
                if (victory_for(board, computer)):
                    return True # Here is the solution.
                # break
            position+=1 

# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    for row in range(3):
        count = 0
        for col in range(2):
            if (board[row][col] == board[row][col+1]):
                count += 1
        if count ==2 or count == 2:
            print(winner_message + sign)
            return True

    for row in range(3):
        count = 0
        for col in range(2):
            if (board[col][row] == board[col+1][row]):
                count += 1
        if count == 2:
            print(winner_message + sign)
            return True

    count = 0
    for col in range(2):
        if (board[col][col] == board[col+1][col+1]):
            count+=1
    if count == 2:
        print(winner_message + sign)
        return True

    count = 0
    for col in range(2):
        if (board[col][2-col] == board[col+1][1-col]):
            count+=1
    if count == 2:
        print(winner_message + sign)
        return True
    display_board(board)

#the program starts here
user = "o"
computer = "x"
winner_message = "the winner is: "

bucle = False
board = []

currently_turn = 0 #alternates between user and computer's turn

inizialize_game(board)

while not (bucle):
    if currently_turn == 0:
        bucle = enter_move(board)
        currently_turn = 1
    elif currently_turn == 1:
        bucle = draw_move(board)
        currently_turn = 0
display_board(board)