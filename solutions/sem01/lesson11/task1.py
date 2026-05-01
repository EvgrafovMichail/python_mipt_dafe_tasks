import math

class Vector2D:
    

    def conj(self) -> "Vector2D":
        # ваш код
        return Vector2D(self.abscissa, (self.ordinate)*(-1))

    def get_angle(self, other: "Vector2D") -> float:
        if isinstance(other, Vector2D):
            if self == Vector2D() or other == Vector2D():
                raise ValueError
            return math.acos((self @ other)/(abs(self)*abs(other)))
        raise TypeError
    
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)
    
    @property
    def abscissa(self) -> float:
        return self._abscissa
    
    @property
    def ordinate(self) -> float:
        return self._ordinate
    
    def __repr__(self) -> str:
        x = int(self._abscissa) if self._abscissa == int(self._abscissa) else self._abscissa
        y = int(self._ordinate) if self._ordinate == int(self._ordinate) else self._ordinate
        return f"Vector2D(abscissa={x}, ordinate={y})"

    def __eq__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return False
        return (math.isclose(self.ordinate, other.ordinate) and math.isclose(self.abscissa, other.abscissa))
    
    def __ne__(self, other: 'Vector2D') -> bool:
        return not (self == other)
    
    def __lt__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa < other.abscissa
        elif not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate < other.ordinate
        return False
    
    def __le__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self < other or self == other)
    
    def __gt__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        if not math.isclose(self.abscissa, other.abscissa):
            return self.abscissa > other.abscissa
        elif not math.isclose(self.ordinate, other.ordinate):
            return self.ordinate > other.ordinate
        return False
    
    def __ge__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self > other or self == other)
        
    def __abs__(self) -> float:
        return (self.abscissa**2 + self.ordinate**2)**0.5
    
    def __bool__(self) -> bool:
        return not (math.isclose(self.abscissa, 0) and math.isclose(self.ordinate, 0))
    
    def __mul__(self, scalar: float):
        if isinstance(scalar, Vector2D):
            return NotImplemented  
        return Vector2D(self.abscissa * scalar, self.ordinate * scalar)
    
    def __rmul__(self, scalar: float):
        if isinstance(scalar, Vector2D):
            return NotImplemented  
        return Vector2D(self.abscissa * scalar, self.ordinate * scalar)
    
    def __truediv__(self, scalar: float):
        return Vector2D(self.abscissa / scalar, self.ordinate / scalar)
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(round(self.abscissa + other.abscissa, 5), round(self.ordinate + other.ordinate, 5))
        return Vector2D(round(self.abscissa + other, 5), round(self.ordinate + other, 5))
    
    def __radd__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(round(self.abscissa + other.abscissa, 5), round(self.ordinate + other.ordinate, 5))
        if isinstance(other, (int, float)):
            return Vector2D(round(self.abscissa + other, 5), round(self.ordinate + other, 5))
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(round(self.abscissa - other.abscissa, 5), round(self.ordinate - other.ordinate, 5))
        if isinstance(other, (int, float)):
            return Vector2D(round(self.abscissa - other, 5), round(self.ordinate - other, 5))
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(round(self.abscissa - other.abscissa, 5), round(self.ordinate - other.ordinate, 5))
       
        return NotImplemented
    
    def __neg__(self):
        return Vector2D(-self.abscissa, -self.ordinate)
    
    def __float__(self) -> float:
        return abs(self)
    
    def __int__(self) -> float:
        return int(abs(self))
    
    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)
    
    def __matmul__(self, other: 'Vector2D'):
        if isinstance(other, Vector2D):  
            return (self.abscissa * other.abscissa + self.ordinate * other.ordinate)
        return NotImplemented
