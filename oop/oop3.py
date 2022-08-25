# Наследование

# class Animal:
#     def __init__(self,age,gender,racion):
#         self.age = age
#         self.gender = gender
#         self.racion = racion

#     def feed(self):
#         if self.racion == 'meat':
#             return 'Какое вкусное мясо'
#         else:
#             return 'Я люблю траву'
    
#     def make_sound(self):
#         pass



class Publication:
    def __init__(self,name,date,pages,library,type):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type = type


    def get_code_in_library(self):
        date_code = self.date.replace(',','')
        return f'{self.library[:2]},{self.type},{self.name[:2]},{self.pages},{date_code}'

class Book(Publication):
    def __init__(self, name, date, pages, library):
        super().__init__(name, date, pages, library, type)
        self.type = 'book'
    

class Magazine(Publication):
    def __init__(self, name, date, pages, library):
        super().__init__(name, date, pages, library, type)
        self.type = 'magazine'


class Newspaper(Publication):
    def __init__(self, name, date, pages, library):
        super().__init__(name, date, pages, library, type)
        self.type = 'newspaper'


algorithms = Book('How to cho', '10.08.2022', 200, 'itacademy')
# print(algorithms.get_code_in_library())



import random

class Player:
    playlist = []
    
    def add_to_playlist(self,song):
        self.playlist.append(song)
        
    def play(self,song):
        for song in self.playlist:
            print(song)

    def delete_from_playlist(self,song):
        self.playlist.remove(song)

    def shuffle(self):
        random.shuffle(self.playlist)

class AudioPlayer(Player):
    pass

class VideoPlayer(Player):
    pass


audioplayer = AudioPlayer()
# audioplayer.add_to_playlist('синий трактор')
# audioplayer.add_to_playlist('акуленок')
# audioplayer.add_to_playlist('immigrant song')
# audioplayer.add_to_playlist('cho')
# audioplayer.add_to_playlist('pashol')
# audioplayer.shuffle()
# audioplayer.play()