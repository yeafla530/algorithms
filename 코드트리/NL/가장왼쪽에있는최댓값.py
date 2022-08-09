# 가장 왼쪽에 있는 최대값의 위치
n = int(input())
arr = list(map(int, input().split()))

prev_idx = n

while True:
    idx = 0
    for i in range(1, prev_idx):
        if arr[i] > arr[idx]:
            idx = i
    print(idx+1, end=' ')
    
    if idx == 0:
        break

    prev_idx = idx


# 두번째풀이
# 가장 왼쪽에 있는 최대값의 위치
n = int(input())
arr = list(map(int, input().split()))
indices = list()

indices.append(0)

for i in range(1, n):
    last_idx = indices[-1]
    if arr[i] > arr[last_idx]:
        print(i)
        indices.append(i)

for idx in indices[::-1]:
    print(idx+1, end=" ")