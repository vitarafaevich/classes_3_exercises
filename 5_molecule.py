import tkinter
import random

tk = tkinter.Tk()
c = tkinter.Canvas(tk, width=500, height=500, bg='white')
#to add canvas into the main window
c.pack()


class Molecule:
    """
    Class representing a Molecule
    """
    #direction of movement on x and y
    x_dir = 15
    y_dir = 5

    def __init__(self, color, radius, speed):
        self.color = color
        self.radius = radius
        self.speed = speed
        #starting position on the canvas
        x_start = random.randint(10, 400)
        y_start = x_start
        self.object = c.create_oval(x_start, y_start, radius + x_start, radius + y_start, fill=color)

    def move_molecule(self):
        """
        Method move_molecule(self): to chaotically move molecule in the canvas
        """
        #getting the coordinates
        x1, y1, x2, y2 = c.coords(self.object)
        if x1 + self.radius  <= 0 or x2 + self.radius  >= 500:
            Molecule.x_dir *= -1
        if y1 + self.radius  <= 0 or y2 + self.radius >= 500:
            Molecule.y_dir *= -1

        c.move(self.object, Molecule.x_dir, Molecule.y_dir)
        #the next call of move_molecule after time in speed
        c.after(self.speed, self.move_molecule)


molecule1 = Molecule('light blue', 30, 100)
molecule1.move_molecule()
molecule2 = Molecule('light green', 40, 80)
molecule2.move_molecule()
molecule3 = Molecule('salmon', 50, 60)
molecule3.move_molecule()
molecule4 = Molecule('lavender', 35, 120)
molecule4.move_molecule()
molecule5 = Molecule('peachpuff', 45, 90)
molecule5.move_molecule()
molecule6 = Molecule('light coral', 55, 70)
molecule6.move_molecule()
molecule7 = Molecule('khaki', 25, 110)
molecule7.move_molecule()
molecule8 = Molecule('powder blue', 65, 50)
molecule8.move_molecule()
molecule9 = Molecule('light yellow', 70, 40)
molecule9.move_molecule()
molecule10 = Molecule('light pink', 20, 130)
molecule10.move_molecule()
molecule11 = Molecule('thistle', 60, 75)
molecule11.move_molecule()
molecule12 = Molecule('light goldenrod', 50, 55)
molecule12.move_molecule()
molecule13 = Molecule('honeydew', 45, 85)
molecule13.move_molecule()
molecule14 = Molecule('misty rose', 35, 65)
molecule14.move_molecule()
molecule15 = Molecule('sky blue', 80, 30)
molecule15.move_molecule()

#to keep the window open
tkinter.mainloop()