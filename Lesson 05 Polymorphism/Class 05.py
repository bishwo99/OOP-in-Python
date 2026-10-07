class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)

p1 = Point(2,3)
p2 = Point(4,5)

p3 = p1 + p2
print(p3.x)
print(p3.y)
print("Another operator")
class point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __sub__(self, other):
        return point(self.a-other.a, self.b-other.b)

x1 = point(6,7)
x2 = point(4,2)

x3 = x1 - x2

print(x3.a)
print(x3.b)

