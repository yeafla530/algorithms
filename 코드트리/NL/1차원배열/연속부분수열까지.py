n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


for i in range(n1):
    is_true = True
    for j in range(n2):
        if a[i+j] != b[j]:
            is_true = False
            break
        
    
    if is_true == True:
        print("Yes")
        break
if is_true == False:
    print("No")
