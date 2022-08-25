import requests
import json

class User:
    def __init__(self, url):
        self.url = url
    
    def get_users(self):
        result = requests.get(self.url)
        return result.json()
    
    def create_user(self, first_name, last_name, username, email, password):
        result = requests.post(self.url, data={"first_name": first_name, 
                                                "last_name": last_name,
                                                "username": username,
                                                "email": email,
                                                "password": password})
        if result.status_code == 200 or result.status_code == 201:
            return "Пользователь успешно создан"
        else:
            return "Ошибка!", result.status_code
    
    def change_last_name(self, id_user, last_name):
        user_info = self.get_user(id_user)
        if user_info:
            user_info['last_name'] = last_name

            print(user_info)
            print(f"{self.url}{id_user}/")
            result = requests.put(f"{self.url}{id_user}/", data=user_info)

            print(result.status_code)
            if result.status_code == 200 or result.status_code == 201:
                return f"last_name успешно изменен на {last_name}"
            else:
                return "Ошибка!", result.status_code
        else:
            return "Такого пользователя нет"

    def change_first_name(self, id_user, first_name):
        user_info = self.get_user(id_user)
        if user_info:
            user_info['first_name'] = first_name

            print(user_info)
            print(f"{self.url}{id_user}/")
            result = requests.put(f"{self.url}{id_user}/", data=user_info)

            print(result.status_code)
            if result.status_code == 200 or result.status_code == 201:
                return f"first_name успешно изменен на {first_name}"
            else:
                return "Ошибка!", result.status_code
        else:
            return "Такого пользователя нет"

    def get_user(self, id_user):
        try:
            result = requests.get(f"{self.url}{id_user}")
            if result.status_code == 200:
                return result.json()
            else:
                return None
        except Exception as ex:
            print('error', ex)


user = User(url='https://nuranov29.pythonanywhere.com/users/')
# first_name = input('first_name:')
# username = input('username:')
# email = input('email:')
# password = input('password:')
# print(user.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password))
# id_user = int(input('id_user:'))
# last_name = input('last_name:')
# print(user.change_last_name(id_user=id_user, last_name=last_name))