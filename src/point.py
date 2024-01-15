class Point(object):
    """
    Class to Represent a single point in the image.
    Contains (x, y) co-ordinates, elevation at the point (x, y) and color of the pixel.
    """

    def __init__(self, x, y, elevation, color):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.color = color

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " elevation: " + \
               str(self.elevation) + " color: " + str(self.color)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.elevation == other.elevation
