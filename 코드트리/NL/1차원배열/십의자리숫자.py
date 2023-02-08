arr = list(map(int, input().split()))
nums = [0 for _ in range(10)]

for elem in arr:
    if elem == 0:
        break
    nums[elem // 10] += 1


for i in range(1, 10):
    print(f"{i} - {nums[i]}")

