#!/usr/bin/env python3
# -*- coding: utf-8

"""
Напишите программу, состоящую из двух списков Listbox . В первом
будет,например, перечень товаров, заданный программно. Второй изначально
пуст, пусть это будет перечень покупок. При клике на одну кнопку товар
должен переходить из одного списка в другой. При клике на вторую
кнопку – возвращаться (человек передумал покупать). Предусмотрите
возможность множественного выбора элементов списка и их перемещения
"""

from tkinter import Tk, Listbox, Button, EXTENDED, END, S, N


def add():
    product = []
    select = list(box1.curselection())
    select.reverse()
    for item in select:
        op = box1.get(item)
        product.append(op)
    for val in product:
        box2.insert(0, val)
    for k in select:
        box1.delete(k)


def delete():
    product = []
    select = list(box2.curselection())
    select.reverse()
    for item in select:
        op = box2.get(item)
        product.append(op)
    for val in product:
        box1.insert(0, val)
    for k in select:
        box2.delete(k)


if __name__ == '__main__':
    root = Tk()

    products = ['meat', 'onion', 'apple', 'fish', 'sausage', 'meat',
                'cherry ', 'cheese', 'eggs', 'plum']

    box1 = Listbox(selectmode=EXTENDED)
    box1.grid(row=0, rowspan=2, column=0, pady=5, padx=2)

    box2 = Listbox(selectmode=EXTENDED)
    box2.grid(row=0,  rowspan=2, column=3, padx=2)

    button_up = Button(height=1, width=5, text='>>>', command=add)
    button_up.grid(row=0, column=1, sticky=S)

    button_back = Button(height=1, width=5, text='<<<', command=delete)
    button_back.grid(row=1, column=1, sticky=N)

    for i in products:
        box1.insert(END, i)

    root.mainloop()
