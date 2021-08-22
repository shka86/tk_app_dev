#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import tkinter.ttk as ttk


class Root():
    def __init__(self, title_):
        self.root = tk.Tk()
        self.root.title(title_)
        self.nb = ttk.Notebook()


class FrameTab():
    'rowとcolumnはnotebookに対して効いてない'
    def __init__(self, master, label, row=0, column=0):
        self.r = 0
        self.entity = tk.Frame(master.nb)
        master.nb.add(self.entity, text=label, padding=3)
        master.nb.grid(row=row, column=column)


class FrameBox():
    def __init__(self, master, label):
        self.r = 0
        self.entity = tk.LabelFrame(master.entity, text=label)
        self.entity.pack(padx=5, pady=5)
        master.r += 1


class Button():
    def __init__(self, master, label, bind_action=None):
        self.entity = tk.Button(master.entity, text=label, command=bind_action)
        self.entity.grid(row=master.r, column=1, padx=3, pady=3)
        master.r += 1


class DropDown():
    def __init__(self, master, label, values):
        name = tk.Label(master.entity, text=label)
        name.grid(row=master.r, column=0)
        db = ttk.Combobox(master.entity, state='readonly')
        db["values"] = values
        db.current(0)
        db.grid(row=master.r, column=1, padx=3, pady=3)
        master.r += 1


class Slider():
    def __init__(self, master, label, min_, max_):
        name = tk.Label(master.entity, text=label)
        name.grid(row=master.r, column=0)
        sl = tk.Scale(master.entity, from_=min_, to=max_, orient=tk.HORIZONTAL)
        sl.grid(row=master.r, column=1, padx=3, pady=3)
        master.r += 1


class CheckBox():
    def __init__(self, master, label, ture_false, bind_action=None):
        name = tk.Label(master.entity, text=label)
        name.grid(row=master.r, column=0)

        if ture_false:
            val = tk.BooleanVar().set(True)
        else:
            val = tk.BooleanVar().set(False)

        cb = ttk.Checkbutton(master.entity, variable=val)
        cb.grid(row=master.r, column=1, padx=3, pady=3)
        master.r += 1


####################################################

def test_action_print():
    print("hello_tk_world")

####################################################


if __name__ == '__main__':
    # make window ##########################
    root1 = Root("sample waku1")

    # make tab1
    tab1 = FrameTab(root1, "Tab1")
    # box1_1 = FrameBox(tab1, "box1_1")
    # box1_2 = FrameBox(tab1, "box1_2")
    # btn1 = Button(box1_1, "btn1", test_action_print)
    # slider1 = Slider(box1_1, "param1", 0, 100)
    # slider2 = Slider(box1_1, "param2", 0, 100)
    # dropdown1 = DropDown(box1_1, "param2", ["1", "2", "3"])
    # btn2 = Button(box1_2, "btn2", test_action_print)

    # make tab2
    tab2 = FrameTab(root1, "Tab2")
    # box2_1 = FrameBox(tab2, "box2_1" )
    # box2_2 = FrameBox(tab2, "box2_2")
    # dropdown2 = DropDown(box2_1, "param3", ["a", "b", "c"])
    # checkbox = CheckBox(box2_1, "param4", True)

    # make tab3
    tab3 = FrameTab(root1, "Tab3", row=1, column=1)
    # box3_1 = FrameBox(tab3, "box2_1")
    # dropdown3 = DropDown(box3_1, "param4", ["a", "b", "c"])

    # gen gui
    root1.root.mainloop()
