arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    print(round(sum(arr[i]) / 4, 1), end=" ")

print()
for j in range(4):
    result = 0
    for i in range(2):
        result += arr[i][j]
    
    print(round(result / 2, 1), end=" ")

print()

result = 0
for i in range(2):
    for j in range(4):
        result += arr[i][j]

print(round(result/8, 1))