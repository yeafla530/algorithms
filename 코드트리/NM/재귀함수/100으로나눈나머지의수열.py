n = int(input())

def calc(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return calc(n-1) * calc(n-2) % 100

print(calc(n))