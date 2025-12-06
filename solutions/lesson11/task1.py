import math

class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = float(abscissa)
        self._ordinate = float(ordinate)
    
    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate
    
    def __repr__ (self) -> str:
        return "Vector2D(abscissa=" + str(self._abscissa) + "ordinate=" + str(self._ordinate) + ")"

    def __eq__ (self, other: "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa == other.abscissa) and (self.ordinate == other.ordinate)
    
    def __ne__ (self, other : "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa == other.abscissa) and (self.ordinate == other.ordinate)
    
    def __lt__ (self, other : "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa < other.abscissa) or (self.abscissa == other.abscissa and self.ordinate < other.ordinate)

    def __gt__ (self, other : "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa > other.abscissa) or (self.abscissa == other.abscissa and self.ordinate > other.ordinate)

    def __le__ (self, other : "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa <= other.abscissa) or (self.abscissa == other.abscissa and self.ordinate <= other.ordinate)
    
    def __ge__ (self, other : "Vector2D") -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return (self.abscissa >= other.abscissa) or (self.abscissa == other.abscissa and self.ordinate >= other.ordinate)

    def __abs__ (self) -> float:
        return (self.abscissa ** 2 + self.ordinate ** 2) ** 0.5

    def __bool__ (self) -> bool:
        if self.abscissa == 0 and self.ordinate == 0:
            return False
        return True

    def __mul__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * number, self.ordinate * number)
    
    def __rmul__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            raise TypeError("number должен быть числом")
        return Vector2D(self.abscissa * number, self.ordinate * number)
    
    def __truediv__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa / number, self.ordinate / number)
    
    def __rtruediv__ (self, number : int | float) -> "Vector2D":
            raise TypeError("нельзя делить вектор на число")
    
    def __add__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa + number, self.ordinate + number)
    
    def __radd__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            raise TypeError("number должен быть числом")
        return Vector2D(self.abscissa + number, self.ordinate + number)

    def __sub__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa - number, self.ordinate - number)
    
    def __rsub__ (self, number : int | float) -> "Vector2D":
        if not isinstance(number, (int, float)):
            raise TypeError("number должен быть числом")
        return Vector2D(number - self.abscissa, number - self.ordinate)

    def __neg__ (self):
        return Vector2D(-1 * self.abscissa, -1 * self.ordinate)
    
    def __complex__ (self):
        return complex(self.abscissa, self.ordinate)
    
    def __float__ (self):
        return float(abs(self))
    
    def __int__ (self):
        return int(float(self))

    def __matmul__ (self, other : "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        return self.abscissa * other.abscissa + self.ordinate * other.ordinate
    
    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("other должен быть вектором")
        if other.abscissa == 0 and other.ordinate == 0:
            raise TypeError("расчет угла между данным вектором и нулевым вектором невозможен")
        return math.acos((other @ self) / (abs(other) * abs(self)))

    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -1 * self.ordinate)