class Book:  # обьявляем класс книга
    def __init__(self, **kwargs):  # создаем коструктор с аргументом **kwargs
        self.dict = kwargs

    def find_string(self, find):  # эта функция будет отвечать за поиск информации о книге
        return self.dict.get(find, False)  # возвращаю значение ключа find

    def set_string(self, set1, value):  # Эта функция отвечает за замену любого параметра
        self.dict[set1] = value  # заменяем на тотЮ который хочет пользователь
        return self.dict  # выводм словарь

    def __repr__(self):
        print(f'name : {self.dict["name"]}\nauthor : {self.dict["author"]}\n'
              f'year : {self.dict["year"]}\ngenre : {self.dict["genre"]}\n'
              f'publisher: {self.dict["publisher"]}\nprice: {self.dict["price"]}')
# name = input('name')
# author = input('author')
# year = input('year')
# genre = input('genre')
# publisher = input('publisher')
# price = input('price')
# book = Book(name=name, author=author, year=year, genre=genre, publisher=publisher, price=price)
# print(book.find_string('name'))
book1 = Book(name='The lord of Rings',
             author="Джон Рональд Руэль Толкин",
             year='2001',
             genre="Fantasy/Adventure",
             publisher='George Allen & Unwin',
             price="759 грн")
print(book1.find_string(find="price"))
print(book1.set_string('name', 'The lord Rings'))
