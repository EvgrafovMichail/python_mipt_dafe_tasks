import math

class Vector2D:
    def __init__(self, abscissa=0.0, ordinate=0.0):
        self._abscissa =abscissa
        self._ordinate =ordinate
    
    @property
    def abscissa(self):
        return self._abscissa
    
    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return math.isclose(self._abscissa, other._abscissa) and math.isclose(self._ordinate, other._ordinate)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector2D):
            if self.__eq__(other):
                return False
            if not math.isclose(self._abscissa, other._abscissa):
                return self._abscissa > other._abscissa
            return self._ordinate > other._ordinate
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector2D):
            if self.__eq__(other):
                return False
            if not math.isclose(self._abscissa, other._abscissa):
                return self._abscissa < other._abscissa
            return self._ordinate < other._ordinate
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Vector2D):
            return not self.__lt__(other)
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Vector2D):
            return not self.__gt__(other)
        return NotImplemented

    def __abs__(self):
        return math.sqrt(self._abscissa ** 2 + self._ordinate ** 2)

    def __bool__(self):
        return not math.isclose(abs(self), 0.0, abs_tol=1e-15)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._abscissa * other, self._ordinate * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        
        if isinstance(other, (int, float)):
            return Vector2D(self._abscissa / other, self._ordinate / other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector2D):
            new_x = self._abscissa + other._abscissa
            new_y = self._ordinate + other._ordinate
            return Vector2D(new_x, new_y)
        elif isinstance(other, (int, float)):
            new_x = self._abscissa + other
            new_y = self._ordinate + other
            return Vector2D(new_x, new_y)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            new_x = self._abscissa - other._abscissa
            new_y = self._ordinate - other._ordinate
            return Vector2D(new_x, new_y)
        elif isinstance(other, (int, float)):
            new_x = self._abscissa - other
            new_y = self._ordinate - other
            return Vector2D(new_x, new_y)
        return NotImplemented

    def __rsub__(self, other):
        raise TypeError

    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)

    def __complex__(self):
        return complex(self._abscissa, self._ordinate)

    def __float__(self):
        return float(abs(self))

    def __int__(self):
        return int(abs(self))

    def __matmul__(self, other):
        if isinstance(other, Vector2D):
            return (self._abscissa * other._abscissa + self._ordinate * other._ordinate)
        return NotImplemented

    def get_angle(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("расчет угла между данным вектором и нулевым вектором невозможен")
        
        if (math.isclose(self._abscissa, 0.0) and math.isclose(self._ordinate, 0.0)
                or math.isclose(other._abscissa, 0.0) and math.isclose(other._ordinate, 0.0)):
            raise ValueError("расчет угла между данным вектором и нулевым вектором невозможен")

        vector_product = self @ other
        cos = vector_product / (abs(self) * abs(other))

        return math.acos(cos)

    def conj(self):
        return Vector2D(self._abscissa, -self._ordinate)
    