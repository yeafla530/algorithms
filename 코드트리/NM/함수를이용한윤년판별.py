def is_leap_year(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    return False

n = int(input())

if is_leap_year(n):
    print('true')
else:
    print('false')