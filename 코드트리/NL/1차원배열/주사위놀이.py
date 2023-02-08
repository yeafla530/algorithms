arr = list(map(int, input().split()))

dice = [0 for _ in range(7)]

for elem in arr:
    dice[elem] += 1

for i in range(1, 7):
    print(f"{i} - {dice[i]}")