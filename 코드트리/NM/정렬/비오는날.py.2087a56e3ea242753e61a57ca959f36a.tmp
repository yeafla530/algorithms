import sys

n = int(input())
arr = []
for _ in range(n):
    date, day, weather = input().split()
    arr.append([date, day, weather])

arr.sort(key=lambda x: (x[0]))

for i in range(n):
    if arr[i][2] == "Rain":
        print(arr[i][0], arr[i][1], arr[i][2])
        sys.exit()
