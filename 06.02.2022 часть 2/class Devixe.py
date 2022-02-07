class Device:
    def __init__(self, mader, material, color):
        self.mader = mader
        self.material = material
        self.color = color


    def start(self):
        print('Device is running')


class CoffeeMachine(Device):
    def __init__(self, mader, material, color, **kwargs):
        super().__init__(mader, material, color)

        self.kwargscoffe = kwargs

    def info(self):
       return f'model:{self.kwargscoffe["model"]}, material: {self.material},'\
             f'mader:{self.mader},functions:{self.kwargscoffe["functions"]},color:'\
             f'{self.color}, broken: {self.kwargscoffe["broken"]}'

    def start_make_coffee(self):
        print('start making coffee')


class Blender(Device):
    def __init__(self, mader,material,color ,**kwargs):
        super().__init__(mader,material,color)
        self.kwargsblender = kwargs

    def info(self):
        return f'model:{self.kwargsblender["model"]}, material: {self.material},'\
              f'mader:{self.mader},functions:{self.kwargsblender["functions"]},color:'\
              f'{self.color}, broken: {self.kwargsblender["broken"]}'

    def start_blender(self):
        print('start blendering')


class MeatGrinder(Device):
    def __init__(self, mader, material, color, **kwargs):
        super().__init__(mader, material, color)
        self.kwargsmeat = kwargs
    def info(self):
        return f'model:{self.kwargsmeat["model"]}, material: {self.kwargsmeat["material"]},'\
              f'functions:{self.kwargsmeat["functions"]},'\
              f'color:{self.kwargsmeat["color"]}, broken: {self.kwargsmeat["broken"]}'

    def grind_meat(self):
        print('arharharr, i hate this meat!!!')


device = Device(mader='lomko',material='metalik',color='purple')
coffem = CoffeeMachine(mader=device.mader,material=device.material, color=device.color,
                       kwar=device,functions=5, model='asd-4', broken="no")
blender = Blender(mader=device.mader,material=device.material, color=device.color,
                  functions=3, model='arc series', broken='yes')
meatgrinder = MeatGrinder(mader=device.mader,material=device.material, color=device.color,
                          functions=2, model='russain meat', broken='never broken')
print(coffem.info())
print(blender.info())
