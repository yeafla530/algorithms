n = int(input())

def down_to_up(n):
    if n == 0:
        return
    
    down_to_up(n-1)
    print(n, end=" ")


def up_to_down(n):
    if n == 0:
        return
    
    print(n, end=" ")
    up_to_down(n-1)



down_to_up(n)
print()
up_to_down(n)

# 다른 정답
n = int(input())

def print_number(a):
    if a == n+1:
        return 
    
    print(a, end=" ")
    print_number(a+1)
    if a == n:
        print()
    print(a, end=" ")    


print_number(1)