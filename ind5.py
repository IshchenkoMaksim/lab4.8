#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
B программе создается анимация круга, который движется от левой
границы холста до правой. Изучите приведенную программу и
самостоятельно запрограммируйте постепенное движение фигуры в ту т
очку холста, где пользователь кликает левой кнопкой мыши. Координаты
события хранятся в его атрибутах x и y (event.x, event.y).
"""

from tkinter import Tk, Canvas
import math


class Ball:
    def __init__(self, width=400, height=300):
        self.x = 1
        self.y = 1
        self.t = 0
        self.dt = 1
        self.i = 1
        self.height = height
        self.width = width
        self.rad = 20

        self.c = Canvas(root, width=self.width, height=self.height, bg="white")
        self.c.pack()
        self.ball = self.c.create_oval(0, 100, 40, 140, fill='green')

        self.c.bind('<Button-1>', self.click)
        root.after(10, self.frame)

    def click(self, event):
        p = self.c.coords(self.ball)
        dx = event.x - p[0]
        dy = event.y - p[1]

        r = math.sqrt(dx ** 2 + dy ** 2)
        self.x = dx / r
        self.y = dy / r

        self.t += self.dt
        p[0] += self.x + 10
        p[1] += self.y + 10

        if 200 > dx >= 100 or 200 > dy >= 100 or -200 < dx <= -100 or -200 < dy <= -100:
            self.dt = 2
        elif 300 > dx >= 200 or 300 > dy >= 200 or -300 < dx <= -200 or -300 < dy <= -200:
            self.dt = 4
        elif 500 > dx >= 300 or 500 > dy >= 300 or -500 < dx <= -300 or -500 < dy <= -300:
            self.dt = 7
        elif dx >= 500 or dy >= 500 or dx <= -500 or dy <= -500:
            self.dt = 10
        else:
            self.dt = 1

    def frame(self):
        self.c.move(self.ball, self.dt * self.x, self.dt * self.y)
        p = self.c.coords(self.ball)

        if p[1] < 0 or p[1] > self.height - 2 * self.rad:
            self.y = -self.y

        if p[0] < 0 or p[0] > self.width - 2 * self.rad:
            self.x = -self.x

        root.after(10, self.frame)


if __name__ == '__main__':
    root = Tk()
    Ball()
    root.mainloop()
