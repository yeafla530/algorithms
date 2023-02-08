arr = list(map(int, input().split()))

max_num = 0
for elem in arr:
    if elem > max_num:
        max_num = elem

print(max_num)