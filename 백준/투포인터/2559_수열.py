# O(n^2)안됨 
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 누적합
prefix_sum = [0] * (n-(k-1))

for i in range(n):
    

