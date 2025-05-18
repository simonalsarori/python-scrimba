class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

films = [film_1,film_2]
print(films[1].title,films[0].title)
films[0].nice_print()

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

#################################################
#inhertance

class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces")
        
class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")
    
    
character1=Wizard()
character1.move()


#############################
#model
from platform import python_version as pv ,system

print(pv())

#or
import platform, string, os

print(platform.python_version())