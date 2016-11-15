class Vector:
    def __init__(self, *args):
        self.coords = [x for x in args]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name, ', '.join((str(x) for x in self.coords)))

    def __eq__(self, other):
        return self.coords == other.coords

    def __add__(self, other):
        n = max(len(self.coords), len(other.coords))
        new_coords = [self.coords[i] + other.coords[i] for i in range(n)]
        return Vector(new_coords)

    def __mul__(self, other):
        new_coords = [x * other for x in self.coords]
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)


assert(Vector(1,2,3))