n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0] * (n+1)

def get_sum(s, e):
    # print(s, e)
    return prefix[e] - prefix[s-1]

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i]

result = 0
# cnt = 1~n까지
for cnt in range(1, n+1):
    for i in range(1, n-cnt+2):
        if get_sum(i, i+cnt-1) == k:
            result += 1


print(result)

