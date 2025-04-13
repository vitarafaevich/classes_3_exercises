'''
class Album:
    album_tuple = {}

    @classmethod
    def album_info(cls, file):
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                name, duration, singer, year = line.strip().split(' - ')
                result = Track(name, duration, singer, year)
                cls.album_tuple[name] = [result.duration, result.singer, result.seconds_dur, result.year,
                                         result.playing, result.start_time, result.played_time, result.end]

    def play(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            if not track_info[4]:  # Если трек не играет
                print(f'Starting to play composition {track_name} by {track_info[1]}')
                track_info[4] = True  # Устанавливаем, что трек играет
                track_info[5] = datetime.datetime.now()  # Запоминаем время начала
                while track_info[6] < track_info[2]:  # track_info[2] - продолжительность в секундах
                    time.sleep(1)
                    track_info[6] += 1  # Увеличиваем время воспроизведения на 1 секунду
                    print(f'Playing... {track_info[6]} seconds played')

                print(f'Composition {track_name} is now over!')
                track_info[4] = False  # Устанавливаем, что трек не играет
                track_info[7] = True  # Устанавливаем, что трек закончился
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def pause(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            if track_info[4]:  # Если трек играет
                print(f'Pausing {track_name}')
                track_info[4] = False  # Устанавливаем, что трек не играет
            else:
                print(f'Composition {track_name} is not currently playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def resume(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            if not track_info[4]:  # Если трек не играет
                print(f'Resuming {track_name}')
                track_info[4] = True  # Устанавливаем, что трек играет
                track_info[5] = datetime.datetime.now()  # Запоминаем время возобновления
                # Здесь можно добавить логику для продолжения воспроизведения с учетом времени паузы
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')


class Track:
    def __init__(self, name, duration, singer, year):
        self.name = name
        self.duration = duration
        self.singer = singer
        self.year = year
        self.playing = False
        self.start_time = None
        self.played_time = 0
        self.end = False
        self.seconds_dur = self.seconds(duration)

    def seconds(self, duration):
        return int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    def __repr__(self):
        return f"{self.name} - {self.singer} ({self.year})"


# Пример использования
album = Album()
album.album_info('music.txt')
album.play('tangled up in blue')
album.pause('tangled up in blue')
album.play('tangled up in blue')




import datetime
import time

class Album:
    album_tuple = {}

    @classmethod
    def album_info(cls, file):
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                name, duration, singer, year = line.strip().split(' - ')
                result = Track(name, duration, singer, year)
                cls.album_tuple[name] = {
                    'duration': result.seconds_dur,
                    'singer': result.singer,
                    'year': result.year,
                    'played_time': result.played_time,
                    'playing': result.playing,
                    'start_time': result.start_time,
                    'end': result.end
                }

    def play(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            duration = track_info['duration']
            singer = track_info['singer']
            played_time = track_info['played_time']
            playing = track_info['playing']

            if not playing:  # Если трек не играет
                print(f'Starting to play composition {track_name} by {singer}')
                track_info['playing'] = True  # Устанавливаем, что трек играет
                track_info['start_time'] = datetime.datetime.now()  # Запоминаем время начала

                while played_time < duration:  # played_time - время проигрывания
                    time.sleep(1)
                    played_time += 1  # Увеличиваем время воспроизведения на 1 секунду
                    track_info['played_time'] = played_time  # Обновляем время воспроизведения
                    print(f'Playing... {played_time} seconds played')

                print(f'Composition {track_name} is now over!')
                track_info['playing'] = False  # Устанавливаем, что трек не играет
                track_info['end'] = True  # Устанавливаем, что трек закончился
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def pause(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            playing = track_info['playing']

            if playing:  # Если трек играет
                print(f'Pausing {track_name}')
                track_info['playing'] = False  # Устанавливаем, что трек не играет
            else:
                print(f'Composition {track_name} is not currently playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def resume(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            playing = track_info['playing']

            if not playing:  # Если трек не играет
                print(f'Resuming {track_name}')
                track_info['playing'] = True  # Устанавливаем, что трек играет
                track_info['start_time'] = datetime.datetime.now()  # Запоминаем время возобновления
                # Здесь можно добавить логику для продолжения воспроизведения с учетом времени паузы
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')

class Track:
    def __init__(self, name, duration, singer, year):
        self.name = name
        self.duration = duration
        self.singer = singer
        self.year = year
        self.playing = False
        self.start_time = None
        self.played_time = 0
        self.end = False
        self.seconds_dur = self.seconds(duration)

    @staticmethod
    def seconds(cls, duration):
        return int(cls.duration.split(':')[0]) * 60 + int(cls.duration.split(':')[1])

    def __repr__(self):
        return f"{self.name} - {self.singer} ({self.year})"


# Пример использования
album = Album()
album.album_info('music.txt')
album.play('tangled up in blue')
album.pause('tangled up in blue')
album.play('tangled up in blue')

'''

import datetime
import time


class Album:
    album_tuple = {}

    @classmethod
    def album_info(cls, file):
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                name, duration, singer, year = line.strip().split(' - ')
                result = Track(name, duration, singer, year)
                cls.album_tuple[name] = {
                    'duration': result.seconds_dur,
                    'singer': result.singer,
                    'year': result.year,
                    'played_time': result.played_time,
                    'playing': result.playing,
                    'start_time': result.start_time,
                    'end': result.end
                }

    def play(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            duration = track_info['duration']
            singer = track_info['singer']
            played_time = track_info['played_time']
            playing = track_info['playing']

            if not playing:  # Если трек не играет
                print(f'Starting to play composition {track_name} by {singer}')
                track_info['playing'] = True  # Устанавливаем, что трек играет
                track_info['start_time'] = datetime.datetime.now()  # Запоминаем время начала

                while played_time < duration:  # played_time - время проигрывания
                    time.sleep(1)
                    played_time += 1  # Увеличиваем время воспроизведения на 1 секунду
                    track_info['played_time'] = played_time  # Обновляем время воспроизведения
                    print(f'Playing... {played_time} seconds played')

                print(f'Composition {track_name} is now over!')
                track_info['playing'] = False  # Устанавливаем, что трек не играет
                track_info['end'] = True  # Устанавливаем, что трек закончился
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def pause(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            playing = track_info['playing']

            if playing:  # Если трек играет
                print(f'Pausing {track_name}')
                track_info['playing'] = False  # Устанавливаем, что трек не играет
            else:
                print(f'Composition {track_name} is not currently playing.')
        else:
            print(f'Track {track_name} not found in the album.')

    def resume(self, track_name):
        if track_name in self.album_tuple:
            track_info = self.album_tuple[track_name]
            playing = track_info['playing']

            if not playing:  # Если трек не играет
                print(f'Resuming {track_name}')
                track_info['playing'] = True  # Устанавливаем, что трек играет
                track_info['start_time'] = datetime.datetime.now()  # Запоминаем время возобновления
                # Здесь можно добавить логику для продолжения воспроизведения с учетом времени паузы
            else:
                print(f'Composition {track_name} is already playing.')
        else:
            print(f'Track {track_name} not found in the album.')


class Track:
    def __init__(self, name, duration, singer, year):
        self.name = name
        self.duration = duration
        self.singer = singer
        self.year = year
        self.playing = False
        self.start_time = None
        self.played_time = 0
        self.end = False
        self.seconds_dur = self.seconds(duration)

    @staticmethod
    def seconds(duration):
        return int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    def __repr__(self):
        return f"{self.name} - {self.singer} ({self.year})"



album = Album()
album.album_info('music.txt')
album.play('tangled up in blue')
time.sleep(5)
album.pause('tangled up in blue')
time.sleep(2)
album.resume('tangled up in blue')
