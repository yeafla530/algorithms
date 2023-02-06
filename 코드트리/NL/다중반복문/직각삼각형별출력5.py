n = int(input())

for i in range(n, 0, -1):
    # 4 3 2 1
    for j in range(i):  
        print("*"*i, end=" ")
    print()