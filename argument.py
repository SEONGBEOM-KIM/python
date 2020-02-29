def plus(*args):
    result = 0
    for number in args:
        result += number
    print(result)


plus(1, 3, 4, 6, 9, 3, 3, 4, 2, 1)
