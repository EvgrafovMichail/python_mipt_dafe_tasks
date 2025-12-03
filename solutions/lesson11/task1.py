import math


class Vector2D:
    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate
    
    @property
    def abscissa(self):
        return self._abscissa
    
    @property
    def ordinate(self):
        return self._ordinate
    
    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"

    def __eq__(self, other: object) -> bool: # ==
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.abscissa, other.abscissa) \
        and math.isclose(self.ordinate, other.ordinate)
    
    def __gt__(self, other: object) -> bool: # >
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate > other.ordinate
        return self.abscissa > other.abscissa
    
    def __lt__(self, other: object) -> bool: # <
        if not isinstance(other, Vector2D):
            return NotImplemented
        if math.isclose(self.abscissa, other.abscissa):
            if math.isclose(self.ordinate, other.ordinate):
                return False
            return self.ordinate < other.ordinate
        return self.abscissa < other.abscissa
    
    def __ge__(self, other: object) -> bool: # >=
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self > other or self == other
    
    def __le__(self, other: object) -> bool: # <=
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self < other or self == other
    
    def __abs__(self) -> float:
        return (self.abscissa ** 2 + self.ordinate ** 2) ** 0.5
    
    def __bool__(self) -> bool:
        return not (math.isclose(self.abscissa, 0.0, abs_tol=1e-10) 
                    and math.isclose(self.ordinate, 0.0, abs_tol=1e-10))
    
    def __mul__(self, num: float) -> object: # *
        if not isinstance(num, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * num, self.ordinate * num)
    
    def __rmul__(self, num: float) -> object: # *
        if not isinstance(num, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa * num, self.ordinate * num)
    
    def __truediv__(self, num: float) -> object: # /
        if not isinstance(num, (int, float)):
            return NotImplemented
        return Vector2D(self.abscissa / num, self.ordinate / num)
    
    def __add__(self, other: object | int | float) -> object: # +
        if isinstance(other, int | float):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa + other.abscissa,
                            self.ordinate + other.ordinate)
        return NotImplemented
    
    def __radd__(self, other: int | float) -> object: # +
        if isinstance(other, int | float):
            return Vector2D(self.abscissa + other, self.ordinate + other)
        return NotImplemented
    
    def __sub__(self, other: object | int | float) -> object: # -
        if isinstance(other, int | float):
            return Vector2D(self.abscissa - other, self.ordinate - other)
        if isinstance(other, Vector2D):
            return Vector2D(self.abscissa - other.abscissa,
                            self.ordinate - other.ordinate)
        return NotImplemented
    
    # def __rsub__(self, other: int | float) -> object: # -
    #     if isinstance(other, (int, float)):
    #         return Vector2D(other - self.abscissa, other - self.ordinate)
    #     return NotImplemented
    
    def __neg__(self) -> object: # - (унарный)
        return Vector2D(-self.abscissa, -self.ordinate)
    
    def __int__(self) -> int:
        return int((self.abscissa ** 2 + self.ordinate ** 2) ** 0.5)
    
    def __float__(self) -> float:
        return (self.abscissa ** 2 + self.ordinate ** 2) ** 0.5
    
    def __complex__(self) -> complex:
        return complex(self.abscissa, self.ordinate)
    
    def __matmul__(self, other: object) -> float: # @
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self.abscissa * other.abscissa 
                + self.ordinate * other.ordinate)
    
    def conj(self) -> "Vector2D":
        return Vector2D(self.abscissa, -self.ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Аргумент должен быть типа Vector2D")
        if not math.isclose(abs(self), 0) and not math.isclose(abs(other), 0):
            cos_angle = (self @ other) / (abs(self) * abs(other))
            cos_angle = max(-1.0, min(1.0, cos_angle))
            return math.acos(cos_angle)
        else:
            raise ValueError("Расчет угла между данным вектором и нулевым вектором невозможен.")