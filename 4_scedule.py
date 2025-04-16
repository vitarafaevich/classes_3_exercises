#day - group - lesson_num - auditory - lesson_type - lesson_name - professor


class Information:
    """
    Class representing schedule information
    """
    def __init__(self, day, group, lesson_num, auditory, lesson_type, lesson_name, professor):
        self.day = day
        self.group = group
        self.lesson_num = lesson_num
        self.auditory = auditory
        self.lesson_type = lesson_type
        self.lesson_name = lesson_name
        self.professor = professor

    def __repr__(self):
        return f'{self.day} {self.group} {self.lesson_num} {self.auditory} {self.lesson_type} {self.lesson_name} {self.professor}'


class Schedule:
    """
    Class representing a schedule
    """
    all_lessons = {}

    @classmethod
    def upload(cls, filename):
        """
        Method resume(self, name): to resume (continue) the composition playback
        :param filename: the name of the file where data is stored
        """
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    day, group, lesson_num, auditory, lesson_type, lesson_name, professor = line.strip().split(
                        ' ; ')
                    info = Information(day, group, lesson_num, auditory, lesson_type, lesson_name, professor)
                    cls.all_lessons[day] = [info[1:]]

    def show(self):
        """
        Method show(self): to show the schedule for a week
        """
        for day in self.all_lessons:
            lessons = self.all_lessons[day]
            print(f'Schedule for {day}:')
            for lesson in lessons:
                print(
                    f'  {lesson.lesson_num}. {lesson.lesson_name} ({lesson.lesson_type}) - {lesson.auditory}, Professor: {lesson.professor}')
            print()


schedule = Schedule()
schedule.upload('shedule.txt')
schedule.show()
