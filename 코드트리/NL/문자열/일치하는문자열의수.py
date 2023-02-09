n, a = input().split()
n = int(n)
count = 0
for i in range(n):
    s = input()

    if s == a:
        count += 1
    
print(count)