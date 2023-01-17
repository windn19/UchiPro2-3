class Point:
    size = 1
    color = 'black'

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


my_point = Point()
my_point.set_coordinates(3, 5)
print(getattr(my_point, 'get_coordinates')())
print(hasattr(my_point, 'set_coordinate'))
