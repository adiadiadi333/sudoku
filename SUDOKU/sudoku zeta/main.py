import tkinter as tk
from box import Box
from cell import *

root = tk.Tk()
root.title("SUDOKU SOLVER")
root.geometry("630x720")

tray = tk.Frame(root, bg='red', height=630, width=630, relief='ridge', bd=9)
tray.pack(side="top")

for i in range(1, 10):
    for j in range(1, 10):
        Box(tray, i, j).pack()


def show_soln():
    puzzle = Box.output_all()
    soln = solved(puzzle)
    if all_filled(soln):
        Box.print_all(soln)
    else:
        popup=tk.Tk()
        popup.title('ARE YOU JOKING?!!')
        popup.geometry("700x60")
        tk.Label(popup,text="ITS IMPOSSIBLE!!!",font=('courier',30),fg='red',bg='yellow').pack(fill='both',expand=True)


btn_frame = tk.Frame(root, bg='blue', height=90, width=630)
btn_frame.config(highlightbackground='green', highlightthickness=15)
btn_frame.pack(side="bottom", expand=True, fill="x")

clear = tk.Button(btn_frame, text='CLEAR', fg='yellow', bg='orange', font=('courier', 40, 'bold'), relief='groove',
                  bd=10, command=Box.clear_all)
clear.pack(side="left", fill="both", in_=btn_frame, expand=True)

solve = tk.Button(btn_frame, text='SOLVE', fg='yellow', bg='orange', font=('courier', 40, 'bold'), relief='groove',
                  bd=10, command=show_soln)
solve.pack(side="left", fill="both", in_=btn_frame, expand=True)

root.mainloop()
