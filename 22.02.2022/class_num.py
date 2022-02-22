class Num:
    def __init__(self, numb):
        self.num = numb

    def input_value(self, value):
        self.num = value
        return True

    def print_value(self):
        print(self.num)
        return True

    def from_one_value_to_eight(self):
        return oct(self.num)

    def from_one_value_to_sixteen(self):
        return hex(self.num)

    def from_one_value_to_two(self):
        return bin(self.num)


num = Num(78)
print(num.from_one_value_to_two())
