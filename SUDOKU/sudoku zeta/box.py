import tkinter as tk


class Box:
    boxes = []

    @staticmethod
    def clear_all():
        for i in Box.boxes:
            i.clear()

    @staticmethod
    def output_all():
        return [[Box.boxes[i].output() for i in range(9 * j, 9 * j + 9)] for j in range(9)]

    @staticmethod
    def print_all(p):
        k = 0
        for i in range(9):
            for j in range(9):
                Box.boxes[k].print(p[i][j])
                k += 1

    def __init__(self, master, row, col):
        self.master = master
        self.row = row
        self.col = col
        self.candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.id = tk.Button(master, text="0", font=40, bg='white', relief='raised', cursor='hand2',
                            command=self.set_focus)
        Box.boxes.append(self)

    def un_focus(self, event):
        self.id.config(bg='white', relief='raised')

    def focus(self, event):
        self.id.config(bg='yellow', relief='sunken')

    def set_focus(self):
        self.master.focus_set()
        self.id.focus_set()
        self.id.config(bg='yellow', relief='sunken')

    def input(self, event):
        if event.char in [str(i) for i in range(10)]:
            self.id.config(text=event.char)

    def focus_next_widget(self, event):
        self.id.tk_focusNext().focus()

    def clear(self):
        self.id.config(text="0", bg='white', relief='raised')

    def pack(self):
        self.id.bind("<FocusIn>", self.focus)
        self.id.bind("<FocusOut>", self.un_focus)
        self.id.bind("<Button-3>", self.un_focus)
        self.id.bind("<Tab>", self.focus_next_widget)
        self.id.bind("<Key>", self.input)
        self.id.place(relx=(self.col - 1) / 9, rely=(self.row - 1) / 9, relwidth=1 / 9, relheight=1 / 9)

    def print(self, n):
        self.id.config(text=n)

    def output(self):
        return int(self.id['text'])
