from oop4 import Verification

class V2(Verification):

    def save(self):
        with open('user.txt') as new:
            for i in new:
                if f'{self.login, self.password}\n' == i:
                    raise ValueError('Логин занят')
        Verification.save(self)

user = V2('cuma', 'cho12345')
user.save()
# tempmail