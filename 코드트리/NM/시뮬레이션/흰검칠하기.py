n = int(input())
count = [[0, 0] for _ in range(200001)]
arr = [0] * 200001
start = 100000
# print(count)

for _ in range(n):
    num, p = input().split()
    num = int(num)
    # print(num)

    if p == "R":
        count[start][0] += 1
        arr[start] = 2
        for _ in range(num-1):
            start += 1
            count[start][0] += 1
            arr[start] = 2
            # print(count[start], start)
    else:
        arr[start] = 1
        count[start][1] += 1
        for _ in range(num-1):
            start -= 1
            arr[start] = 1
            count[start][1] += 1
    




color = [0, 0, 0]
for i in range(len(count)):
    if count[i][0] >= 2 and count[i][1] >= 2:
        color[2] += 1
    else:
        if arr[i] == 1:
            color[0] += 1
        elif arr[i] == 2:
            color[1] += 1

print(*color)
