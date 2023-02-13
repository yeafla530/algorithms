n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    s = 0
    a, b = map(int, input().split())

    s = sum(arr[a-1:b])

    print(s)

# 정답
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

def get_answer(a, b):
    return_value = 0
    for i in range(a, b+1):
        return_value += arr[i]
    
    return return_value



for _ in range(m):
    a, b = map(int, input().split())
    print(get_answer(a, b))