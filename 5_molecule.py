import pandas as pd
import random


class Schedule:
    def __init__(self, group_number, students):
        self.group_number = group_number
        self.students = students
        self.week_schedule = {'Понедельник': ['', '', '', '', '', ''], 'Вторник': ['', '', '', '', '', ''],
                              'Среда': ['', '', '', '', '', ''], 'Четверг': ['', '', '', '', '', ''],
                              'Пятница': ['', '', '', '', '', ''], 'Суббота': ['', '', '', '', '', '']}

    def create_schedule(self):
        our_lessons = Lesson.all_lessons
        random.shuffle(our_lessons)
        our_rooms = Classrooms.rooms

        counter = 0
        for elem in our_lessons:
            for i in range(6):
                if counter != 0:
                    counter = 0
                    break

                for key in self.week_schedule:
                    if counter != 0:
                        break
                    if self.week_schedule[key][i] == '':
                        random.shuffle(our_rooms)
                        for room in our_rooms:
                            if Classrooms.rooms_availability[room] >= self.students:
                                self.week_schedule[key][i] = f'{elem} ауд. {room}'
                                counter += 1
                                break

    def show_schedule(self):
        df = pd.DataFrame(self.week_schedule)
        df.index += 1
        with open('schedule.xlsx', 'w', encoding='utf-8') as f:
            df.to_excel('schedule.xlsx')


class Lesson:
    all_lessons = []

    def __init__(self, title, teacher, l_type):
        self.title = title
        self.teacher = teacher
        self.l_type = l_type

    def __repr__(self):
        return f'{self.title} {self.teacher} {self.l_type}'

    @classmethod
    def upload(cls, file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                title, teacher, l_type = line.strip().split('; ')
                cls.all_lessons.append(Lesson(title, teacher, l_type))


class Classrooms:
    rooms = []
    rooms_availability = {}

    def __init__(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                room, capacity = line.split('; ')
                Classrooms.rooms.append(room)
                Classrooms.rooms_availability[room] = int(capacity)


auditorium = Classrooms('classrooms.txt')
Lesson.upload('lessons.txt')
our_schedule = Schedule(22704, 30)
our_schedule.create_schedule()
our_schedule.show_schedule()
