import tkinter as tk
import tkinter.messagebox as mbox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        self.buttons = []

        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=("Helvetica", 20), width=4, height=2,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        reset_button = tk.Button(master, text="Reset", font=("Helvetica", 14), command=self.reset_board)
        reset_button.grid(row=3, column=1)

    def handle_click(self, row, col):
        index = 3 * row + col
        button = self.buttons[index]
        if self.board[index] == " ":
            self.board[index] = self.current_player
            button.config(text=self.current_player)
            if self.check_for_winner():
                mbox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_for_tie():
                mbox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_for_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]

        for i, j, k in win_conditions:
            if self.board[i] == self.board[j] == self.board[k] != " ":
                return True

        return False

    def check_for_tie(self):
        return " " not in self.board

    def reset_board(self):
        self.current_player = "X"
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
