
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_subsequence(a, b):
    for i in range(n-m+1):
        if a[i:i+m] == b:
            return True
    return False


if is_subsequence(a, b):
    print("Yes")
else:
    print("No")