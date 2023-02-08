arr = list(map(int, input().split()))

min_result = 1000
max_result = -1000

for elem in arr:
    if elem == 999 or elem == -999:
        print(max_result, min_result)
        break 
    
    if min_result > elem:
        min_result = elem
    
    if max_result < elem:
        max_result = elem