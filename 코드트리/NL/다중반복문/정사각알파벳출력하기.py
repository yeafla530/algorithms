n = int(input())

a = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(a), end="")
        a += 1
    print()