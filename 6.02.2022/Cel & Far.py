class Tempreture:  # создал класс
    count = 0  # создаю счетчик

    @staticmethod
    def f_to_c(f):
        """Эта функция отвечает за перевод с фаренгейта в цельсий"""
        Tempreture.count += 1  # обращаюсь к нашему классу и добавляю к счетчику 1
        return (f-32) * 5/9  # возвращаю градусы в цельсиях

    @staticmethod
    def c_to_f(c):
        """Эта функция отвечает за перевод с цельсия в фаренгейт"""
        Tempreture.count += 1  # добавляю к счетчику 1
        return (c*1.8000) + 32  # возвращаю градусы в фаренгейте

    @staticmethod
    def countc():
        """Эта функция возвращает количество сделанных переводов темпратур"""
        return Tempreture.count

# результаты сравнивал в гугле


print(Tempreture.c_to_f(9))
print(Tempreture.f_to_c(3))
print(Tempreture.count)
