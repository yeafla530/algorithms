def is_exist(m, d):
    if m <= 12 and d <= 31:
        if m == 2 and d <= 28:
            return True
        elif (m % 2 == 0 and m != 2) and d <= 30:
            return True
        elif (m % 2 != 0 or m == 8) and d <= 31:
            return True
    return False


m, d = map(int, input().split())

if is_exist(m, d):
    print("Yes")
else:
    print("No")