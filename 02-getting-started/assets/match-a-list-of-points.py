points = []
# points = [(12, 0)]
# points = [(0, 0)]
# points = [(89, 12), (0, 1), (0, 3)]
# points = [(0, 12), (0, 0), (1, 3)]

match points:
    case []:
        print("Empty list!")

    case [(0, 0)]:
        print("Single origin point.")

    case [(0, y), *_]: # *_ matches any number of elements after (0, y)
        print(f"The FIRST point's X is zero, and Y is {y}")

    case [*_, (0, y)]: # *_ matches any number of elements first and then (0, y)
        print(f"The LAST point's X is zero, and its Y is {y}")

    case [(x, 0)]:
        print(f"Single point which its X is {x}, and its Y is zero")

    case [(x, y)]:
        print(f"Single point at {x} on the x-axis and {y} on the y-axis")

    case _:
        raise ValueError("Not a handled!")