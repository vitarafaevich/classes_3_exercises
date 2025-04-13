"""
временное моделирование, чтобы можно было запускать и останавливать трек
с правильного места
пауза плей => продолжает с того места

в альбоме после одного трека начинается следующий
"""
import datetime
import time


class Album:
    """
    Class representing a music player
    """
    album_tuple = {}

    @classmethod
    def album_info(cls, file):
        """
        Static method album_info(cls, file): to read the information from the file
        :param cls: referring to current class
        :param file: the name of the file where data is stored
        """
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

    def play(self, name):
        """
        Method play(self, name): to start the composition playback
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track_info = self.album_tuple[name]
            duration = track_info['duration']
            singer = track_info['singer']
            played_time = track_info['played_time']
            playing = track_info['playing']

            #defeat None in playing
            if not playing:
                print(f'Starting to play composition {name} by {singer}')
                track_info['playing'] = True
                track_info['start_time'] = datetime.datetime.now()

                while played_time < duration:
                    time.sleep(1)
                    played_time += 1
                    track_info['played_time'] = played_time
                    print(f'Playing some musiiiic for... {played_time} seconds')

                print(f'Composition {name} is now over!')
                track_info['playing'] = False
                track_info['end'] = True
            else:
                print(f'Composition {name} is already playing. Did\'nt u hear it? :)')
        else:
            print(f'Track {name} not found in the album :(')

    def pause(self, name):
        """
        Method play(self, name): to pause the composition
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track_info = self.album_tuple[name]
            playing = track_info['playing']

            if playing:
                print(f'Pausing {name}')
                track_info['playing'] = False
            else:
                print(f'Composition {name} is not currently playing.')
        else:
            print(f'Track {name} not found in the album :(')

    def resume(self, name):
        """
        Method play(self, name): to resume (continue) the composition playback
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track_info = self.album_tuple[name]
            playing = track_info['playing']

            if not playing:
                print(f'Resuming {name}')
                track_info['playing'] = True
                track_info['start_time'] = datetime.datetime.now()

            else:
                print(f'Composition {name} is already playing. Don\'t try to trick my code! :)')
        else:
            print(f'Track {name} not found in the album :(')


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
album.play('stairway to heaven')
time.sleep(5)
album.pause('stairway to heaven')
time.sleep(2)
album.resume('tangled up in blue')
