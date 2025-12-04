import math
from numbers import Real

class Vector2D:
    def __init__(self, abscissa:float = 0.0, ordinate: float = 0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)

    @property
    def abscissa(self):
        return self._abscissa
    
    @property
    def ordinate(self):
        return self._ordinate

    def __repr__(self):
        def format_val(val):
            if val == int(val):
                return str(int(val))
            return str(val)
        return f"Vector2D(abscissa={format_val(self.abscissa)}, ordinate={format_val(self.ordinate)})"
    
    def __bool__(self):
        return not math.isclose(abs(self), 0.0,  abs_tol=1e-15)
    
    def __abs__(self):
        return math.hypot(self.abscissa, self.ordinate)
    
    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (math.isclose(self.abscissa, other.abscissa) and
                math.isclose(self.ordinate, other.ordinate))
    

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return True  
        return not self == other

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False  
            return self.ordinate < other.ordinate
        return self.abscissa < other.abscissa

    def __le__(self, other) -> bool: #<=
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self < other) or (self == other)

    def __gt__(self, other) -> bool: #>
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not (self <= other)

    def __ge__(self, other) -> bool:#>=
        if not isinstance(other, Vector2D):
            return NotImplemented
        return not (self < other)
    

    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)
    
    def __float__(self) -> float:
        return float(abs(self))
    
    def __int__(self) ->int:
        return int(abs(self))
    


    def __add__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa, self.ordinate + other.ordinate)
        return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, Real):
            return self + other  
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa,
                          self.ordinate - other.ordinate)
        return NotImplemented
    
    def __rsub__(self, other) :
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Real):
            return Vector2D(self.abscissa * other, self.ordinate*other)
        return NotImplemented
    
    def __rmul__(self, other):
        if isinstance(other, Real):
            return self * other
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, Real):
            if math.isclose(other, 0.0):
                raise ZeroDivisionError("Division by zero")
            return Vector2D(self.abscissa/other, self.ordinate/other)
        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)

    def __matmul__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.abscissa*other.abscissa + self.ordinate*other.ordinate
    
    def __rmatmul__(self, other):
        if isinstance(other, Vector2D):
            return other @ self  
        return NotImplemented
    
    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Only Vector2D")
        
        if not bool(self) or not bool(other):
           raise ValueError("Zero Vecro2D =(")
        
        cos_angel = max(-1.0, min(1.0, (self @ other)/ (abs(self) * abs(other))))
        return math.acos(cos_angel)
        

