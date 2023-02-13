n = int(input())

def print_sum(n):
    if n == 1:
        return 1
    
    return print_sum(n-1) + n

print(print_sum(n))