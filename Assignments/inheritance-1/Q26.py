'''
26. Media Player

Abstract:

MediaPlayer

Derived:

AudioPlayer
VideoPlayer

Implement play functionality.
'''
from abc import ABC,abstractmethod
class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

class AudioPlayer:
    def play(self):
        print("audio player is playing.....")

class VideoPlayer:
    def play(self):
        print("video player is playing.....")

obj1=AudioPlayer()
obj1.play()

obj1=VideoPlayer()
obj1.play()