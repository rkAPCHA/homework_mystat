class Fraction:  # создаю класс
    count = 0  # создаю счетчик

    def __init__(self, caliber, amount):  # создаю конструктор в котором будут хранится калибр и количество патронов
        Fraction.count += 1  # обращаюсь в наш класс и добавляю к нему 1
        self.caliber = caliber
        self.amount = amount

    @staticmethod
    def count_class():
        """Эта функция отвечает за возврат количество созданых обьектов класса"""
        return Fraction.count


fraction = Fraction(12.3, 40)
fraction1 = Fraction(13.3, 20)
fraction2 = Fraction(11.1, 26)
print(Fraction.count)
