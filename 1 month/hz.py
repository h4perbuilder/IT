# n = (4, 5)
# a,b = n
# print(a)

# data = ['ACME', 50, 91.1,(2021,12, 21)]
# name,age,height,*date = data
# print(date)


# 2
# record = ('Kuma', 'kuma04@example.com', '773-555-112', '555-555-212')
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname,*fields = line
# print(uname)




# 1
import re

# line = 'asdf fjdk; afed, fjek,asdf,    foo'
# a = re.split(r'[;,\s]\s*',line)
# print(a)

# 2
# filename = 'spam.txt'
# url = 'http://www.python.org'  
# print(filename.endswith('.txt'))


# 3
# text = 'yeah,but no, but yeah, but no, but yeah'
# b = re.sub(r'but','ok',text)
# print(b)

# 4
# result = re.findall(r'map', 'Карта google map и объект yandexmap - это разные вещи')
# print(result)


# 5
# text = 'UPPER PYTHON, lower python, Mixed Python'
# c = re.sub('python', 'cho', text, flags=re.IGNORECASE)
# d = re.findall('python', text ,flags=re.IGNORECASE)
# print(c)
# print(d)