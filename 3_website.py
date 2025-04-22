import pygame
import time


class Track:
    """
    Class representing a composition in a music player
    """
    def __init__(self, name, duration, singer, year):
        self.name = name
        self.duration = duration
        self.singer = singer
        self.year = year
        self.filepath = f'music/{self.name}.mp3'
        self.playing = False
        self.played_time = 0
        self.seconds_dur = self.seconds(duration)

    @staticmethod
    def seconds(duration):
        return int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    def __repr__(self):
        return f"{self.name} - {self.singer} ({self.year})"


class Album:
    """
    Class representing a music player
    """
    album_tuple = {}

    @classmethod
    def album_info(cls, filename):
        """
        Method album_info(self, filename): to read the information from the file
        :param filename: the name of the file where data is stored
        """
        with open(filename, 'r') as file:
            for line in file:
                name, duration, artist, year = line.strip().split(' - ')
                track = Track(name, duration, artist, year)
                cls.album_tuple[name] = track

    def play(self, name):
        """
        Method play(self, name): to start the composition playback
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track = self.album_tuple[name]

            if track.playing == False:
                print(f'Starting to play composition {track.name} by {track.singer}')
                track.playing = True
                pygame.mixer.init()
                pygame.mixer.music.load(track.filepath)
                pygame.mixer.music.play()
            elif track.playing == 'flag':
                track.playing = True
                pygame.mixer.music.play(start=track.played_time)
            else:
                print(f'Composition {track.name} is already playing. Didn\'t you hear it? :)')

            for i in range(tiime):
                if track.played_time < track.seconds_dur:
                    time.sleep(1)
                    track.played_time += 1
                    print(f'Playing some musiiiic for... {track.played_time} seconds')
                else:
                    print(f'Composition {track.name} is now over!')
                    track.playing = False
                    track.played_time = 0
                    pygame.mixer.music.stop()

        else:
            print(f'Track {name} not found in the album :(')

    def pause(self, name):
        """
        Method pause(self, name): to pause the composition
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track = self.album_tuple[name]

            if track.playing:
                print(f'Pausing {track.name}')
                track.playing = False
                pygame.mixer.music.pause()
            else:
                print(f'Composition {track.name} is not currently playing.')
        else:
            print(f'Track {name} not found in the album :(')

    def resume(self, name):
        """
        Method resume(self, name): to resume (continue) the composition playback
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track = self.album_tuple[name]
            if not track.playing:
                print(f'Resuming {track.name}')
                track.playing = 'flag'
                pygame.mixer.unpause()
                Album.play(self, name)

            else:
                print(f'Composition {track.name} is already playing. Don\'t try to trick my code! :)')

    def stop(self, name):
        """
        Method stop(self, name): to stop the composition playback
        :param name: the name of the composition
        """
        if name in self.album_tuple:
            track = self.album_tuple[name]

            if track.playing:
                print(f'Stopping {track.name}')
                track.playing = False
                pygame.mixer.music.stop()
                track.played_time = 0
            else:
                print(f'Composition {track.name} is not currently playing.')
        else:
            print(f'Track {name} not found in the album :(')


album = Album()
album.album_info('music.txt')

tiime = int(input('for what time u want a track playing '))
album.play('here_comes_the_sun')
#time.sleep(tiime)
album.pause('here_comes_the_sun')
#time.sleep(2)
tiime = int(input('for what time u want a track playing '))
album.resume('here_comes_the_sun')

