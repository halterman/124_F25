class My_Point:
    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a new point object.
        
        :param self: The object being initialized
        :param x: the x coordinate of the new point
        :type x: float
        :param y: the y coordinate of the new point
        :type y: float
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Produces a human-readable representation of the point object
        
        :param self: The object being initialized
        :return: A human-readable string for the object
        :rtype: str
        """
        return f'({self.x}, {self.y})'
    
    def distance(self, p: My_Point) -> float:
        import math
        x1 = self.x
        y1 = self.y
        x2 = p.x
        y2 = p.y
        dist = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
        return dist


p1 = My_Point(0.0, 0.0)
p2 = My_Point(1.0, 1.0)

print(p1)
print(p2)
print(p1.distance(p2))
