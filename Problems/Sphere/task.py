class Sphere:
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 * self.PI * (self.radius*self.radius*self.radius))/3
