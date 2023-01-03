n, k = map(int, input().split())
arr = []
def permutation(cnt):
    global n, k, arr
    if cnt == k:
        for i in range(cnt):
            print(arr[i], end=" ")
        print()
        return
    
    for i in range(n, 0, -1):
        arr.append(i)
        permutation(cnt+1)
        arr.pop()

permutation(0)