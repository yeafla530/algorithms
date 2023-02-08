arr = [0 for _ in range(4)]

for _ in range(3):
    yn, temp = input().split()
    temp = int(temp)
    if yn == 'Y' and temp >= 37:
        arr[0] += 1
    elif yn == "N" and temp >= 37:
        arr[1] += 1

    elif yn == "Y" and temp < 37:
        arr[2] += 1
    else:
        arr[3] += 1


print(*arr, end=" ")
if arr[0] >= 2:
    print("E")
 
