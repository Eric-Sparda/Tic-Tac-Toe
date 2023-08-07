from tkinter import *
from tkinter import messagebox
import random
import json
import os

window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("450x575")
window.resizable(False,False)

player = 'X'
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


def on_click(row, col):
    global player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        check_winner()
        cpu_row, cpu_col = random.choice([(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""])
        window.after(50, lambda: buttons[cpu_row][cpu_col].config(text="O"))
        check_winner()

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            winner = buttons[row][0]["text"]
            messagebox.showinfo("Winner", f"The winner is {winner}")
            restart_game()

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            winner = buttons[0][col]["text"]
            messagebox.showinfo("Winner", f"The winner is {winner}")
            restart_game()

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        winner = buttons[0][0]["text"]
        messagebox.showinfo("Winner", f"The winner is {winner}")
        restart_game()

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        winner = buttons[0][2]["text"]
        messagebox.showinfo("Winner", f"The winner is {winner}")
        restart_game()
    if all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3)):
        messagebox.showinfo("Tie", "It's a Tie")
        restart_game()

def restart_game():
    global player
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].grid(row=row, column=col)


reset_button = Button(text="Restart", font=('consolas', 20), command=restart_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
