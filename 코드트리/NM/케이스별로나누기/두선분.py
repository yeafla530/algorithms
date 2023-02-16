# 교차 판단 
x1, x2, x3, x4 = map(int, input().split())
arr = [0] * 101

for i in range(x1, x2+1):
    arr[i] += 1

for i in range(x3, x4+1):
    arr[i] += 1

is_inter = False
for i in range(101):
    if arr[i] >= 2:
        is_inter = True

if is_inter:
    print("intersecting")

else:
    print("nonintersecting")


