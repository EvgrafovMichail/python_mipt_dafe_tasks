from math import sqrt
from math import acos
from math import isclose
class Vector2D:
    def __init__(self,abscissa=0.0,ordinate=0.0):
        if not isinstance(abscissa,(int,float)):
            raise TypeError(f"abscissa must be int or float, not {type(abscissa).__name__}")
        if not isinstance(ordinate,(int,float)):
            raise TypeError(f"ordinate must be int or float, not {type(ordinate).__name__}")
        self._abscissa=abscissa 
        self._ordinate=ordinate

    def get_abscissa(self):
        return self._abscissa
    def get_ordinate(self):
        return(self._ordinate)
    abscissa=property(get_abscissa)
    ordinate=property(get_ordinate)
    def __str__(self):
        return f"Vector2D(abscissa={self.abscissa}, ordinate={self.ordinate})"
    def __eq__(v1,v2):
        if isinstance(v2,Vector2D):
            return isclose(v1.abscissa,v2.abscissa,abs_tol=1e-12) and isclose(v1.ordinate,v2.ordinate,abs_tol=1e-12)
        return False
    def __ne__(v1,v2):
        return not v1==v2
    def __lt__(v1,v2):
        if not isinstance(v2,Vector2D):
            raise TypeError(f"cannot compare Vector2D and {type(v2).__name__}")
        if not isclose(v1.abscissa,v2.abscissa,abs_tol=1e-12):
            return v1.abscissa<v2.abscissa
        else:
            if isclose(v1.ordinate,v2.ordinate,abs_tol=1e-12):
                return False
            return v1.ordinate<v2.ordinate
                 
    def __le__(v1,v2):
        return v1<v2 or v1==v2
    def __gt__(v1,v2):
        return not v1<v2 and v1!=v2
    def __ge__(v1,v2):
        return v1>v2 or v1==v2
    def __abs__(self):
        return sqrt(self.abscissa**2+self.ordinate**2)
    def __bool__(self):
        return not isclose(abs(self),0,abs_tol=1e-12)
    def __mul__(vector,num):
        if isinstance(num,(int,float)):
            return Vector2D(num*vector.abscissa,num*vector.ordinate)
        return NotImplemented
    def __rmul__(vector,num):
        return(vector*num)
    def __neg__(vector):
        return vector*(-1)
    def __truediv__(vector,num):
        if isinstance(num,(float,int)):
            return Vector2D(abscissa=vector.abscissa/num,ordinate=vector.ordinate/num)
        return NotImplemented
    def __rtruediv__(vector,num):
        return NotImplemented
    def __add__(vector,num_or_vec):
        if isinstance(num_or_vec,Vector2D):
            return(Vector2D(abscissa=vector.abscissa+num_or_vec.abscissa,ordinate=vector.ordinate+num_or_vec.ordinate))
        if isinstance(num_or_vec,(int,float)):
            return(Vector2D(abscissa=vector.abscissa+num_or_vec,ordinate=vector.ordinate+num_or_vec))
        else:
            return NotImplemented
    def __radd__(vector,num_or_vec):
        return vector+num_or_vec
    def __sub__(vector,num_or_vec):
        if not isinstance(num_or_vec,(int,float,Vector2D)):
            return NotImplemented
        return vector+(-num_or_vec)
    def __rsub__(vector,num_or_vec):
        return NotImplemented
    
    def __int__(vector):
        return int(abs(vector))
    def __float__(vector):
        return float(abs(vector))
    def __complex__(vector):
        return complex(vector.abscissa,vector.ordinate)
    def __matmul__(v1,v2):
        if isinstance(v2,Vector2D):
            return v1.abscissa*v2.abscissa+v1.ordinate*v2.ordinate
        return NotImplemented
    def __rmatmul__(v1,v2):
        return v1@v2

    def conj(self) -> "Vector2D":
        return Vector2D(abscissa=self.abscissa,ordinate=-(self.ordinate))

    def get_angle(self, other: "Vector2D") -> float:
        if isinstance(other,Vector2D):
            if other and self:
                return acos((self@other)/(abs(self)*abs(other)))
            raise ValueError("cannot calculate angle when one vector is zero")
        raise TypeError(f"unsupported operation between Vector2D and {type(other).__name__}")