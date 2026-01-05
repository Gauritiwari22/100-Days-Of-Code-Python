"Day17"

# Creating our own classes in python
class User:
    pass   #used when nothing is to written inside a class and continue with objects


user1=User()
user1.ID="001"
user1.username="Richard"

# the __init__() function- used for initialising attributes
class Car:

    def __init__(self,name,seats,color,speed): #whenever an object is created using Car class theis function will run
        self.name=name
        self.seats=seats
        self.color=color
        self.speed=speed
        

    def compare(self,other):
        if self.speed>other.speed:
            print(f"{self.name} is better than {other.name}.")
        elif self.speed<other.speed:
            print(f"{other.name} is better than {self.name}.")
        else:
            print(f"{self.name} and {other.name} are equally good.")

        

Fortuner=Car("Fortuner",7,"white",200)
Scorpio=Car("Scorpio",7,"red",100)
print(Fortuner.seats)
print(Scorpio.speed)
print(Scorpio.color)
Fortuner.compare(Scorpio)


