# A ≤ B ≤ C ≤ D 
# C <= a + b
# A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D

arr = list(map(int, input().split()))
arr.sort()

a = arr[0]
b = arr[1]
c = arr[2]
d = arr[-1] - a - b - c 

print(a, b, c, d)