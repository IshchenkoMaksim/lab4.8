#!/usr/bin/env python3
# -*- coding: utf-8

"""
Напишите программу по описанию. Размеры многострочного текстового
поля определяются значениями, введенными в однострочные текстовые поля.
Изменение размера происходит при нажатии мышью на кнопку,  а также при
нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый (lightgrey),
когда поле не в фокусе,  и белый, когда имеет фокус. Событие получения
фокуса обозначается как <FocusIn> , потери – как <FocusOut>.
"""

from tkinter import Tk, Frame, Entry, Button, Text, LEFT, RIGHT


def change_size(event):
    txt1['width'] = ent1.get()
    txt1['height'] = ent2.get()


def focus_change(event, color):
    txt1['bg'] = color


if __name__ == "__main__":
    root = Tk()

    f = Frame()
    f.pack()

    ent1 = Entry(f, width=3)
    ent1.bind('<Return>', change_size)
    ent1.pack(side=LEFT)

    ent2 = Entry(f, width=3)
    ent2.bind('<Return>', change_size)
    ent2.pack(side=LEFT)

    but = Button(f, text='Изменить')
    but.bind('<Button-1>', change_size)
    but.pack(side=RIGHT)

    txt1 = Text(width=20, height=15, bg='lightgrey')
    txt1.bind('<FocusIn>', lambda x, c="white": focus_change(x, c))
    txt1.bind('<FocusOut>', lambda x, c="lightgrey": focus_change(x, c))
    txt1.pack()

    root.mainloop()
