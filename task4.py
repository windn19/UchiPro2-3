class Polygon:
   def set_vertices_count(self, count):
       self.count = count

   def set_coordinates(self, coords):
       self.coords = coords

   def get_side_length(self, num):
       if num == self.count:
           length = ((self.coords[0][0] - self.coords[num - 1][0]) ** 2 +
                     (self.coords[0][1] - self.coords[num - 1][1]) ** 2) ** 0.5
       else:
           length = ((self.coords[num][0] - self.coords[num - 1][0]) ** 2 +
                     (self.coords[num][1] - self.coords[num - 1][1]) ** 2) ** 0.5
       return round(length, 2)


n = int(input())
coords = []
for i in range(n):
   x, y = map(int, input().split())
   coords.append((x, y))

polygon = Polygon()
polygon.set_vertices_count(n)
polygon.set_coordinates(coords)
print(polygon.get_side_length(1))
print(polygon.get_side_length(2))