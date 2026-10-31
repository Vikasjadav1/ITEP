'''
. Write a Java program to create a class called "MusicLibrary" with a collection of songs and 
methods to add and remove songs, and to play a random song.
'''
import random
class MusicLibrary:
    musics=[]
    
    def add_song(self,song):
        self.__song=song
        MusicLibrary.musics.append(song)

    def remove_song(self,song):
        if song in MusicLibrary.musics:
            MusicLibrary.musics.remove(song)
            print("removed.....................")

    def random_song(self):
        if MusicLibrary.musics:
            song = random.choice(MusicLibrary.musics)
            print("Now playing:", song)
        else:
            print("No songs available")
            


sng=MusicLibrary()
sng.add_song("saiyara")
sng.add_song("pkkkkkkkkk")
sng.add_song("samjhawana")

sng.remove_song("samjhawana")

print(MusicLibrary.musics)


sng.random_song()