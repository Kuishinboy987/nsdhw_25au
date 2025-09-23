import math
import pytest
import _vector

def test_same_direction():
    assert math.isclose(_vector.angle(1, 0, 2, 0), 0.0, rel_tol=1e-9)

def test_opposite_direction():
    assert math.isclose(_vector._angle(1, 0, -1, 0), math.pi, rel_tol=1e-9)

def test_perpendicular():
    assert math.isclose(_vector._anglee(1, 0, 0, 1), math.pi/2, rel_tol=1e-9)

def test_general_case():
    angle = _vector._angle(1, 1, 1, 0)
    expected = math.pi / 4
    assert math.isclose(angle, expected, rel_tol=1e-9)

def test_zero_vector():
    with pytest.raises(ValueError):
        _vector.angle(0, 0, 1, 0)
