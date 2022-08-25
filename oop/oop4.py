# class Verification:
#     def __init__(self,login,password):
#         self.login = login
#         self.password = password
    
#     def lenPassword(self):
#         if len(self.password) < 8:
#             raise ValueError('Слабый пароль')

#     def save(self):
#         with open('user.txt','a',encoding='utf-8') as new:
#             new.write(f'{self.login, self.password}\n')

# cho = Verification('cuma','cho12345')
# cho.lenPassword()
# cho.save()


# Множественное наследование
class Doctor:
    def voice(self):
        print('Я доктор умею лечить как доктор')

class Builder:
    def voice(self):
        print('Я строю умею строить')

class Person(Builder,Doctor):
    # pass
    def voice(self):
        print('чо а ничо')

azi = Person()
# azi.voice()


# Машина
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type 
        self.year = year 
    
    def start(self):
        return 'Машина заведена'

    def stop(self):
        return 'Машина заглушена'

    def car_update_year(self,new_year):
        self.year = new_year
    
    def car_update_type(self,new_type):
        self.type = new_type
    
    def car_update_color(self,new_color):
        self.color = new_color

car = Car('','','')
car.car_update_color('white')
car.car_update_type('sport')
car.car_update_year(2001)
# print(car.color, car.type, car.year)
# print(car.start)
# print(car.stop)

