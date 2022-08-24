class Clientele:
    def __init__(self, f_name,s_name,city, balance):
        self.f_name = f_name
        self.s_name = s_name
        self.balance = balance
        self.city = city
 
    def __str__(self):
        return f'''"{self.f_name} {self.s_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.f_name} {self.s_name},г. {self.city}'
 
clientele_1 = Clientele('Иван','Петров','Москва',50)
clientele_2 = Clientele('Пётр','Иванов','Москва',50)
clientele_3 = Clientele('Иван','Петров','Москва',50)
clientele_4 = Clientele('Пётр','Иванов','Москва',50)
guest_list=[clientele_1, clientele_2, clientele_3, clientele_4]

for guest in guest_list:
    print(guest.get_guest())