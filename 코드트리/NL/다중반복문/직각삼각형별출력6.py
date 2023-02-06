n = int(input())

# 전체적으로 반복할 횟수
# 0, 1, 2, 3, 4
for i in range(0, n):
    # *이 반복될 횟수
    for j in range(0, n-i):
        print("*", end=" ")
    print()