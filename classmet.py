class Point:
    MAX_SIZE = 10

    @classmethod
    def validate_size(cls, size):
        return size <= cls.MAX_SIZE

    def set_size(self, size):
        if self.validate_size(size):
            self.size = size
        else:
            self.size = self.MAX_SIZE


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


print(Point.validate_size(15))
my_point = Point()
my_point.set_size(15)
print(my_point.size)

cat = Cat()
cat.set_cat(24, 3)
cat.set_weight(10)
print(cat.__dict__)
cat.set_weight(30)
print(cat.__dict__)
