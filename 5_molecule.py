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


'''import tkinter
import random
import math

tk = tkinter.Tk()
canvas_size = 500
c = tkinter.Canvas(tk, width=canvas_size, height=canvas_size, bg='white')
c.pack()

class Molecule:
    """
    Class representing a Molecule
    """
    def __init__(self, color, radius, speed):
        self.color = color
        self.radius = radius
        self.speed = speed
        self.x_dir = random.choice([-1, 1]) * random.randint(5, 15)
        self.y_dir = random.choice([-1, 1]) * random.randint(5, 15)

        #starting position on the canvas
        x_start = random.randint(10, canvas_size - 100)
        y_start = random.randint(10, canvas_size - 100)
        self.object = c.create_oval(x_start, y_start, radius + x_start, radius + y_start, fill=color)

    def move_molecule(self):
        """
        Method to chaotically move molecule in the canvas
        """
        x1, y1, x2, y2 = c.coords(self.object)

        #avoiding collision with walls
        if x1 - self.radius <= 0 or x2 + self.radius >= canvas_size or y1 - self.radius <= 0 or y2 + self.radius >= canvas_size:
            self.random_direction() 

        c.move(self.object, self.x_dir, self.y_dir)

        #avoiding collision with other molecules
        for other in molecules:
            if other != self and self.is_colliding(other):
                self.handle_collision(other)

        # Следующий вызов move_molecule через указанный интервал времени
        c.after(50, self.move_molecule)  # Уменьшено время для более плавного движения

    def is_colliding(self, other):
        """
        Проверка на столкновение с другой молекулой
        """
        x1, y1, x2, y2 = c.coords(self.object)
        ox1, oy1, ox2, oy2 = c.coords(other.object)

        # Проверка расстояния между центрами молекул
        distance = math.sqrt((x1 + self.radius - (ox1 + other.radius)) ** 2 +
                             (y1 + self.radius - (oy1 + other.radius)) ** 2)
        return distance < (self.radius + other.radius)

    def handle_collision(self, other):
        """
        Обработка столкновения с другой молекулой
        """
        self.random_direction()  # Изменение направления при столкновении

    def random_direction(self):
        """
        Выбор случайного направления
        """
        #random angle and direction
        angle = random.uniform(0, 2 * math.pi)
        self.x_dir = self.speed * math.cos(angle)
        self.y_dir = self.speed * math.sin(angle)

# Создание списка молекул
molecules = [
    Molecule('light blue', 30, 5),
    Molecule('light green', 30, 5),
    Molecule('salmon', 30, 5),
    Molecule('lavender', 30, 5),
    Molecule('peachpuff', 30, 5),
    Molecule('light coral', 30, 5),
    Molecule('khaki', 30, 5),
    Molecule('powder blue', 30, 5),
    Molecule('light yellow', 30, 5),
    Molecule('light pink', 30, 5),
    Molecule('thistle', 30, 5),
    Molecule('light goldenrod', 30, 5),
    Molecule('honeydew', 30, 5),
    Molecule('misty rose', 30, 5),
    Molecule('sky blue', 30, 5)
]

# Запуск движения для каждой молекулы
for molecule in molecules:
    molecule.move_molecule()

# Держим окно открытым
tkinter.mainloop()
'''

'''
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
'''