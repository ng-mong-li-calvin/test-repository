def add(a, b):
    return a + b


def test():
    assert not add(3, 5) == 1
    assert add(6, 2) == 8


def main():
    test()


if __name__ == '__main__':
    main()
