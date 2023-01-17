import math


class Point:
    MAX_SIZE = 10

    @staticmethod
    def get_distance(x, y):
        return math.sqrt(x**2 + y**2)


class Cat:
    tail = 20
    claws = 1
    weight = 15
    MAX_WEIGHT = 25


    def sleep(self):
        print(self.name)
        print('Котик поспал')

    def set_cat(self, tail, claws):
        self.tail = tail
        self.claws = claws

    @classmethod
    def validate_weight(cls, weight):
        return weight <= cls.MAX_WEIGHT

    def set_weight(self, weight):
        if self.validate_weight(weight):
            self.name = 'Милаш'
        else:
            self.name = 'Пухляш'

    @staticmethod
    def eat(food):
        print(f'Вес котика увеличился на {food} грамм')


print(Point.get_distance(-2, -2))
my_point = Point()
print(my_point.get_distance(-2, -2))

cat = Cat()
cat.set_cat(24, 3)
cat.set_weight(10)
print(cat.__dict__)
cat.eat(100)