n, m = map(int, input().split())

def greatest_common_factor(n, m):
    gcd = 0
    
    for i in range(min(n, m), 0, -1):
        if m % i == 0 and n % i == 0:
            gcd = i
            print(gcd)
            break



greatest_common_factor(n, m)
