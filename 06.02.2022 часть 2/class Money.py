class Money:
    def __init__(self,currency,whole_money, coins):
        self.currency = currency
        self.whole_money = whole_money
        self.coins = coins

    def info(self):
        print(f'whole_money: {self.whole_money}\ncoins: {self.coins}\ncurrency: {self.currency}')

    def redact(self):
        user = input('Какой параметр ты хочешь редактировать\n')
        if user == 'currency':
            user = input('На какую валюту ты хочешь поменять?\n')
            self.currency = user
            return 'замена произошла успешно'
        if user == 'whole_money':
            user = int(input('Ведите сумму\n'))
            self.whole_money = user
            return 'замена произошла успешно'
        if user == 'coins':
            user = input('Введите копейки\n')
            self.coins = int(user)
            return 'замена произошла успешно'


money = Money("гривны", 60, 40)
money.info()
money.redact()
money.info()
