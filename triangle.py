"""
Класс, описывающий треугольник.

Инициализатор класса принимает три пары координат вершин треугольника.

Класс имеет:

* метод для расчета площади треугольника;

* метод для расчета периметра треугольника;

* метод, определяющий, может ли существовать данный треугольник. (True/False)

* Предполагается, что на вход будут подаваться только валидные данные
"""


class Triangle:
    def __init__(self, point1, point2, point3):
        """
        :param point1: список из 2х элементов, обозначающий координату вершины
        :param point2: список из 2х элементов, обозначающий координату вершины
        :param point3: список из 2х элементов, обозначающий координату вершины
        """

        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

        # Вычисляем сразу длины треугольника (можно и отдельно, но почему бы и не сразу)
        self.__all_sides_len()

    def __all_sides_len(self):
        """
        Создаем переменные и вычисляем длины сторон треугольника
        """

        self.__side1_len = self.__side_len(self.__point1, self.__point2)
        self.__side2_len = self.__side_len(self.__point2, self.__point3)
        self.__side3_len = self.__side_len(self.__point3, self.__point1)

    def __side_len(self, point1, point2):
        """
        Вычисление длины стороны треугольника по координатам двух вершин

        :param point1: список из 2х элементов, обозначающий координату вершины
        :param point2: список из 2х элементов, обозначающий координату вершины
        :return: длина стороны
        """

        _side_len = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
        return _side_len

    def print_points(self):
        """
        Выводит вершины созданного треугольника

        Для красоты
        """

        print("Triangle created with points:")
        print(self.__point1)
        print(self.__point2)
        print(self.__point3)

    def print_triangle_side_len(self):
        """
        Выводит длины сторон созданного треугольника

        Для красоты
        """

        print("The lengths of the triangle' sides :")
        print("Side 1 = " + str(self.__side1_len))
        print("Side 2 = " + str(self.__side2_len))
        print("Side 3 = " + str(self.__side3_len))

    def __half_per(self):
        """
        Вычисление полупериметра треугольника

        :return: полупериметр треугольника
        """

        _half_per = self.triangle_perimeter() / 2
        return _half_per

    def triangle_perimeter(self):
        """
        Вычисление периметра треугольника

        :return: периметр треугольника
        """

        _per = (self.__side1_len + self.__side2_len + self.__side3_len)
        return _per

    def triangle_square(self):
        """
        Вычисление площади треугольника

        :return: площадь треугольника
        """

        _half_p = self.__half_per()
        _sq = ((_half_p
                * (_half_p - self.__side1_len)
                * (_half_p - self.__side2_len)
                * (_half_p - self.__side3_len)
                )
               ** 0.5)
        return _sq

    def triangle_exist(self):
        """
        Проверяем возможность существования треугольника:
          Каждая сторона не равна нулю
          Сумма двух сторон больше третьей

        :return: bool
        """

        _triangle_exist_bool = False
        if self.__all_sides_len_non_zero():
            _triangle_exist_bool = (self.__side1_len + self.__side2_len > self.__side3_len
                                    and self.__side2_len + self.__side3_len > self.__side1_len
                                    and self.__side3_len + self.__side1_len > self.__side2_len)
        return _triangle_exist_bool

    def __all_sides_len_non_zero(self):
        """
        Проверка, что все стороны больше нуля

        :return: bool
        """

        _bool = self.__side1_len > 0 and self.__side2_len > 0 and self.__side3_len > 0
        return _bool
