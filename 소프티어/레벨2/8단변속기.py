
arr = list(map(int, input().split()))
# ascending , descending
check = [False] * 2

r = arr[0]
for i in range(1, 8):
    if r < arr[i]:
        check[0] = True
    
    else:
        check[1] = True

    r = arr[i]


if check.count(True) == 2:
    print("mixed")

else:
    if check[0] == True:
        print("ascending")
    
    else:
        print("descending")