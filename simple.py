#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk

# make window ##########################
root = tk.Tk()
root.title("sample waku1")
nb = ttk.Notebook(master=root)

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
