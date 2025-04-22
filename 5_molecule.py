import tkinter
import random
import math

canvas_size = 500
tk = tkinter.Tk()
c = tkinter.Canvas(tk, width=canvas_size, height=canvas_size, bg='white')
c.pack()


class Molecule:
    """
    Class representing a molecule
    """
    def __init__(self):
        self.radius = self.random_radius()
        self.speed = self.random_speed()
        self.color = self.random_color()
        self.x_dir = random.choice([-1, 1]) * random.randint(5, 15)
        self.y_dir = random.choice([-1, 1]) * random.randint(5, 15)

        # starting position on the canvas
        x_start = random.randint(10, canvas_size - self.radius)
        y_start = random.randint(10, canvas_size - self.radius)

        self.object = c.create_oval(x_start, y_start, self.radius + x_start, self.radius + y_start, fill=self.color)

    def movement_guidance(self):
        """
        Method movement_guidance(self): to chaotically move molecule on the canvas
        """
        x1, y1, x2, y2 = c.coords(self.object)

        # avoiding collision with walls
        if (x1 - self.radius <= 0 or x2 + self.radius >= canvas_size
                or y1 - self.radius <= 0 or y2 + self.radius >= canvas_size):
            self.random_direction()
        c.move(self.object, self.x_dir, self.y_dir)

        # avoiding collision with other molecules
        for other in molecules:
            if other != self and self.collision_management(other):
                self.random_direction()

        # the next call of move_molecule after time in speed
        c.after(50, self.movement_guidance)

    def collision_management(self, other):
        """
        Method collision_management(self, other): indicating the collisions
        :param other: the 'other' molecule, allow us to check the collision with 'self' molecule
        """
        #x1, x2 - upper left corner; y1, y2 - lower right corner
        x1, y1, x2, y2 = c.coords(self.object)
        ox1, oy1, ox2, oy2 = c.coords(other.object)

        # checking the distance, formula: d = √((x2 - x1)² + (y2 - y1)²); x1 + self.radius - the center of the molecule;
        # counting the distance between centers
        distance = math.sqrt((x1 + self.radius - (ox1 + other.radius)) ** 2 +
                             (y1 + self.radius - (oy1 + other.radius)) ** 2)
        return distance < (self.radius + other.radius)

    def random_direction(self):
        """
        Method random_direction(self): generating random direction
        """
        self.x_dir = random.choice([-1, 1]) * random.randint(2, 10)
        self.y_dir = random.choice([-1, 1]) * random.randint(2, 10)

    @staticmethod
    def random_radius():
        """
        Staticmethod random_radius(): generating random radius
        """
        return random.randint(10, 60)

    @staticmethod
    def random_speed():
        """
        Staticmethod random_speed(): generating random speed
        """
        return random.randint(2, 10)

    @staticmethod
    def random_color():
        """
        Staticmethod random_color(): generating colours in HEX format
        """
        return f'#{random.randint(0, 0xFFFFFF):06x}'


molecules = [Molecule() for i in range(5)]

for molecule in molecules:
    molecule.movement_guidance()

tkinter.mainloop()
