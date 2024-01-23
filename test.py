def enter_move():
    if(input("Input whatever you want player 1: ") == "a"):
        print("player 1")
        return True

def draw_move():
    if(input("Input whatever you want player 2: ") == "b"):
        print("player 2")
        return True

bucle = False
currently_turn = 0

while not (bucle):
    if currently_turn == 0:
        bucle = enter_move()
        currently_turn = 1
    elif currently_turn == 1:
        bucle = draw_move()
        currently_turn = 0