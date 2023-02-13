n = int(input())

def calc(n):
    if n < 10:
        return n*n
    
    return calc(n // 10) + (n % 10) ** 2

print(calc(n))

