import math

class Vector2D:
    def __init__(self, abscissa=0.0, ordinate=0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)
    
    @property
    def abscissa(self):
        return self._abscissa
    
    @property
    def ordinate(self):
        return self._ordinate
    
    def __repr__(self):
        abscissa_str = str(int(self._abscissa)) if self._abscissa.is_integer() else str(self._abscissa)
        ordinate_str = str(int(self._ordinate)) if self._ordinate.is_integer() else str(self._ordinate)
        return f"Vector2D(abscissa={abscissa_str}, ordinate={ordinate_str})"
    
    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._abscissa, other._abscissa) and math.isclose(self._ordinate, other._ordinate)
    
    def __ne__(self, other):
        eq_result = self.__eq__(other)
        return not eq_result if eq_result is not NotImplemented else NotImplemented
    
    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self._abscissa, other._abscissa):
            return False if math.isclose(self._ordinate, other._ordinate) else self._ordinate < other._ordinate
        return self._abscissa < other._abscissa
    
    def __le__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self.__le__(other)
    
    def __ge__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not self.__lt__(other)
    
    def __abs__(self):
        return math.hypot(self._abscissa, self._ordinate)
    
    def __bool__(self):
        return not (math.isclose(self._abscissa, 0.0, abs_tol=1e-15) and 
                   math.isclose(self._ordinate, 0.0, abs_tol=1e-15))
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._abscissa * scalar, self._ordinate * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if math.isclose(scalar, 0.0):
            raise ZeroDivisionError("Деление на ноль")
        return Vector2D(self._abscissa / scalar, self._ordinate / scalar)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._abscissa + other, self._ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self._abscissa - other, self._ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        return NotImplemented
    
    def __rsub__(self, other):
        return NotImplemented
    
    def __neg__(self):
        return Vector2D(-self._abscissa, -self._ordinate)
    
    def __complex__(self):
        return complex(self._abscissa, self._ordinate)
    
    def __float__(self):
        return float(abs(self))
    
    def __int__(self):
        return int(float(self))
    
    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate
    
    def get_angle(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Должен быть Vector2D")
        
        if not bool(self) or not bool(other):
            raise ValueError("Угол не определен")
        
        dot_product = self @ other
        norms_product = abs(self) * abs(other)
        cos_angle = dot_product / norms_product
        cos_angle = max(-1.0, min(1.0, cos_angle))
        
        return math.acos(cos_angle)
    
    def conj(self):
        return Vector2D(self._abscissa, -self._ordinate)