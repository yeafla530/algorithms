# 최댓값
n = int(input())
arr = list(map(int, input().split()))

def select(n):
    if n == 0:
        return arr[0]
        
    return max(select(n-1), arr[n])



print(select(n-1))