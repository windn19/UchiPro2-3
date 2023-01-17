import math


class Circle:
   def set_center(self, x, y):
       self.x = x
       self.y = y

   def set_radius(self, R):
       self.R = R

   def get_distance(self):
       return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

   def get_area(self):
       return round(3.14 * self.R ** 2, 2)


x = int(input())
y = int(input())
R = int(input())

c = Circle()
c.set_center(x, y)
c.set_radius(R)
print(c.get_area())
print(c.get_distance())
