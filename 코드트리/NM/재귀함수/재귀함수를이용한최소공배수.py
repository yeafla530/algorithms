n = int(input())
arr = list(map(int, input().split()))

def calc(n):
    if n == 1:
        return 1
    
    for i in range(2, n+1):
        is_div = False
        for j in range(len(arr)):
            if arr[j] % i == 0:
                arr[j] = arr[j] // i
                is_div = True
        
        if is_div:
            return calc(max(arr[:])) * i
            break



print(calc(max(arr[:])))