#!/usr/bin/env python3
# -*- coding: utf-8

"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном
текстовом поле приводит к перемещению текста из него в список (экземпляр
Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке
списка, она должна копироваться в текстовое поле.
"""

from tkinter import Tk, Listbox, Entry


def add(event):
    item = ent.get()
    lab.insert(0, item)
    ent.delete(0, 'end')


def copy(event):
    # ent.delete(0, 'end')
    item = lab.get(lab.curselection())
    ent.insert('end', item)


if __name__ == "__main__":
    root = Tk()

    ent = Entry(width=30)
    ent.pack(padx=3, pady=5)
    ent.bind('<Return>', add)

    lab = Listbox(width=30, height=15)
    lab.pack()
    lab.bind('<Double-Button-1>', copy)

    root.mainloop()
