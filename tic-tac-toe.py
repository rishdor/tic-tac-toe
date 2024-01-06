import tkinter as tk
from tkinter import messagebox

class Scoreboard(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.score = [0, 0]
        self.turn = 'X'

        self.score_label = tk.Label(self, text="X: 0  O: 0", bg="black", fg="white", anchor='center', justify='center')
        self.score_label.pack()

        self.turn_label = tk.Label(self, text="Turn: X", bg="black", fg="white", anchor='center', justify='center')
        self.turn_label.pack()

    def update_score(self, winner):
        if winner == 'O':
            self.score[0] += 1
        elif winner == 'X':
            self.score[1] += 1

        self.score_label['text'] = "O: {}  X: {}".format(*self.score)

    def update_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

        self.turn_label['text'] = "Turn: {}".format(self.turn)
    
class GameFlow:
    def __init__(self, size=3, win_length = 3):
        self.root = tk.Tk()
        self.root.configure(bg='black')
        self.size = size
        self.win_length = win_length
        self.button_width = 77
        self.button_height = 83
        self.board_frame = tk.Frame(self.root, width=self.button_width*self.size, height=self.button_height*self.size)
        self.board_frame.pack_propagate(False)
        self.board = None
        self.scoreboard = Scoreboard(self.root, bg="black")

    def create_board(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                button = tk.Button(self.board_frame, text=" ", width=10, height=5, bg="black", fg="white", activebackground="gray", command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            board.append(row)
        return board

    def on_button_click(self, i, j):
        button = self.board[i][j]
        if button['text'] == " ":
            button.config(text=self.scoreboard.turn)
            if self.check_winner(self.scoreboard.turn):
                self.scoreboard.update_score(self.scoreboard.turn)
                messagebox.showinfo("game over", "{} won".format(self.scoreboard.turn))
                self.reset_board()
            elif not self.check_for_available_moves():
                messagebox.showinfo("game over", "its a draw")
                self.reset_board()
            else:
                self.scoreboard.update_turn()

    def check_winner(self, player):
        def check_consecutive(lst, symbol, length):
            count = 0
            for item in lst:
                if item == symbol:
                    count += 1
                    if count == length:
                        return True
                else:
                    count = 0
            return False

        for i in range(self.size):
            if check_consecutive([button['text'] for button in self.board[i]], player, self.win_length):
                return True
            if check_consecutive([self.board[j][i]['text'] for j in range(self.size)], player, self.win_length):
                return True

        for i in range(self.size - self.win_length + 1):
            for j in range(self.size - self.win_length + 1):
                if check_consecutive([self.board[i+k][j+k]['text'] for k in range(self.win_length)], player, self.win_length):
                    return True
                if check_consecutive([self.board[i+k][j+self.win_length-k-1]['text'] for k in range(self.win_length)], player, self.win_length):
                    return True

        return False
    
    def check_for_available_moves(self):
        for i in range(self.size):
            for j in range (self.size):
                if self.board[i][j]['text'] == " ":
                    return True
        return False

    def reset_board(self):
        for row in self.board:
            for button in row:
                button.config(text=" ")

    def start_game(self):
        self.scoreboard.pack()  
        self.board = self.create_board()
        self.board_frame.pack()
        self.root.geometry('{}x{}'.format(self.button_width*self.size + (self.size-1)*3+2, self.button_height*self.size +42+ (self.size-1)*3+2))
        self.root.mainloop()

game = GameFlow(5, 3)
game.start_game()