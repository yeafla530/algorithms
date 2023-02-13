def g(x):
    return 10 if x < 10 else g(int(x / 10)) + (x % 10)

def f(a, b):
    c = 1
    while b:
        c *= a
        b -= 1
    return g(c)

print(f(2, 5))
