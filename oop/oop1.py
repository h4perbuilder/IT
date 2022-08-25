# ООП - объектно-ориентированное программирование

# наследование
# инкапсуляция
# полиморфизм

class Car:
    brand = 'toyota'
    model = 'supra'
    year = 2004
    owner = 'aziret'

    def info(self):
        return f"info: {self.brand},{self.model},{self.year},{self.owner}"

mycar = Car()
# print(mycar.info())

class Car2: # класс
    def __init__(self, brand, model,year,owner, odometr, type_of, volue): # магический метод
        self.b = brand # атрибут класса
        self.model = model 
        self.year = year 
        self.owner = owner 
        self.odometr = odometr 
        self.type_of = type_of 
        self.volue = volue 
        self.is_going = False
    
    def info2(self): #обычный метод
        return f"info: {self.b}, {self.model}, {self.year}, {self.owner}, {self.type_of}, {self.volue}, \nмашина едет: {self.is_going}, скорость: {self.odometr}"
    
    def car_is_going(self, km):
         self.odometr += km 
         self.is_going = True
         
    def cat_not_going(self):
        self.is_going = False 
        self.odometr = 0

    def car_update_name(self,name):
        self.b = name

car2 = Car2("Tesla", 'S', 2016, 'Ilon', 50, 'sport', 3.5)
# car2.car_is_going(500)
# car2.cat_not_going()
# car2.car_update_name('cho')
print(car2.info2())


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def info(self):
    return f"Имя: {self.name}, возраст:{self.age}"


class Cat(Animal):
    def sound(self):
        return 'миау'

cat1 = Cat('Oleg',3)
# print(cat1.info())


class Dog(Animal):
    def sound(self):
        return 'ГАв ГАв'
    
dog1 = Dog('Oleg',3)
# print(dog1.info())
# print(Animal.info())
