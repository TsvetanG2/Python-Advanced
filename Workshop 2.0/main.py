array = [1, "hello", False, None, 4.5]


def all(array):
    for el in array:
        if not el:
            return False

    return True


def any(array):
    for el in array:
        if el:
            return True

    return False