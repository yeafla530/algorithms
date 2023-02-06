n = int(input())

for i in range(0, n):
    for _ in range(2*i+1):
        print("*", end="")
    print()