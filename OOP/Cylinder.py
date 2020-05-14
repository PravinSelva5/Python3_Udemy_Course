class Cylinder:
    pi = 3.14

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        return (self.pi) * (self.radius**2) * (self.height)

    def surface_area(self):
        return (2 * self.pi * (self.radius**2)) + (2 * self.pi * self.radius * self.height)

# EXAMPLE OUTPUT
c = Cylinder(2,3)

# Output should be 56.52
c.volume()

# Output should be 94.2
c.surface_area()
