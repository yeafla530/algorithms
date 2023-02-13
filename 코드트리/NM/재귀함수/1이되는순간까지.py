n = int(input())

def calc(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return calc(n // 2) + 1
    else:
        return calc(n//3) + 1

print(calc(n))