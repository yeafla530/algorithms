import math

m, n = map(int, input().split())

def check(num):
    if num == 2:
        return True

    if num == 1 or num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    
    return True



for num in range(m, n+1):
    if check(num):
        print(num)