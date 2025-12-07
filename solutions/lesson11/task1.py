import math
class Vector2D:
    __abcissa: float
    __ordinata: float
    
    def __init__(self, abcissa: float = 0, ordinata: float = 0):
        self.__abcissa = abcissa
        self.__ordinata = ordinata
    @property   
    def abcissa(self):
        return self.__abcissa
    @property
    def ordinata(self):
        return self.__ordinata
        
    def __repr__(self):
        return f'Vector2D(abcissa={self.abcissa}, ordinata={self.ordinata})'
    
    def __eq__(self, other):
        return math.isclose(self.__abcissa, other.__abcissa) and math.isclose(self.__ordinata, other.__ordinata)    
    def __gt__(self, other):
        return (self != other and 
               (self.abcissa > other.abcissa or self.abcissa == other.abcissa and self.ordinata > other.ordinata))    
    def __lt__(self, other):
        return (self != other and 
                (self.abcissa < other.abcissa or self.abcissa == other.abcissa and self.ordinata < other.ordinata))       
    def __ge__(self, other):
        return (self == other or 
                (self.abcissa > other.abcissa or self.abcissa == other.abcissa and self.ordinata > other.ordinata))      
    def __le__(self, other):
        return (self == other or
                (self.abcissa < other.abcissa or self.abcissa == other.abcissa and self.ordinata < other.ordinata))
        
    def __add__(self, other):
        if not isinstance(other, Vector2D | float | int):
            return NotImplemented
      
        if isinstance(other, float | int):
            return Vector2D(self.abcissa + other, self.ordinata + other)
        return Vector2D(self.abcissa + other.abcissa, self.abcissa + other.ordinata)
    def __sub__(self, other):
        if not isinstance(other, Vector2D | float | int):
            return NotImplemented
       
        if isinstance(other, float | int):
            return Vector2D(self.abcissa - other, self.ordinata - other)
        return Vector2D(self.abcissa - other.abcissa, self.abcissa - other.ordinata)
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        return Vector2D(self.abcissa * other, self.ordinata * other)
    def __rmul__(self, other):
        return self * other
    def __truediv__(self, other):
        return Vector2D(self.abcissa / other, self.ordinata / other)
    def __neg__(self):
        return Vector2D(-self.abcissa, -self.ordinata)
    
    def __float__(self):
        return abs(self)
    def __int__(self):
        return int(abs(self))
    def __complex__(self):
        return complex(self.abcissa, self.ordinata)
    def __bool__(self):
        return bool(abs(self))
    
    def __matmul__(self, other: "Vector2D"):
        return self.abcissa*other.abcissa + self.ordinata*other.ordinata
    
    def __abs__(self):
        return math.sqrt(self.abcissa ** 2 + self.ordinata ** 2)
    
    def conj(self) -> "Vector2D":
        return Vector2D(self.abcissa, -self.ordinata)
    
    def get_angle(self, other: "Vector2D") -> float:
        if abs(other) == 0:
            raise ValueError(f"расчет угла между вектором {self} и нулевым вектором невозможен")
        if abs(self) == 0:
            raise ValueError(f"расчет угла между вектором {other} и нулевым вектором невозможен")
        return math.acos((self @ other) / (abs(self) * abs(other)))
    
