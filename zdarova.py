# integer- 1,300,4325
# float-1,4,1.67
# string-'rating'
# bool- true,false


# one=1
# two=1.324
# three="hello people"
# four= True
# print(type(four))


# num1,num2,num3=1,2,3
# print(num3)


# name,surname,age="john","doe",20
# print(age)



# String-Строка
# name="johnjohnjohn"
# surname='natasha it\'s \nbeautiful girl'
# bio="""
# John Nash is s talented Python developer.
# He works at Google.
# """
# print(surname)



# name='Josh'
# surname='Nash'
# company='Google'
# bio="""
# {0} {1} is a talented Python developer.
# He works at {2}.
# """.format(name,surname,company)
# print(bio)



# name = 'John'
# surname = 'Nash'
# company = 'Google'
# bio = f"{name} {surname} is a talented Python developer.\nHe works at {company}."

# print(bio)
# """
# Мы получим следующее:

# John Nash is a talented Python developer.
# He works at Google.

# """



# bio = "John" + " Nash" + " is a talented Python developer.\nHe works at " + "Google"
# #  обратите внимание на пробелы. Пробел для питона считается отдельным символом

# print(bio)
# """
# Мы получим следующее:

# John Nash is a talented Python developer.
# He works at Google.

# """

# name = 'john'
# surname = 'Nash'  
# age = 25 

# print(name + " " + surname + ". He is " + str(age) + " years old")


# text='ok LESSGO'
# print(text.rjust(40),"omg nigga")


# условия

# age=int(input("age:"))
# if age <= 17:
#     print("sidi doma")
# elif age >=18 and age < 40:
#     print("lesgo to war")
# elif age >=40 and age < 60: 
#     print("pashol")
# elif age >=60 and age < 100:
#     print("retirement")
# else:
#     print("spi")



# Списки и срезы
# List-списки-[1,2,3]  изменяемые
# Tuple-кортежи-(1,2,3) неизменяемые
# Dict-словарь-{'азирет':3,
# 3:"toop"
# } изменяемые

# a=[1,2,3,True,"string",[1,3,54],1.54]
# b=[3,2,4,7,5,1,6]
# print(a[2],a[1])#индексы
# print(a[1:5])#срезы
# a.insert(4,'islam')
# a.extend(b)


# my_list = ['cde', 'fgh', 'abc', 'klm', 'opq']
# list_2 = [3, 5, 2, 4, 1]
# my_list.sort()
# list_2.sort()
# print(my_list)
# print(list_2)


# contact_name=['aidana','aziret','oleg','islam','pamir']
# name=(input('Введите имя: '))
# if name in contact_name:
#     print("Есть в контактах",name.title())
# else:
#     print("Нет,пошел отсюда")


# a=[1,2,4,54,45,3]
# c=[]
# c.append(a)
# for i in a:
#     print(i*2)


# b=[2,4,8,108,90,6]
# for i in b:
#     print(i**2)



# циклы
# for i in range(10):
#     print('aziret')



# List-списки-[1,2,3] # изменяемые
# Tuple-кортежи-(1,2,3) # неизменяемые
# Dict-словарь-{
# 'азирет':3,
# 3:"toop"
# 'hel':True
# } #изменяемые
# set-множества-{3,4,5,4,3,5} #может хранить только уник.значения #изменяемые


# кортеж(tuple)
# data = ()
# print(type(data))

# student={'name':'oleg','age':344}
# stud2=dict(name='aziret',age=56)
# name=student.pop('age')
# print(student)
# print(name)


#values 
# student=dict(name='oleg',age=344)
# print(student.values())
# items=list(student.values())
# print(items)

# get
# student = dict (name='oleg',age=344)
# print(student.get('name'))
# print(student.get('lastname'))
# print(student.get('lastname','no keys'))



# contact_name={
#     'aidana':775151506,
#     'aziret':775151507,
#     'oleg':775151508,
#     'islam':775151509,
#     'pamir':775151510
# }
# act=input('выберите действие:'
# '\n1-добав.контакт'
# '\n2-удалить контакт'
# '\n3-поиск контакта'
# '\n4- просмотр контакта')
# while True:
#     if act == 1:
#         name= input('введите имя:')
#         if contact_name.get(name.title):
#             print('есть делай новый чорт')
#             break
#         phone=int(input('Номер:'))
#         contact_name[name]=phone
#         print(contact_name)
#     elif act==2:
#         name= input('введите имя:')
#         if contact_name.get(name.title):
#             contact_name.pop(name.title)
#             print('удалил')
#         else:
#             print('нет пошел отсюда')
#             break

