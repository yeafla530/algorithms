n = int(input())
arr = list(map(float, input().split()))

num = sum(arr)
avg = round(num / n, 1)


print(avg)
if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")