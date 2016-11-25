class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        a = self.x == other.x, self.y == other.y, self.z == other.z
        return all(a)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

v1 = Vector(3, 4, 5)
print(v1)
print(id(v1))

v2 = Vector(3, 4, 5)
print(v2)
print(id(v2))

v3 = Vector(6, 7, 8)

print(v1 == v2)
print(v2 == v3)
print(v1 is v2)
print(v1 + v2)
print(v1 * 6)
print(6 * v1)
