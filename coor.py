class Point:
    size = 1
    color = 'black'

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

class Cat:
    tail = 20
    claws = 1

    def sleep(self):
        print('Котик поспал')

    def set_cat(self, tail, claws):
        self.tail = tail
        self.claws = claws


my_point = Point()
my_point.set_coordinates(3, 5)
print(my_point.__dict__)
my_point1 = Point()
my_point1.set_coordinates(5, 3)
print(my_point1.__dict__)

cat = Cat()
cat.set_cat(15, 2)
print(cat.__dict__)
cat1  = Cat()
cat1.set_cat(17, 3)
print(cat1.__dict__)
