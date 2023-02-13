def f(a, b):
    if a < b or b == 0:
        return 1
    return f(a - 2, b - 1) + f(a - 1, b) * b

print(f(4, 3))