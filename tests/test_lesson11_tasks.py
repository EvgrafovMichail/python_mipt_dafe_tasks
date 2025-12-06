import pytest

import math
import sys
from io import StringIO


from solutions.lesson11.task1 import Vector2D


def test_read_attributes():
    vector = Vector2D(12, -13)

    assert vector.abscissa == 12
    assert vector.ordinate == -13


def test_read_attributes2():
    vector = Vector2D(abscissa=12, ordinate=-13)

    assert vector.abscissa == 12
    assert vector.ordinate == -13


def test_read_attributes3():
    vector = Vector2D(ordinate=-13, abscissa=12)

    assert vector.abscissa == 12
    assert vector.ordinate == -13


def test_read_attributes4():
    vector = Vector2D(12, ordinate=-13)

    assert vector.abscissa == 12
    assert vector.ordinate == -13


def test_read_attributes5():
    vector = Vector2D(12)

    assert vector.abscissa == 12
    assert vector.ordinate == 0


def test_read_attributes6():
    vector = Vector2D(abscissa=12)

    assert vector.abscissa == 12
    assert vector.ordinate == 0


def test_read_attributes7():
    vector = Vector2D(ordinate=-13)

    assert vector.abscissa == 0
    assert vector.ordinate == -13


def test_read_default_attributes():
    vector = Vector2D()

    assert vector.abscissa == 0
    assert vector.ordinate == 0


def test_write_attributes():
    vector = Vector2D()

    with pytest.raises(AttributeError):
        vector.abscissa = 2

    with pytest.raises(AttributeError):
        vector.ordinate = 2


def test_print():
    old_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    print(Vector2D(1, -2), end="")

    sys.stdout = old_stdout
    output = captured_output.getvalue()
    assert (
        output == "Vector2D(abscissa=1, ordinate=-2)" 
        or output == "Vector2D(abscissa=1., ordinate=-2.)"
        or output == "Vector2D(abscissa=1.0, ordinate=-2.0)" 
    )



@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, True, id="eq"),
        pytest.param(0.1 + 0.2, 0.1 + 0.2, 0.3, 0.3, True, id="smart eq"),
        pytest.param(1, 2, 2, 2, False, id="not eq abscissa"),
        pytest.param(1, 2, 1, 1, False, id="not eq ordinate"),
        pytest.param(1, 2, 2, 1, False, id="not eq abscissa and ordinate"),
    ],
)
def test_eq(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 == vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="eq-list"),
        pytest.param({}, id="eq-dict"),
        pytest.param("1", id="eq-str"),
        pytest.param(1, id="eq-int"),
        pytest.param(1.5, id="eq-float"),
    ],
)
def test_validate_eq(err_vector):
    vector = Vector2D()

    assert not vector == err_vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, False, id="not ne"),
        pytest.param(0.1 + 0.2, 0.1 + 0.2, 0.3, 0.3, False, id="smart not ne"),
        pytest.param(1, 2, 2, 2, True, id="ne abscissa"),
        pytest.param(1, 2, 1, 1, True, id="ne ordinate"),
        pytest.param(1, 2, 2, 1, True, id="ne abscissa and ordinate"),
    ],
)
def test_ne(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 != vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="ne-list"),
        pytest.param({}, id="ne-dict"),
        pytest.param("1", id="ne-str"),
        pytest.param(1, id="ne-int"),
        pytest.param(1.5, id="ne-float"),
    ],
)
def test_validate_ne(err_vector):
    vector = Vector2D()

    assert vector != err_vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, False, id="eq"),
        pytest.param(0.3, 0.3, 0.1 + 0.2, 0.1 + 0.2, False, id="smart eq"),
        pytest.param(1, 3, 2, 2, True, id="lt abscissa"),
        pytest.param(1, 2, 1, 3, True, id="lt ordinate"),
        pytest.param(0.3, 2, 0.1 + 0.2, 3, True, id="smart lt ordinate"),
        pytest.param(2, 2, 1, 3, False, id="not lt abscissa"),
        pytest.param(1, 3, 1, 2, False, id="not lt ordinate"),
        pytest.param(0.3, 3, 0.1 + 0.2, 2, False, id="smart not lt ordinate"),
    ],
)
def test_lt(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 < vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="lt-list"),
        pytest.param({}, id="lt-dict"),
        pytest.param("1", id="lt-str"),
        pytest.param(1, id="lt-int"),
        pytest.param(1.5, id="lt-float"),
    ],
)
def test_validate_lt(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector < err_vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, True, id="eq"),
        pytest.param(0.3, 0.3, 0.1 + 0.2, 0.1 + 0.2, True, id="smart eq"),
        pytest.param(1, 3, 2, 2, True, id="lt abscissa"),
        pytest.param(1, 2, 1, 3, True, id="lt ordinate"),
        pytest.param(0.1 + 0.2, 2, 0.3, 3, True, id="smart lt ordinate"),
        pytest.param(2, 2, 1, 3, False, id="not lt abscissa"),
        pytest.param(1, 3, 1, 2, False, id="not lt ordinate"),
    ],
)
def test_le(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 <= vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="le-list"),
        pytest.param({}, id="le-dict"),
        pytest.param("1", id="le-str"),
        pytest.param(1, id="le-int"),
        pytest.param(1.5, id="le-float"),
    ],
)
def test_validate_le(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector <= err_vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, False, id="eq"),
        pytest.param(0.1 + 0.2, 0.1 + 0.2, 0.3, 0.3, False, id="smart eq"),
        pytest.param(2, 2, 1, 3, True, id="gt abscissa"),
        pytest.param(1, 3, 1, 2, True, id="gt ordinate"),
        pytest.param(0.3, 3, 0.1 + 0.2, 2, True, id="smart gt ordinate"),
        pytest.param(1, 3, 2, 2, False, id="not gt abscissa"),
        pytest.param(1, 2, 1, 3, False, id="not lt ordinate"),
    ],
)
def test_gt(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 > vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="gt-list"),
        pytest.param({}, id="gt-dict"),
        pytest.param("1", id="gt-str"),
        pytest.param(1, id="gt-int"),
        pytest.param(1.5, id="gt-float"),
    ],
)
def test_validate_gt(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector > err_vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 2, 1, 2, True, id="eq"),
        pytest.param(0.1 + 0.2, 0.1 + 0.2, 0.3, 0.3, True, id="smart eq"),
        pytest.param(2, 2, 1, 3, True, id="gt abscissa"),
        pytest.param(1, 3, 1, 2, True, id="gt ordinate"),
        pytest.param(0.3, 3, 0.1 + 0.2, 2, True, id="smart gt ordinate"),
        pytest.param(1, 3, 2, 2, False, id="not gt abscissa"),
        pytest.param(1, 2, 1, 3, False, id="not lt ordinate"),
    ],
)
def test_ge(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)

    assert (vector1 >= vector2) == expected


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="ge-list"),
        pytest.param({}, id="ge-dict"),
        pytest.param("1", id="ge-str"),
        pytest.param(1, id="ge-int"),
        pytest.param(1.5, id="ge-float"),
    ],
)
def test_validate_ge(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector >= err_vector


def test_abs():
    vector = Vector2D(0.1, 0.3)

    assert abs(vector) == 0.31622776601683794


@pytest.mark.parametrize(
    "abscissa, ordinate, expected",
    [
        pytest.param(0, 0, False, id="zero"),
        pytest.param(1, 0, True, id="nonzero abscissa"),
        pytest.param(0, 1, True, id="nonzero ordinate"),
        pytest.param(-1, 1, True, id="all nonzero"),
        pytest.param(0.1 + 0.2 - 0.3, 0.1 + 0.2 - 0.3, False, id="smart zero"),
    ],
)
def test_bool(abscissa, ordinate, expected):
    vector = Vector2D(abscissa, ordinate)

    assert bool(vector) == expected


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, 0.6, 0.3, 0.15, 0.18, id="normal"),
        pytest.param(0.5, 0.6, 0, 0, 0, id="zero num"),
        pytest.param(0.5, 0.6, -0.3, -0.15, -0.18, id="negative num"),
    ],
)
def test_mul_num_rigth(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = vector * num

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, 0.6, 0.3, 0.15, 0.18, id="normal"),
        pytest.param(0.5, 0.6, 0, 0, 0, id="zero num"),
        pytest.param(0.5, 0.6, -0.3, -0.15, -0.18, id="negative num"),
    ],
)
def test_mul_num_left(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = num * vector

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="mul-list"),
        pytest.param({}, id="mul-dict"),
        pytest.param("1", id="mul-str"),
        pytest.param(Vector2D(), id="mul-vector"),
    ],
)
def test_validate_mul(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector * err_vector

    with pytest.raises(TypeError):
        err_vector * vector


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.9, -0.6, 0.3, 3, -2, id="normal"),
        pytest.param(0.9, -0.6, -0.3, -3, 2, id="negative num"),
    ],
)
def test_div_num_rigth(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = vector / num

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


def test_validate_div_num_left():
    vector = Vector2D()

    with pytest.raises(TypeError):
        5 / vector


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="mul-list"),
        pytest.param({}, id="mul-dict"),
        pytest.param("1", id="mul-str"),
        pytest.param(Vector2D(), id="mul-vector"),
    ],
)
def test_validate_div(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector / err_vector

    with pytest.raises(TypeError):
        err_vector / vector


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, 0.3, 0.8, -0.3, id="normal"),
        pytest.param(0.5, -0.6, 0, 0.5, -0.6, id="zero num"),
        pytest.param(0.5, -0.6, -0.3, 0.2, -0.9, id="negative num"),
    ],
)
def test_add_num_rigth(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = vector + num

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, 0.3, 0.8, -0.3, id="normal"),
        pytest.param(0.5, -0.6, 0, 0.5, -0.6, id="zero num"),
        pytest.param(0.5, -0.6, -0.3, 0.2, -0.9, id="negative num"),
    ],
)
def test_add_num_left(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = num + vector

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, 0.3, 0.8, 0.8, 0.2, id="normal"),
        pytest.param(-0.5, 0.6, 0.3, 0.8, -0.2, 1.4, id="normal2"),
        pytest.param(0.5, 0.6, -0.3, -0.8, 0.2, -0.2, id="normal3"),
    ],
)
def test_add_vector(abscissa1, ordinate1, abscissa2, ordinate2, res_abscissa, res_ordinate):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)
    res = vector1 + vector2

    assert res is not vector1
    assert res is not vector2
    assert math.isclose(vector1.abscissa, abscissa1)
    assert math.isclose(vector1.ordinate, ordinate1)
    assert math.isclose(vector2.abscissa, abscissa2)
    assert math.isclose(vector2.ordinate, ordinate2)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="add-list"),
        pytest.param({}, id="add-dict"),
        pytest.param("1", id="add-str"),
    ],
)
def test_validate_add(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector + err_vector

    with pytest.raises(TypeError):
        err_vector + vector


@pytest.mark.parametrize(
    "abscissa, ordinate, num, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, 0.3, 0.2, -0.9, id="normal"),
        pytest.param(0.5, -0.6, 0, 0.5, -0.6, id="zero num"),
        pytest.param(0.5, -0.6, -0.3, 0.8, -0.3, id="negative num"),
    ],
)
def test_sub_num_left(abscissa, ordinate, num, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = vector - num

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, 0.3, 0.8, 0.2, -1.4, id="normal"),
        pytest.param(-0.5, 0.6, 0.3, 0.8, -0.8, -0.2, id="normal2"),
        pytest.param(0.5, 0.6, -0.3, -0.8, 0.8, 1.4, id="normal3"),
    ],
)
def test_sub_vector(abscissa1, ordinate1, abscissa2, ordinate2, res_abscissa, res_ordinate):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)
    res = vector1 - vector2

    assert res is not vector1
    assert res is not vector2
    assert math.isclose(vector1.abscissa, abscissa1)
    assert math.isclose(vector1.ordinate, ordinate1)
    assert math.isclose(vector2.abscissa, abscissa2)
    assert math.isclose(vector2.ordinate, ordinate2)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="sub-list"),
        pytest.param({}, id="sub-dict"),
        pytest.param("1", id="sub-str"),
    ],
)
def test_validate_sub_rigth(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector - err_vector


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="sub-list"),
        pytest.param({}, id="sub-dict"),
        pytest.param("1", id="sub-str"),
        pytest.param(1, id="sub-int"),
        pytest.param(1.5, id="sub-float"),
    ],
)
def test_validate_sub_left(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        err_vector - vector


@pytest.mark.parametrize(
    "abscissa, ordinate, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, -0.6, -0.5, 0.6, id="normal"),
        pytest.param(-0.5, 0.6, 0.5, -0.6, id="normal2"),
        pytest.param(0, 0, 0, 0, id="zero"),
    ],
)
def test_neg(abscissa, ordinate, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = -vector

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)


@pytest.mark.parametrize(
    "abscissa, ordinate, res_real, res_imag",
    [
        pytest.param(0.5, -0.6, 0.5, -0.6, id="normal"),
        pytest.param(-0.5, 0.6, -0.5, 0.6, id="normal2"),
        pytest.param(0, 0, 0, 0, id="zero"),
    ],
)
def test_to_complex(abscissa, ordinate, res_real, res_imag):
    vector = Vector2D(abscissa, ordinate)
    res = complex(vector)

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.real, res_real)
    assert math.isclose(res.imag, res_imag)


@pytest.mark.parametrize(
    "abscissa, ordinate, expected",
    [
        pytest.param(0.5, 0.6, 0.7810249675906654, id="normal"),
        pytest.param(-0.5, 0.6, 0.7810249675906654, id="normal2"),
        pytest.param(0.5, -0.6, 0.7810249675906654, id="normal3"),
        pytest.param(-0.5, -0.6, 0.7810249675906654, id="normal4"),
        pytest.param(0, 0, 0, id="zero"),
    ],
)
def test_to_float(abscissa, ordinate, expected):
    vector = Vector2D(abscissa, ordinate)
    res = float(vector)

    assert math.isclose(res, expected)


@pytest.mark.parametrize(
    "abscissa, ordinate, expected",
    [
        pytest.param(1.5, 1.6, 2, id="normal"),
        pytest.param(-1.5, 1.6, 2, id="normal2"),
        pytest.param(1.5, -1.6, 2, id="normal3"),
        pytest.param(-1.5, -1.6, 2, id="normal4"),
        pytest.param(0, 0, 0, id="zero"),
    ],
)
def test_to_int(abscissa, ordinate, expected):
    vector = Vector2D(abscissa, ordinate)
    res = int(vector)

    assert res == expected


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 0, 0, 1, 0, id="normal"),
        pytest.param(0.5, 0.6, 0.3, 0.8, 0.63, id="normal2"),
        pytest.param(-0.5, 0.6, -0.3, 0.8, 0.63, id="normal3"),
        pytest.param(-0.5, -0.6, -0.3, -0.8, 0.63, id="normal3"),
        pytest.param(0, 0, 0, 0, 0, id="zero"),
    ],
)
def test_scalar_prod(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)
    res = vector1 @ vector2

    assert res is not vector1
    assert res is not vector2
    assert math.isclose(vector1.abscissa, abscissa1)
    assert math.isclose(vector1.ordinate, ordinate1)
    assert math.isclose(vector2.abscissa, abscissa2)
    assert math.isclose(vector2.ordinate, ordinate2)
    assert math.isclose(res, expected)


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="scalar-prod-list"),
        pytest.param({}, id="scalar-prod-dict"),
        pytest.param("1", id="scalar-prod-str"),
        pytest.param(1, id="scalar-prod-int"),
        pytest.param(1.5, id="scalar-prod-float"),
    ],
)
def test_validate_scalar_prod(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector @ err_vector
    with pytest.raises(TypeError):
        err_vector @ vector


@pytest.mark.parametrize(
    "abscissa1, ordinate1, abscissa2, ordinate2, expected",
    [
        pytest.param(1, 0, 0, 1, 1.5707963267948966, id="normal"),
        pytest.param(0.5, 0.6, 0.3, 0.8, 0.335967605926131, id="normal2"),
        pytest.param(-0.5, 0.6, 0.3, 0.8, 1.0535089464672756, id="normal3"),
        pytest.param(0.5, -0.6, 0.3, 0.8, 2.0880837071225176, id="normal3"),
        pytest.param(0.5, -0.6, -0.3, 0.8, 2.8056250476636624, id="normal3"),
    ],
)
def test_get_angle(abscissa1, ordinate1, abscissa2, ordinate2, expected):
    vector1 = Vector2D(abscissa1, ordinate1)
    vector2 = Vector2D(abscissa2, ordinate2)
    res = vector1.get_angle(vector2)

    assert math.isclose(res, expected)


def test_validate_get_angle1():
    vector1 = Vector2D(1, 1)
    vector2 = Vector2D()

    with pytest.raises(ValueError):
        vector1.get_angle(vector2)


def test_validate_get_angle2():
    vector1 = Vector2D(1, 1)
    vector2 = Vector2D()

    with pytest.raises(ValueError):
        vector2.get_angle(vector1)


@pytest.mark.parametrize(
    "err_vector",
    [
        pytest.param([], id="get-angle-list"),
        pytest.param({}, id="get-angle-dict"),
        pytest.param("1", id="get-angle-str"),
        pytest.param(1, id="get-angle-int"),
        pytest.param(1.5, id="get-angle-float"),
    ],
)
def test_validate_get_angle(err_vector):
    vector = Vector2D()

    with pytest.raises(TypeError):
        vector.get_angle(err_vector)


@pytest.mark.parametrize(
    "abscissa, ordinate, res_abscissa, res_ordinate",
    [
        pytest.param(0.5, 0.6, 0.5, -0.6, id="normal1"),
        pytest.param(-0.5, 0.6, -0.5, -0.6, id="normal2"),
        pytest.param(0.5, -0.6, 0.5, 0.6, id="normal3"),
        pytest.param(-0.5, -0.6, -0.5, 0.6, id="normal4"),
    ],
)
def test_conj(abscissa, ordinate, res_abscissa, res_ordinate):
    vector = Vector2D(abscissa, ordinate)
    res = vector.conj()

    assert res is not vector
    assert math.isclose(vector.abscissa, abscissa)
    assert math.isclose(vector.ordinate, ordinate)
    assert math.isclose(res.abscissa, res_abscissa)
    assert math.isclose(res.ordinate, res_ordinate)
