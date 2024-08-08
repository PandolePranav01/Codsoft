import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2, 
                                               command=lambda i=i, j=j: self.player_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def player_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state=tk.DISABLED)
            if self.check_winner("X"):
                messagebox.showinfo("Tic-Tac-Toe", "You win!")
                self.reset_board()
                return
            if self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
                return
            self.current_player = "O"
            self.ai_move()

    def ai_move(self):
        row, col = self.find_best_move()
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", state=tk.DISABLED)
        if self.check_winner("O"):
            messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            self.reset_board()
            return
        if self.is_board_full():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            self.reset_board()
            return
        self.current_player = "X"

    def find_best_move(self):
        best_move = None
        best_value = -math.inf
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    move_value = self.minimax(False, -math.inf, math.inf)
                    self.board[i][j] = " "
                    if move_value > best_value:
                        best_move = (i, j)
                        best_value = move_value
        return best_move

    def minimax(self, is_maximizing, alpha, beta):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        eval = self.minimax(False, alpha, beta)
                        self.board[i][j] = " "
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        eval = self.minimax(True, alpha, beta)
                        self.board[i][j] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return [player, player, player] in win_conditions

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
