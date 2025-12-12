import math


class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self.__abscissa = float(abscissa)
        self.__ordinate = float(ordinate)
    
    @property
    def abscissa(self):
        return self.__abscissa
    @property
    def ordinate(self):
        return self.__ordinate
    
    def __repr__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"
    
    def __eq__(self, other: object):
        if not isinstance(other, Vector2D):
            return False
        return (math.isclose(self.abscissa, other.abscissa) and 
                math.isclose(self.ordinate, other.ordinate))
    
    def __ne__(self, other: object):
        return not self.__eq__(other)
    
    def __lt__(self, other: object):
        if not isinstance(other, Vector2D):
            return NotImplemented
        
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate < other.ordinate
        return self.abscissa < other.abscissa
    
    def __le__(self, other: object):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other
    
    def __gt__(self, other: object):
        if not isinstance(other, Vector2D):
            return NotImplemented
        
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate > other.ordinate
        return self.abscissa > other.abscissa
    
    def __ge__(self, other: object):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self > other or self == other
    
    def __abs__(self):
        return math.sqrt(self.abscissa**2 + self.ordinate**2)
    
    def __bool__(self):
        return not math.isclose(abs(self), 0.0, abs_tol=1e-15)
    
    def __mul__(self, other: object):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * other, self.ordinate * other)
    
    def __rmul__(self, other: object):
        return self.__mul__(other)
    
    def __truediv__(self, other: object):
        if not isinstance(other, (int, float)):
            return NotImplemented
        if math.isclose(other, 0.0):
            raise ZeroDivisionError("Делить на ноль нельзя")
        return Vector2D(self.abscissa / other, self.ordinate / other)
    
    def __add__(self, other: object):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        elif isinstance(other, Vector2D):
            return Vector2D(
                self.abscissa + other.abscissa,
                self.ordinate + other.ordinate
            )
        else:
            return NotImplemented
    
    def __radd__(self, other: object):
        return self.__add__(other)
    
    def __sub__(self, other: object):
        if isinstance(other, (int, float)):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        elif isinstance(other, Vector2D):
            return Vector2D(
                self.abscissa - other.abscissa,
                self.ordinate - other.ordinate
            )
        else:
            return NotImplemented
    
    def __rsub__(self, other: object):
        return NotImplemented
    
    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)
    
    def __complex__(self):
        return complex(self.abscissa, self.ordinate)
    
    def __float__(self):
        return float(abs(self))
    
    def __int__(self):
        return int(abs(self))
    
    def __matmul__(self, other: object):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate
    
    def conj(self):
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: object):
        if not isinstance(other, Vector2D):
            raise TypeError("Объект Vector2D требуется")
        if not bool(self) or not bool(other):
            raise ValueError(
                "Нельзя найти угол между данным и нулевым векторами"
            )
        dot_product = self @ other
        magnitude_self = abs(self)
        magnitude_other = abs(other)
        cos_theta = dot_product / (magnitude_self * magnitude_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return math.acos(cos_theta)