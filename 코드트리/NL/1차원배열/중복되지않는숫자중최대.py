n = int(input())
arr = list(map(int, input().split()))

max_num = -1

for cur_num in arr:
    if max_num < cur_num:
        count = 0

        for elem in arr:
            if elem == cur_num:
                count += 1
        
        if count == 1:
            max_num = cur_num

print(max_num)