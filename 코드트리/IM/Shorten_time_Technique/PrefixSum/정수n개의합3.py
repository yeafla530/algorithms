n, k = map(int, input().split())
arr = [[0] * (n + 1)] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]
prefix_sum = [[0]*(n+1) for _ in range(n+1)]

