import math

class Vector2D:
    _x : float
    _y : float

    def __init__(self, abscissa=0, ordinate=0):
        self._x = float(abscissa)
        self._y = float(ordinate)

    @property
    def abscissa(self):
        return self._x

    @property
    def ordinate(self):
        return self._y

    def __repr__(self):
        return f"Vector2D(abscissa={self._x}, ordinate={self._y})"

    def conj(self):
        return Vector2D(self._x, -self._y)

    def get_angle(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError
        if not self or not other:
            raise ValueError
        dot = self @ other
        return math.acos(dot / (abs(self) * abs(other)))

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self._x, other._x) and math.isclose(self._y, other._y)

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self._x, other._x):
            if math.isclose(self._y, other._y):
                return False
            return self._y < other._y
        return self._x < other._x

    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self <= other

    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self < other
    
    def __abs__(self):
        #hypot-вычисляет евклидово расстояние в n-мерном пространстве. 
        return math.hypot(self._x, self._y)

    def __bool__(self):
        return not (math.isclose(self._x, 0.0, abs_tol=1e-12) and math.isclose(self._y, 0.0, abs_tol=1e-12))

    def __neg__(self):
        return Vector2D(-self._x, -self._y)

    def __complex__(self):
        return complex(self._x, self._y)

    def __float__(self):
        return abs(self)

    def __int__(self):
        return int(abs(self))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._x * other, self._y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._x / other, self._y / other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._x + other, self._y + other)
        if isinstance(other, Vector2D):
            return Vector2D(self._x + other._x, self._y + other._y)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self + other
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._x - other, self._y - other)
        if isinstance(other, Vector2D):
            return Vector2D(self._x - other._x, self._y - other._y)
        return NotImplemented

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._x * other._x + self._y * other._y
