n, a = map(int, input().split())
arr = []

while True:
    if n < a:
        arr.append(n)
        break
    
    arr.append(n % a)
    n = n // a

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end="")
    