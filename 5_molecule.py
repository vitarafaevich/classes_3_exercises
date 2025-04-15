import tkinter
import random

tk = tkinter.Tk()
c = tkinter.Canvas(tk, width=500, height=500, bg='white')
c.pack()


class Molecule:
    x_dir = 15
    y_dir = 5

    def __init__(self, color, radius, speed):
        self.color = color
        self.radius = radius
        self.speed = speed
        x_start = random.randint(10, 450)
        y_start = x_start
        self.object = c.create_oval(x_start, y_start, radius + x_start, radius + y_start, fill=color)

    def move_molecule(self):
        x1, y1, x2, y2 = c.coords(self.object)
        if x1 <= 0 or x2 >= 500:
            Molecule.x_dir *= -1
        if y1 <= 0 or y2 >= 500:
            Molecule.y_dir *= -1

        c.move(self.object, Molecule.x_dir, Molecule.y_dir)

        c.after(self.speed, self.move_molecule)


molecule1 = Molecule('light blue', 60, 100)
molecule1.move_molecule()
molecule2 = Molecule('yellow', 50, 60)
molecule2.move_molecule()
molecule3 = Molecule('pink', 40, 20)
molecule3.move_molecule()
molecule4 = Molecule('purple', 50, 30)
molecule4.move_molecule()
molecule5 = Molecule('green', 60, 200)
molecule5.move_molecule()


tkinter.mainloop()

'''
import random
from tkinter import *

root = Tk()
c = Canvas(width=500, height=500, bg='white')


class Molecule:
    def __init__(self, colour, radius, speed, x_cord=0, y_cord=0):
        self.__colour = colour
        self.__radius = radius
        self.__speed = speed
        #rewrite random
        x_cord = random.randint(10, 100)
        y_cord = x_cord
        self.item = c.create_oval(x_cord, y_cord, radius + x_cord, radius + y_cord, fill)

    def movement(self):
        self.item
'''
