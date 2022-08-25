class Student:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.books = []
        self.knowledge = 0
        self.is_ready_to_work = False
        self.languages = {}
    
    def add_points(self,points):
        self.knowledge += points
        if self.knowledge >= 1000:
            print("Он(а) готов(а) к работе!")
            self.is_ready_to_work = True
    
    def read_book(self,book):
        self.books.append(book)
        self.add_points(50)

    def do_homework(self):
        self.add_points(25)
    
    def do_projects(self):
        self.add_points(150)
    
    def new_language(self,lang,points):
        if points < 1 or points > 100:
            raise ValueError
        else:
            self.languages[lang] = points
            self.add_points(points)
    
    def info(self):
        return f"Меня зовут: {self.name}, Фамилия: {self.lastname},\nЯ читал такие книги как: {self.books},\nмои баллы: {self.knowledge}"

azi = Student('aziret', 'cho')
azi.do_homework()
azi.read_book("cho")
azi.read_book("a nicho")
azi.do_projects()
azi.new_language('python',80)
azi.new_language('html',20)
# print(azi.info())



# Кошелек
class Purse:
    def __init__(self,valuta,name = "неизвестный"):
        if valuta not in ('usd','kgs'):
            raise ValueError("Только 2 варианта")
        self.money = 0.00
        self.valuta = valuta
        self.name = name
    
    def top_up_balance(self,how_money):
        self.money += how_money

    def pick_up(self,how_money):
        if self.money < how_money:
            print("Недостаточно средств!")
        else:
            self.money -= how_money
        
    def info(self):
        return f"Владелец: {self.name}\n{self.money} - {self.valuta}"

azi = Purse('usd','Aziret')
# azi.top_up_balance(100)
# azi.top_up_balance(20)
# azi.info()
# azi.pick_up(12)
# azi.info()



# Задачник
class To_do:
    to_do_items = []

    def add_to_do(self,obj):
        self.to_do_items.append(obj)

    def list_items(self):
        return self.to_do_items
    
    def find(self,word):
        for i in self.to_do_items:
            if word in i :
                return f"index: {self.to_do_items.index(i)}: {i}"

class TodoItems:
    def __init__(self, task):
        self.task = task 
        self.is_done = False
    
    def check(self):
        self.is_done = True
    
    def uncheck(self):
        self.is_done = False

todo = To_do()
todo1 = TodoItems('learn python')
todo2 = TodoItems('books')
todo.add_to_do(todo1.task)
todo.add_to_do(todo2.task)
# print(todo.list_items())
# print(todo.find('python'))
