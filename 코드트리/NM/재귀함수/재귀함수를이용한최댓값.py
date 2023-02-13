n = int(input())
arr = list(map(int, input().split()))

def max_num(n):
    if n == 0:
        return arr[0]

    return max(max_num(n-1), arr[n]) 

print(max_num(n-1))
