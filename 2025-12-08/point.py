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
        # Need to compute the distance, but that is next time
        return 0.0


p1 = My_Point(3.5, 10.0)

print(p1)
