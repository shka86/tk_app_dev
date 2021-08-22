#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk

class FrameTop(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.master = master
        self.master.title("sample waku1")
        self.gen_frame_left()
        self.gen_frame_right()

    def gen_frame_left(self):
        self.frame_left = tk.Frame(self.master, width=100, height=100, bg="navy")
        self.frame_left.grid(row=0, column=0)

        self.nb = ttk.Notebook(master=self.frame_left)
        self.tab1 = Tab(self.nb, label="tab1")
        self.tab2 = Tab(self.nb, label="tab2")

    def gen_frame_right(self):
        self.frame_right = tk.Frame(self.master, width=100, height=100, bg="blue")
        self.frame_right.grid(row=0, column=1)

# class FrameLeft(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)


# class FrameRight(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)


class Tab(tk.Frame):
    def __init__(self, master=None, label=""):
        super().__init__(master)
        master.add(self, text=label, padding=3)
        master.pack()


def main():
    # make window ##########################
    root = tk.Tk()
    top = FrameTop(root)
    top.mainloop()

if __name__ == '__main__':
    main()
