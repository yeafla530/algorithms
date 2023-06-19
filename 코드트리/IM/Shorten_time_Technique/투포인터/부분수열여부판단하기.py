n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

def is_sub():
    i = 1

    for j in range(1, m+1):
        while i <= n and a[i] != b[j]:
            i += 1
        
        if i == n+1:
            return False
        
        else:
            i+=1

    return True

if is_sub():
    print("Yes")

else:
    print("No")