class Set:
    def __init__(self, *args):
        self.args = args

    def sum_el(self):
        return sum([x for x in self.args])

    def average(self):
        return sum([x for x in self.args]) // len([x for x in self.args])

    def maximum(self):
        maxi = self.args[0]
        for i in self.args:
            if i > maxi:
                maxi = i

        return maxi

    def minimum(self):
        mini = self.args[0]
        for i in self.args:
            if i < mini:
                mini = i
        return mini

test_obj_1 = Set(['2,6,4,3,2'])
print(test_obj_1.maximum())

