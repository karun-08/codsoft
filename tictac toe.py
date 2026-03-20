import math

board =[" " for i in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3],board[i*3+1],board[i*3+2])
        if i<2:
         print("--+--+--")

def check_win(b, player):
    win_positions = [
      [0,1,2],[3,4,5],[6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
     if b[pos[0]] == b[pos[1]] == b[pos[2]] == player:
            return True
    return False

def is_draw(b):
    return " " not in b

def minimax(b, depth, is_max):
    if check_win(b,"O" ):
        return 10 - depth
    if check_win(b,"X"):
        return depth - 10
    if is_draw(b):
        return 0
    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best = max(score, best)
        return best

    else:
         best = math.inf
         for i in range(9):
             if b[i] == " ":
                 b[i] = "X"
                 score = minimax(b, depth+1, True)
                 b[i] = " "
                 best = min(score, best)

         return best

def find_best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board,0,False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play():
    print("positions are 0-8")
    print_board()

    while True:
        try:
           user = int(input('enter position (0-8):'))
           if user <  0 or user > 8:
               print("Enter number between 0-8!")
               continue
        except ValueError:
               print("please enter valid number!")
               continue
        
        if board[user]!=" ":
               print("position already taken!")
               continue
        
        board[user] = "X"
        print_board()

        if check_win(board,"X"):
            print("You win!")
            break
        if is_draw(board):
            print("draw")
            break

        ai = find_best_move()
        board[ai] = "O"

        print("\nAI move.")
        print_board()

        if check_win(board,"O"):
            print("AI wins")
            break
        if is_draw(board):
            print("draw")
            break
        
play()