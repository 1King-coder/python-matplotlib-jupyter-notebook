from math import tan, radians


class Point:
    """
    Class to help the use of points.
    """

    def __init__(self, coordenates: tuple) -> None:
        self.x = coordenates[0]
        self.y = coordenates[1]


class Straight:
    """
    Class for Straight theorems
    """

    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.p1x, self.p1y = point_1.x, point_1.y
        self.p2x, self.p2y = point_2.x, point_2.y

    @property
    def point_to_point_distance(self) -> float:
        """
        The distance between 2 points.

        d(OB) = sqrt((X - Xo)^2 + (Y - Yo)^2)
        """

        return ((self.p1x - self.p2x)**2 + (self.p1y - self.p2y)**2)**0.5

    @property
    def equation(self) -> dict:
        """
        Equation -> (A)x + (B)y + (C) = 0
        """

        eq = {
            "A": self.p1x - self.p2x,
            "B": self.p2y - self.p1y,
            "C": self.p1x*self.p2y - self.p2x*self.p1y
        }

        eq["eq"] = f"{eq['A']}x + ({eq['B']}y) + ({eq['C']})"

        return eq

    @staticmethod
    def angular_coefficient(angle: float) -> float:
        """
        angular coeficient : M
        y
        |    /
        |   /
        |  /
        | / angle @° 
        |/)___________
                      x

        M = Tan(@°)
        or
        (x - xº)M = (y - yº)
        """

        return tan(radians(angle))

    @staticmethod
    def rel_points(ref_point: Point, distance: float, angle: float = False,
                   angular_coef: float = False) -> list:
        """
        Use of my theorem to get the points.

        Return a Array with the relative
        points as Point objects.
        """
        p1x_coordenate = ref_point.x + \
            ((distance**2)/((Straight.angular_coefficient(angle)**2)+1))**0.5
        p2x_coordenate = ref_point.x - \
            ((distance**2)/((Straight.angular_coefficient(angle)**2)+1))**0.5

        if angular_coef:
            p1x_coordenate = ref_point.x + \
                ((distance**2)/((angular_coef**2)+1))**0.5
            p2x_coordenate = ref_point.x - \
                ((distance**2)/((angular_coef**2)+1))**0.5

        p1y_coordenate = ref_point.y - \
            Straight.angular_coefficient(angle)*(ref_point.x - p1x_coordenate)
        p2y_coordenate = ref_point.y - \
            Straight.angular_coefficient(angle)*(ref_point.x - p2x_coordenate)

        return [
            Point((p1x_coordenate, p1y_coordenate)),
            Point((p2x_coordenate, p2y_coordenate))
        ]
