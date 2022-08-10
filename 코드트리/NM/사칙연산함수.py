def c_sum(a, b):
    return a + b
def c_sub(a, b):
    return a - b
def c_div(a, b):
    return a // b
def c_mul(a, b):
    return a * b

a, s, b = input().split()
a, b = int(a), int(b)
if s == "+":
    print(f'{a} {s} {b} = {c_sum(a, b)}')
elif s == "-":
    print(f'{a} {s} {b} = {c_sub(a, b)}')
elif s == "/":
    print(f'{a} {s} {b} = {c_div(a, b)}')
elif s == "*":
    print(f'{a} {s} {b} = {c_mul(a, b)}')
else:
    print("False")
