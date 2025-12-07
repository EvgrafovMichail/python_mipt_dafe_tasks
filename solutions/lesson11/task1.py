from math import *  # noqa: F403

EPS = 1e-9


class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            return False
        
        return (
            abs(self.abscissa - other.abscissa) < EPS and abs(self.ordinate - other.ordinate) < EPS
        )

    def __gt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        
        if not (abs(self.abscissa - other.abscissa) < EPS):
            return self.abscissa > other.abscissa
        
        if abs(self.ordinate - other.ordinate) < EPS:
            return False
        
        return self.ordinate > other.ordinate

    def __lt__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        
        return not (self >= other)

    def __ge__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        
        return self == other or self > other

    def __le__(self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError
        
        return self == other or self < other

    def __abs__(self):
        return sqrt(self.abscissa**2 + self.ordinate**2)  # noqa: F405

    def __bool__(self):
        return not (abs(self.abscissa) < EPS and abs(self.ordinate) < EPS)

    def __mul__(self, num: float):
        if not isinstance(num, (int, float)):
            raise TypeError
        
        return Vector2D(self.abscissa * num, self.ordinate * num)

    def __rmul__(self, num: float):
        if not isinstance(num, (int, float)):
            raise TypeError
        
        return Vector2D(self.abscissa * num, self.ordinate * num)

    def __truediv__(self, num: float):
        if not isinstance(num, (int, float)):
            raise TypeError
        
        if num == 0:
            raise ZeroDivisionError
        
        return Vector2D(self.abscissa * (1 / num), self.ordinate * (1 / num))

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        
        raise TypeError

    def __radd__(self, num: float):
        if not isinstance(num, (int, float)):
            raise TypeError
        
        return Vector2D(self.abscissa + num, self.ordinate + num)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa, self.ordinate - other.ordinate)
        
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
            
        raise TypeError

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __complex__(self):
        return self.abscissa + self.ordinate * 1j

    def __float__(self):
        return float(abs(self))

    def __int__(self):
        return int(abs(self))

    def __matmul__(self, other_vector: "Vector2D"):
        if not isinstance(other_vector, Vector2D):
            raise TypeError
        return self.abscissa * other_vector.abscissa + self.ordinate * other_vector.ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError
        
        if isclose(abs(self), 0.0) or isclose(abs(other), 0.0):  # noqa: F405
            raise ValueError
        
        cosinus = (self @ other) / (abs(self) * abs(other))
        return acos(cosinus)  # noqa: F405
