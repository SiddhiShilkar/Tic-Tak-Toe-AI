import tkinter as tk
import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    # Check rows, columns, and diagonals for a win or a draw
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return 10 if board[i][0] == 'X' else -10
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return 10 if board[0][i] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return 10 if board[0][2] == 'X' else -10

    return 0

def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = "-"
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = "-"
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = "-"

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def on_click(row, col):
    global current_player, game_over

    if board[row][col] == "-" and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        score = evaluate(board)
        if score == 10:
            label.config(text="AI wins!")
            game_over = True
        elif score == -10:
            label.config(text="You win!")
            game_over = True
        elif not is_moves_left(board):
            label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if current_player == 'X':
                ai_move()

def ai_move():
    global current_player, game_over
    if not game_over:
        row, col = find_best_move(board)
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        score = evaluate(board)
        if score == 10:
            label.config(text="AI wins!")
            game_over = True
        elif score == -10:
            label.config(text="You win!")
            game_over = True
        elif not is_moves_left(board):
            label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def create_gui():
    global buttons, label

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    label = tk.Label(root, text="Tic-Tac-Toe", font=("Helvetica", 20))
    label.pack()

    frame = tk.Frame(root, bg="lightblue")
    frame.pack()

    buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(frame, text="-", font=("Helvetica", 20), width=6, height=2,
                                      command=lambda i=i, j=j: on_click(i, j))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    create_gui()

def reset_game():
    global board, current_player, game_over
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    label.config(text="Tic-Tac-Toe")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="-")

def on_click(row, col):
    global current_player, game_over

    if board[row][col] == "-" and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        score = evaluate(board)
        if score == 10:
            label.config(text="AI wins!")
            game_over = True
        elif score == -10:
            label.config(text="You win!")
            game_over = True
        elif not is_moves_left(board):
            label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if current_player == 'X':
                ai_move()

        if game_over:
            root.after(1000, reset_game)  # Start a new game after 1 second

def ai_move():
    global current_player, game_over
    if not game_over:
        row, col = find_best_move(board)
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        score = evaluate(board)
        if score == 10:
            label.config(text="AI wins!")
            game_over = True
        elif score == -10:
            label.config(text="You win!")
            game_over = True
        elif not is_moves_left(board):
            label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
