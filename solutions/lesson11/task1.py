class Vector2D:
    _abscissa: float
    _ordinate: float

    def __init__(self, abscissa: float = 0.0, ordinate: float = 0.0):
        self._abscissa = abscissa
        self._ordinate = ordinate

    @property
    def abscissa(self) -> float:
        return self._abscissa

    @property
    def ordinate(self) -> float:
        return self._ordinate

    # ИСПРАВИТЬ!!!
    def print(self):
        print(f"Vector2D(abscissa={self._abscissa}, ordinate={self._abscissa})")

    def conj(self) -> "Vector2D":
        # ваш код
        return Vector2D()

    def get_angle(self, other: "Vector2D") -> float:
        # ваш код
        return 0

    # ваш код


v = Vector2D(5, 7)
print(v)
