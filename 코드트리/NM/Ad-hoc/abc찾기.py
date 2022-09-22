# A, B, C, A + B, B + C, C + A, A + B + C 
arr = list(map(int, input().split()))
arr.sort()

a = arr[0]
b = arr[1]
abc = arr[-1]

bc = abc - a 
c = bc - b 
print(a, b, c)

