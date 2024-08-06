from math import inf


def divide(x, y) -> float:
    if y == 0:
        return inf
    else:
        return x/y


if __name__ == "__main__":
    print(divide(10, 3))
    print(divide(10, 0))

