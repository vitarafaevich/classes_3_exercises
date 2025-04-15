#evening, is working

import time
import pygame

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

    def album_info(self, filename):
        """
        Method album_info(self, filename): to read the information from the file
        :param filename: the name of the file where data is stored
        """
        self.album_tuple = {}
        with open(filename, 'r') as file:
            for line in file:
                name, duration, artist, year = line.strip().split(' - ')
                track = Track(name, duration, artist, year)
                self.album_tuple[name] = track

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
                #pygame.mixer.music.play(start=track.played_time)
                Album.play(self, name)
                #pygame.mixer.music.unpause()

            else:
                print(f'Composition {track.name} is already playing. Don\'t try to trick my code! :)')

    def stop(self, name):
        if name in self.album_tuple:
            track = self.album_tuple[name]

            if track.playing:
                print(f'Stopping {track.name}')
                track.playing = False
                pygame.mixer.music.stop()
                #track.played_time = 0
            else:
                print(f'Composition {track.name} is not currently playing.')
        else:
            print(f'Track {name} not found in the album :(')


album = Album()
album.album_info('music.txt')

tiime = int(input('for what time u want a track playing '))
album.play('here_comes_the_sun')
time.sleep(tiime)
album.pause('here_comes_the_sun')
time.sleep(2)
tiime = int(input('for what time u want a track playing '))
album.resume('here_comes_the_sun')


'''
import datetime
import time
from pygame import mixer


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
                
                #edited
                print(f'Starting to play composition {name}...')
                track_info['playing'] = True
                #track is still playing
                while not track_info['end'] == True and track_info['playing'] == True:
                    time.sleep(1)
                    played_time += 1
                    track_info['played_time'] = played_time
                    print(f'Playing some musiiiic for... {played_time} seconds')
                if track_info['end'] == True:
                    print(f'Composition {name} is now over!')
                    track_info['playing'] = False
                    track_info['end'] = True
                

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
        Method pause(self, name): to pause the composition
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
album.play('aura')
time.sleep(5)
album.pause('aura')
album.play('riders')
'''




'''
class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
'''