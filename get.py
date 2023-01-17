class Point:
    size = 1
    color = 'black'

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def sum_coor(self):
        return self.x + self.y

class Cat:
    tail = 20
    claws = 1

    def sleep(self):
        print(self.name)
        print('Котик поспал')

    def set_cat(self, tail, claws, name):
        self.tail = tail
        self.claws = claws
        self.name = name

    def get_cat(self):
        return self.name, self.tail, self.claws


my_point = Point()
my_point.set_coordinates(3, 5)
my_point1 = Point()
my_point1.set_coordinates(5, 4)
print(my_point)
print(my_point.get_coordinates())
print(my_point.sum_coor())
print(my_point1.sum_coor())

cat = Cat()
cat.set_cat(24, 3, 'Васька')
print(cat.get_cat())
cat.sleep()