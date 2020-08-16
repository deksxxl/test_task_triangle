import pytest
import math
from triangle import Triangle


def test_simple_triangle_square():
    _point1 = [0, 0]
    _point2 = [5, 5]
    _point3 = [0, 10]
    _triangle_square_to_compare = 25.0

    _test_triangle = Triangle(_point1, _point2, _point3)

    _triangle_square = _test_triangle.triangle_square()

    # Говорят так float сравнивать лучшее
    _square_equal_to_compared_num = math.isclose(_triangle_square, _triangle_square_to_compare, rel_tol=1e-5)

    assert _square_equal_to_compared_num


# Набор тестовых данных в формате:
#                point1, point2, point3, square
test_data = (
                ([0, 0], [5, 5], [0, 10], 25.0),
                ([0, 0], [5, 5], [-10, -10], 0.0),
                ([-7.5, 0], [0, -10], [0, 10], 75.0)
                )


@pytest.mark.parametrize("data_list", test_data)
def test_parametrized_triangle_square(data_list):
    _point1 = data_list[0]
    _point2 = data_list[1]
    _point3 = data_list[2]
    _triangle_square_to_compare = data_list[3]

    _test_triangle = Triangle(_point1, _point2, _point3)

    _triangle_square = _test_triangle.triangle_square()

    _square_equal_to_compared_num = math.isclose(_triangle_square, _triangle_square_to_compare, rel_tol=1e-5)

    assert _square_equal_to_compared_num
