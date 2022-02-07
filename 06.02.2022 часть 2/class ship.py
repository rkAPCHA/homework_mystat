class Ship:
    def __init__(self, people, cannons, weight):
        self.people = people
        self.cannons = cannons
        self.weight = weight

    def ship_is_ready(self):
        return 'ship is ready'

    def ship_is_not_ready(self):
        return 'ship isn`t ready'


class Fregat(Ship):
    def info(self):
        return f'people: {self.people}, cannons : {self.cannons}, weight: {self.weight}'

    def fregat_is_ready(self):
        if self.people == 0:
            print('where is everyone? immediately call all lazy people aboard the ship!')
            return Ship.ship_is_not_ready(self)

        elif self.cannons >= 60:
            print('ship is overload! We need to throw some cannons overboard!')
            return Ship.ship_is_not_ready(self)
        else:
            return Ship.ship_is_ready(self)


class Destroyer(Ship):
    def info(self):
        return f'people: {self.people}, cannons : {self.cannons}, weight: {self.weight}'

    def destroy_submarine(self):
        return 'submarin destroyed'

    def destroy_enemyships(self):
        return 'ship destroyed'

    def people_afterfight(self):
        return f'after fight {self.people-20} survived'


class Cruiser(Ship):
    def info(self):
        return f'people: {self.people}, cannons : {self.cannons}, weight: {self.weight}'


    def drive(self):
        return f'мы выдвигаемся! с кораблем весом {self.weight}'

    def drown(self):
        return f'мы тонем... а точнее около {self.people}'


fregat = Fregat(0,76,4000)
destroyer = Destroyer(345,10, 10000)
cruiser = Cruiser(200, 7, 4000)
print(fregat.fregat_is_ready())

