n = int(input())
s = n
re = False
for i in range(2*s-1):
    for z in range(n-s):
        print("  ", end="")
    for j in range(2*s-1):
        print('*', end=" ")

    if s > 1 and not re:
        s -= 1
    else:
        re = True
        s += 1

    print()
