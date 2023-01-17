import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.ing = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza(диаметр={self.radius} из {self.ing})'

    def area(self):
        return self.circle_area(self.radius)

    @classmethod
    def margherita(cls):
        return cls(30, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(40, ['mozarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


print(Pizza.margherita())
print(Pizza.prosciutto())
p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
