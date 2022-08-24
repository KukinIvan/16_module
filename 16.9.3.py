class Clientele:
    def __init__(self, f_name,s_name,city, balance):
        self.f_name = f_name
        self.s_name = s_name
        self.balance = balance
        self.city = city
 
    def __str__(self):
        return f'''"{self.f_name} {self.s_name}". {self.city}. Баланс: {self.balance} руб.'''
 
clientele_1 = Clientele('Иван','Петров','Москва',50)
print(clientele_1)