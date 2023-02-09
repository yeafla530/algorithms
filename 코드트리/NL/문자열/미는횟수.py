a = input()
b = input()

count = 0
for i in range(len(a)):
    a = a[-1] + a[:-1]
    count += 1

    if a == b:
        break
    
if count == len(a):
    print(-1)
else:
    print(count)

