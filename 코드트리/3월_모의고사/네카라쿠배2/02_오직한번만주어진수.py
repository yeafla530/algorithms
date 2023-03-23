n = int(input())
arr = list(map(int, input().split()))
d = {}
for s in arr:
    if s not in d:
        d[s] = 1
    
    else:
        d[s] += 1

is_print = False
for (k, idx) in d.items():
    if idx == 1:
        is_print = True
        print(k)
        break 
    
if is_print == False:
    print(-1)