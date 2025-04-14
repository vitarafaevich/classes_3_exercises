import math


class Schedule:
    def __init__(self, day, group, classroom, lesson, num, type, teacher):
        self.__day = day
        self.__group = group


class Classes:
    classes_list = []
    timing_tuple = {}

    def __init__(self, lesson, professor, name, num_cl):
        self.num_class = lesson
        self.professor = professor
        self.class_name = name
        self.num_cl = num_cl

    #to write normally with datetime
    @classmethod
    def timing(cls):
        for i in range (1, (math.ceil((((24-9)*60)/110)/60))+1):
            duration = 110
            start_time = 9

            mins = (i*60+duration%60)
            cls.timing_tuple[i] = [9 + ((i*60+duration)//60) + ':' + str(mins)]




    @classmethod
    def data(cls, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                lesson, professor, name = line.strip().split(' ; ')
                #i'm not sure
                cls.classes_list.append(cls(lesson, professor, name))



class Information:
    def __init__(self, day, group):
        self.__day = day
        self.__group = group

