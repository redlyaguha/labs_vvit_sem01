class Circle:
    def __init__(self,radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

Circle = Circle(5)
Circle.set_radius(10)
print(Circle.get_radius())