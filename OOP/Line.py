# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        '''
        Could have used tuple unpacking:

            x1,y1 = self.coor1
            x2,y2 = self.coor2

        '''

        distance =  ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2) ** 0.5
        return distance

    def slope(self):
        m = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return m


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


li.distance()  # Expected output = 9.433981132056603

li.slope() # Expected output = 1.6
