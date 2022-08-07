n = int(input())
s = n-1
a = 1
re = False

for i in range(2*n-1):
    for x in range(s):
        print("  ", end="")
    for y in range(a):
        print("@", end=" ")
    
    if a < n and not re:
        a += 1
    else:
        re = True
        a -= 1
    s -= 1
    print()