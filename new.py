class Point:
    size = 1
    color = 'black'

    def set_coordinates(self):
        print(self.size)
        print("Вызов метода set_coordinates")

class Cat:
    tail = 20
    claws = 1

    def sleep(self):
        print(self.name)
        print('Котик поспал')


my_point = Point()
my_point.size = 5
my_point.set_coordinates()

cat = Cat()
cat.name = 'Васька'
cat.sleep()
