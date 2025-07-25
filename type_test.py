def add(a, b):
    if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
        raise TypeError("Both arguments must be int, float, or str")
    if type(a) is not type(b):
        raise TypeError("Both arguments must be of the same type")
    return a + b


if __name__ == "__main__":
    a = "cat"
    b = 10

    add(a, b)
