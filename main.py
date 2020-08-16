import triangle as tr

if __name__ == '__main__':
    point1 = [55, 0]
    point2 = [0, -10]
    point3 = [-1.124, 10]

    # Start
    print("Start:\n")

    some_triangle = tr.Triangle(point1, point2, point3)

    some_triangle.print_points()
    print()

    some_triangle.print_triangle_side_len()
    print()

    print("Triangle exist:")
    print(some_triangle.triangle_exist())

    if some_triangle.triangle_exist():
        print("Triangle' perimeter:")
        print(some_triangle.triangle_perimeter())
        print("Triangle' square:")
        print(some_triangle.triangle_square())
