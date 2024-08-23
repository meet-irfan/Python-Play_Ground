import tkinter as tk
import random


class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        self.buttons = []
        self.first_click = None
        self.second_click = None
        self.values = list(range(1, 9)) * 2
        random.shuffle(self.values)

        self.create_buttons()

    def create_buttons(self):
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, text=" ", font=("Arial", 20), width=6, height=3,
                                command=lambda i=i, j=j: self.on_button_click(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def on_button_click(self, i, j):
        if self.first_click is None:
            self.first_click = (i, j)
            self.buttons[i][j].config(text=self.values[i * 4 + j], state="disabled")
        elif self.second_click is None:
            self.second_click = (i, j)
            self.buttons[i][j].config(text=self.values[i * 4 + j], state="disabled")
            self.root.after(500, self.check_match)

    def check_match(self):
        i1, j1 = self.first_click
        i2, j2 = self.second_click

        if self.values[i1 * 4 + j1] == self.values[i2 * 4 + j2]:
            self.buttons[i1][j1].config(bg="green")
            self.buttons[i2][j2].config(bg="green")
        else:
            self.buttons[i1][j1].config(text=" ", state="normal")
            self.buttons[i2][j2].config(text=" ", state="normal")

        self.first_click = None
        self.second_click = None


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
