class Car:  # обьявляем класс машина
    def __init__(self, **kwargs):  # создаем коструктор с аргументом **kwargs
        self.dict = kwargs

    def find_string(self, find):  # эта функция будет отвечать за поиск информации о машине
        return self.dict.get(find, False)  # возвращаю значение ключа find

    def set_string(self, set1, value):  # єта функция отвечает за замену любого параметра
        self.dict[set1] = value  # заменяем на тотЮ который хочет пользователь
        return self.dict  # выводим словарь

# model = input('Model car:\n')
# year_rel = input('Year release:\n')  это вариант с вводом пользователя можно раскоментировать
# who_made = input('Who made this cer(company):\n')
# size_motor = input('Size of motor:\n')
# color = input('color:\n')
# price = input('Price:\n')
# object_1 = Car(model=model,year_rel=year_rel,who_made=who_made,size_motor=size_motor,color=color,price=price)
data = """\nmodel\nyear_rel\nwho_made\nsize_motor\ncolor\nprice\n"""  # сделал перем где будут хранится данные о машине
object_2 = Car(model='toyota', year_rel=1999, who_made='toyota', size_motor='123 cm', color='blue', price=3058.99)
print(object_2.find_string(find='model'))
object_2.find_string(find='year_rel')
object_2.find_string(find='who_made')
object_2.find_string(find='size_motor')
object_2.find_string(find='color')
object_2.find_string(find='price')
user = input(f'какие данные ты хочешь узнать, список данных:{data}')  # тут узнаем у пользователя что он хочет узнать
print(object_2.find_string(find=user))  # и выводим ему это
print(object_2.set_string('model', 'skoda'))
