def make_fibonacci_value(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = make_fibonacci_value(n - 1) + make_fibonacci_value(n - 2)

    return x
