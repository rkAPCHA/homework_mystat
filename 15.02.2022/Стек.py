class Stack:
    def __init__(self, block):
        self.storage = []
        self.limit = block

    def add_new_item(self, value):
        if len(self.storage) == self.limit:
            print('вы не сможете ничего добавить, из-за ограничения!')
            return False
        self.storage.append(value)
        return True

    def __repr__(self):
        print(f'f{self.storage}')

    def del_item(self):
        return self.storage.pop()

    def count_el(self):
        return len(self.storage)

    def is_empty(self):
        return True if len(self.storage) == 0 else False

    def is_full(self):
        return False if len(self.storage) == 0 else True

    def ochistka(self):
        self.storage = []
        return 'очистка произошла успешно'

    def intresting(self):
        return self.storage[-1]

    def more_limit(self, limit):
        self.limit = limit
        return True

    @staticmethod
    def menu():
        print('''Вызовите метод add_new_item, чтобы добавить элемент к стеку
        Вызовите метод del_item, чтобы удалить елемент с стека
        Вызовите метод count_el, чтобы посчитать  елементы стека
        Вызовите метод is_empty, чтобы проверить, является ли стек пустым
        Вызовите метод is_full, чтобы проверить, является ли стек полным
        Вызовите метод ochistka, чтобы очистить стек
        Вызовите метод intresting, чтобы поинтресоватся какой элемент стека последний
        Вызовите метод more_limit, чтобы расширить лимит на кол-во эелементов в стеке''')


steck = Stack(5)
steck.add_new_item('add')
steck.add_new_item({4: 'red'})
steck.add_new_item('f')
steck.add_new_item('r')
steck.add_new_item('g')
steck.add_new_item(78)
steck.del_item()
