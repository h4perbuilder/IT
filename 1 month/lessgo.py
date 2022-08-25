# name='islam'
# surname='olegov'
# surname=surname.capitalize()
# print(surname,name)


# age=int(input("age:"))
# if age <= 17:
#     print("sidi doma")
# elif age <= 18 and age < 40:
#     print("lesgo to war")
# elif age <= 40 and age < 60: 
#     print("pashol")
# elif age >= 60 and age <100:
#     print("retirement")
# else:
#     print("spi")


# age=int(input("give a number"))
# if age %2 == 0 :
#     print("even number")
# else:
#     print("odd number")



# 1
# fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Помидор', 'Дыня','Вишня']
# my_favorite_fruits = ['Киви', 'Вишня', 'Арбуз']
# for i in enumerate (my_favorite_fruits,1):
#             print(f'{i} это мой любимый фрукт')



# 2
# lst1 = [1, 3, 5, 7, 9]
# lst2 = [3, 8, 6, 5]
# for lst2 in lst1:
#     if lst2 in lst1:
#         lst1.remove(lst2)
#     print(lst1)


#3 
# lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
# lst2 = []
# a = lst.copy()
# a.extend(lst)
# for i in lst:
#     if i % 2 == 0:
#         qwery = i / 4
#     if i % 2 != 0:
#         qwery = i*2
# print(lst2)


#4
# num = '3384456779'
# print(max(list(num)))


# 5
# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%d %B %Y"))



# разборки с while

# benz=50

# while benz >0:
#     print(f"вы сможете проехать еще {benz*10} км")
#     print(f'у вас осталось {benz} литров бензина!')
#     benz-=10



# list = [2,3,4,5,46,236,546,54,132]
# i = 0
# while True:
#     if list[i] == 132:
#         print('я нашел 132')
#         break
#     print(f'{i}.не нашел')
#     i+=1



# i=0
# while True:
#     if i == 7:
#         break
#     else:
#         print(i)
#     i+=1



# set - множества
# animals = {'crocodile','begemot','jiraf','begemot'}
# print(animals)

# 1
# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# ok = list_names + get_names
# ok = set(ok)
# print(ok)


# 2
# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# ok = list_names + get_names
# sd = set(list_names) - set(get_names)
# print(sd)


# 3
# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# ok = list_names + get_names
# sd = set(list_names) ^ set(get_names)
# print(sd)


# 4
# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# ok = list_names + get_names
# sd = set(list_names) & set(get_names)
# print(sd)


# 5
# my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"
# str = []
# for num in my_str:
#     if num.isdigit():
#         str.append(num)
# print(set(str))
