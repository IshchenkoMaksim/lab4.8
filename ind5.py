#!/usr/bin/env python3
# -*- coding: utf-8

"""
B программе создается анимация круга, который движется от левой
границы холста до правой. Изучите приведенную программу и
самостоятельно запрограммируйте постепенное движение фигуры в ту т
очку холста, где пользователь кликает левой кнопкой мыши. Координаты
события хранятся в его атрибутах x и y (event.x, event.y).
"""

from tkinter import Tk, Canvas


def click(event):
    c.x = event.x + c.radius
    c.y = event.y + c.radius
    motion()


def motion():
    x = c.coords(c.ball)[2]
    y = c.coords(c.ball)[3]
    if c.x == x and c.y == y:
        return
    if c.x < x:
        c.move(c.ball, -1, 0)
    if c.x > x:
        c.move(c.ball, 1, 0)
    if c.y < y:
        c.move(c.ball, 0, -1)
    if c.y > y:
        c.move(c.ball, 0, 1)
    root.after(10, motion)


if __name__ == "__main__":
    root = Tk()

    c = Canvas(root, width=300, height=200, bg="white")

    c.pack()
    c.radius = 20
    c.ball = c.create_oval(0, 100, 40, 140, fill='green')

    c.bind("<Button-1>", click)

    root.mainloop()
