class Stadion:  # обьявляем класс стадион
    def __init__(self, **kwargs):  # создаем коструктор с аргументом **kwargs
        self.dict = kwargs

    def find_string(self, find):  # эта функция будет отвечать за поиск информации о стадионе
        return self.dict.get(find, False)  # возвращаю значение ключа find

    def set_string(self, set1, value):  # Эта функция отвечает за замену любого параметра
        self.dict[set1] = value  # заменяем на тотЮ который хочет пользователь
        return self.dict  # выводим словарь


# name = input('name')
# year = input('year')
# city = input('city')
# capacity = input('capacity')
# stadion = Stadion(name=name, year=year, city=city, capacity=capacity)
stadion1 = Stadion(name='Первое мая', year='1986', city='Пьхеньян', capacity='114 000')
print(stadion1.find_string('year'))
stadion1.set_string('city', 'Москва')