class Point:
    size = 1
    color = 'black'

    def set_coordinates(self):
        print(id(self))


class Cat:
    tail = 20
    claws = 1

    def sleep(self):
        print('Котик поспал')
        print(id(self))


my_point = Point()
print(id(my_point))
my_point.set_coordinates()

cat = Cat()
print(id(cat))
cat.sleep()
