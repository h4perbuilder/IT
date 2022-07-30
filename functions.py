# def Hello():
#     print('hello americans')

# def Bye():
#     print('hello chinese')

# Hello()
# Bye()


# def cho(x):
#     if x>=0:
#         return True
#     else:
#         return False


# a = [1,-353,4,-5,34,-434,-356,6,-24]
# p = []
# for i in a:
#     if cho(i):
#         p.append(i)
# print(p)




# def calculation():
#     a = int(input('Введите число: '))
#     b = int(input('Введите число: '))
#     operation = input('''
# + для плюса 
# - для минуса
# * для умножения
# / для деления
# ''')

#     if operation == '+':
#         print(a + b)

#     elif operation == '-':
#         print(a - b)

#     elif operation == '*':
#         print(a * b)

#     elif operation == '/':
#         print(a / b)

#     else:
#         print('pashol')

# calculation()




#lambda- анонимная функция

# def sum_two(a,b):
#     return a*b

# print(sum_two(23,32))



# f = lambda a,b: a*b
# print(f(324,43))

# print((lambda x,y: x/y)(10,5))



# встроенные функции
# -------map()------
# синтаксис: map(function,*iterables)

# 1
# my_notebooks = ['macentosh','acer','lenovo','asus','mac','samsung']
# da=[]
# for i in my_notebooks:
#     ok = i.upper()
#     da.append

# 2
# my_notebooks = ['macentosh','acer','lenovo','asus','mac','samsung']
# print(list(map(len,my_notebooks)))

# 3
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.50013]
# print(list(map(round,circle_areas)))
# print(round(23.5456))

# 4
# my_notebooks = ['macentosh','acer','lenovo','asus','mac','samsung',4]
# print(list(map(lambda x: x*2,my_notebooks)))

# -------filter()------
# синтаксис: filter(function,*iterables)

# 1
# scores = [66,90,68,59,76,60,88,74,81,65]
# print(list(filter(lambda x: x > 75,scores)))

# 2
# mixed = ['мак','просо','мак','мак','просо','мак','просо','просо','просо','мак']
# print(list(filter(lambda x: x[0] in 'мак' , mixed)))

# 3
# dromes = ['анна','жанна','rewire','madam','freer','anutuna','kiosk']
# print(list(filter(lambda word: word == word[::-1] , dromes)))

#-----practice-----
# def new_order():
#     answer = input('будете делать заказ? \n y/n: ')
#     if answer =='y':
#         return True
#     elif answer =='n':
#         exit()

# def get_order(ingredients):
#     order = []
#     for ing in ingredients:
#         command = input(f'добавить:{ing}; \n y/n: ')
#         if command == 'y':
#             order.append(ing)
#     return order

# def check_order(order):
#     if not order:
#         print('ничего не заказывали')
#         new_order
#     for ing in order:
#         print(ing)
#     res = input('верный ли ваш заказ \n y/n: ')
#     if res == 'y':
#         print('ваш заказ принят! ожидайте 5 мин')
#         return True
#     elif res =='n':
#         return new_order()

# def main():
#     ingredients = ['майонез','шпрот','кетчуп','сыр','колбаса','рыба']
#     new_order()
#     order = get_order(ingredients)
#     if check_order(order):
#         exit()
# main()
#-----practice-----


# *args **kwargs
# args - arguments
# kwargs - keyword arguments

# def num(*args):
#     sum = 0
#     for n in args:
#         sum += n
#         print(sum)

# num(234,2312,324,54,4)

# 2
# a = [1,2,3,4]
# b = [3,4,5,8,*a,9,84]
# print(b)

# 3



# moduls
# def plus(a,b):
#     return(a*b)
# plus(6,2)







# def calc(num1,num2,value):
#     if value == '+':
#         return num1 + num2
#     if value == '-':
#         return num1 - num2
#     if value == '*':
#         return num1 * num2
#     if value == '/':
#         return num1 / num2
# calc()

# decorator
def inc(x):
    return x+1