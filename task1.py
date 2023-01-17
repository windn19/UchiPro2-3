class Point:
    def set_coordinates(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return self.x, self.y, self.z


x = int(input())
y = int(input())
z = int(input())
pt = Point()
pt.set_coordinates(x, y, z)
print(pt.get_coordinates())
print(pt.__dict__)
