# O(n^2)안됨 
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# 누적합
prefix_sum = [0] * (n-(k-1))

j = 0
for i in range(1, n):
    print(i)
