n = int(input()) # 6

def to_one(n):# 3 1
    if n == 1:
        return 0
    if n % 2 == 0:
     
        return to_one(n // 2) + 1
    else:
     
        return to_one(n // 3) + 1

print(to_one(n))