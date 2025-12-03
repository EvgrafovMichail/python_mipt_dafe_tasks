import math


class Vector2D:
    def __init__(self, abscissa: float = 0, ordinate: float = 0) -> None:
        self._abscissa = abscissa
        self._ordinate = ordinate

    def conj(self) -> "Vector2D":
        return Vector2D(self._abscissa, -self._ordinate)

    def get_angle(self, other: "Vector2D") -> float:
        Vector2D._validate_vec(other)
        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("Cannot get angle with zero vector")
        return math.acos((self @ other) / (abs(self) * abs(other)))

    def get_abscissa(self) -> float:
        return self._abscissa

    def get_ordinate(self) -> float:
        return self._ordinate

    abscissa = property(get_abscissa)
    ordinate = property(get_ordinate)

    def __str__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        if isinstance(other, Vector2D):
            return Vector2D._is_close(self._abscissa, other._abscissa) and Vector2D._is_close(
                self._ordinate, other._ordinate
            )
        return bool(self) == other

    def __ne__(self, other: "Vector2D") -> bool:
        return not (self == other)

    def __lt__(self, other: "Vector2D") -> bool:
        Vector2D._validate_vec(other)
        if not Vector2D._is_close(self._abscissa, other._abscissa):
            return self._abscissa < other._abscissa
        if not Vector2D._is_close(self._ordinate, other._abscissa):
            return self._ordinate < other._ordinate
        return False

    def __le__(self, other: "Vector2D") -> bool:
        Vector2D._validate_vec(other)
        if not Vector2D._is_close(self._abscissa, other._abscissa):
            return self._abscissa <= other._abscissa
        if not Vector2D._is_close(self._ordinate, other._ordinate):
            return self._ordinate <= other._ordinate
        return True

    def __gt__(self, other: "Vector2D") -> bool:
        Vector2D._validate_vec(other)
        return not (self <= other)

    def __ge__(self, other: "Vector2D") -> bool:
        Vector2D._validate_vec(other)
        return not (self < other)

    def __abs__(self) -> float:
        return (self._abscissa**2 + self._ordinate**2) ** (1 / 2)

    def __bool__(self) -> bool:
        return not Vector2D._is_close(abs(self), 0)

    def __mul__(self, val: float) -> "Vector2D":
        Vector2D._validate_val(val)
        return Vector2D(self._abscissa * val, self._ordinate * val)

    def __rmul__(self, val: float) -> "Vector2D":
        Vector2D._validate_val(val)
        return self * val

    def __truediv__(self, val: float) -> "Vector2D":
        Vector2D._validate_val(val)
        return self * (1 / val)

    def __add__(self, other: "Vector2D" | float) -> "Vector2D":
        Vector2D._validate_scal(other)
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa + other._abscissa, self._ordinate + other._ordinate)
        return Vector2D(self._abscissa + other, self._ordinate + other)

    def __radd__(self, other: "Vector2D" | float) -> "Vector2D":
        Vector2D._validate_scal(other)
        return self + other

    def __sub__(self, other: "Vector2D" | float) -> "Vector2D":
        Vector2D._validate_scal(other)
        if isinstance(other, Vector2D):
            return Vector2D(self._abscissa - other._abscissa, self._ordinate - other._ordinate)
        return Vector2D(self._abscissa - other, self._ordinate - other)

    def __neg__(self) -> "Vector2D":
        return self * (-1)

    def __float__(self) -> float:
        return abs(self)

    def __int__(self) -> int:
        return round(abs(self) // 1)

    def __complex__(self) -> complex:
        return complex(self._abscissa, self._ordinate)

    def __matmul__(self, other: "Vector2D") -> float:
        Vector2D._validate_vec(other)
        return self._abscissa * other._abscissa + self._ordinate * other._ordinate

    @staticmethod
    def _validate_vec(other) -> None:
        if not isinstance(other, Vector2D):
            raise TypeError

    @staticmethod
    def _validate_scal(other) -> None:
        if not (isinstance(other, Vector2D) or isinstance(other, float) or isinstance(other, int)):
            raise TypeError

    @staticmethod
    def _validate_val(val) -> None:
        if not (isinstance(val, float) or isinstance(val, int)):
            raise TypeError

    @staticmethod
    def _is_close(lval, rval, eps=10 ** (-5)) -> bool:
        return abs(lval - rval) < eps
