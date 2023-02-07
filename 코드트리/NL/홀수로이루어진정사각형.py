n = int(input())

for i in range(n):
    for j in range(i, n+i):
        print(10+(2*j+1), end=" ")
    print()
