#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk

# make window ##########################
root = tk.Tk()
root.title("sample waku1")

frame_left = tk.Frame(root, width=100, height=100, bg="navy")
frame_left.grid(row=0,column=0)
frame_right = tk.Frame(root, width=100, height=100, bg="blue")
frame_right.grid(row=0,column=1)

nb = ttk.Notebook(master=frame_left)

# make tab1
tab1 = tk.Frame(nb)
nb.add(tab1, text="Tab1", padding=3)
nb.pack()

# make tab2
tab2 = tk.Frame(nb)
nb.add(tab2, text="Tab2", padding=3)
nb.pack()

# gen gui
root.mainloop()
