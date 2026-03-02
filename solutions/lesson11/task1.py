import math


class Vector2D:
    __abscissa: float
    __ordinate: float

    def __init__(self, abscissa: float = 0, ordinate: float = 0):
        self.__abscissa = abscissa
        self.__ordinate = ordinate

    @property
    def abscissa(self):
        return self.__abscissa

    @property
    def ordinate(self):
        return self.__ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.__abscissa, other.__abscissa) and math.isclose(
            self.__ordinate, other.__ordinate
        )

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self != other and (
            self.abscissa > other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate > other.ordinate
        )

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self != other and (
            self.abscissa < other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate < other.ordinate
        )

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self == other or (
            self.abscissa > other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate > other.ordinate
        )

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self == other or (
            self.abscissa < other.abscissa
            or self.abscissa == other.abscissa
            and self.ordinate < other.ordinate
        )

    def __add__(self, other):
        if not isinstance(other, Vector2D | float | int):
            return NotImplemented

        if isinstance(other, float | int):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return Vector2D(self.abscissa + other.abscissa, self.abscissa + other.ordinate)

    def __sub__(self, other):
        if not isinstance(other, Vector2D | float | int):
            return NotImplemented

        if isinstance(other, float | int):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        return Vector2D(self.abscissa - other.abscissa, self.abscissa - other.ordinate)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        return Vector2D(self.abscissa * other, self.ordinate * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Vector2D(self.abscissa / other, self.ordinate / other)

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __complex__(self):
        return complex(self.abscissa, self.ordinate)

    def __bool__(self):
        return bool(abs(self))

    def __matmul__(self, other: "Vector2D"):
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate

    def __abs__(self):
        return math.sqrt(self.abscissa**2 + self.ordinate**2)

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if abs(other) == 0:
            raise ValueError(f"расчет угла между вектором {self} и нулевым вектором невозможен")
        if abs(self) == 0:
            raise ValueError(f"расчет угла между вектором {other} и нулевым вектором невозможен")
        return math.acos((self @ other) / (abs(self) * abs(other)))

vec = Vector2D(1, 1)
vec1 = Vector2D(2, 2)
print(vec1 > vec)