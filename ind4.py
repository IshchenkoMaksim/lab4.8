#!/usr/bin/env python3
# -*- coding: utf-8

""" Создайте на холсте изображение """

from tkinter import Tk, Canvas, ARC


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")

    c = Canvas(root, width=500, height=400, bg='#fff')
    c.pack()

    c.create_oval((403, 18), (470, 84), fill="#fa0", outline='#fff')
    c.create_rectangle((149, 143), (380, 360), fill='#ade', outline='#fff')
    c.create_polygon((260, 30), (115, 144), (405, 143), fill='#ade')

    x = 0
    while x < 500:
        c.create_arc(x, 500, x + 35, 355, start=160, extent=-80,
                     style=ARC, width=3, outline='#393')
        x += 15

    # кот
    c.create_arc((30, 384), (150, 300), fill="#9aa", outline="#333",
                 width=3, start=-48, extent=90)

    c.create_polygon((25, 380), (55, 245), (70, 285), (95, 285), (115, 245),
                     (130, 380), outline="#333", width=3, fill='#abb')

    c.create_oval((50, 295), (80, 325), fill="#fff", outline="#333", width=3)
    c.create_oval((80, 295), (110, 325), fill="#fff", outline="#333", width=3)

    c.create_oval((70, 305), (75, 315), fill="#000")
    c.create_oval((90, 305), (95, 315), fill="#000")

    c.create_oval((75, 320), (85, 328), fill="#eaa", outline="#333", width=3)

    c.create_line((80, 326), (80, 341), width=2)

    c.create_arc((60, 340), (100, 320), start=-10, extent=-160, style=ARC, width=2)

    c.create_oval((44, 370), (76, 390), fill='#9aa', outline="#333", width=3)
    c.create_oval((78, 370), (110, 390), fill='#9aa', outline="#333", width=3)

    root.mainloop()
