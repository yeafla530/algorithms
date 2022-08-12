m1, d1, m2, d2 = map(int, input().split())

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def num_of_days(m, d):
    total_days = 0
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(1, m):
        total_days += days[i]
    
    total_days += d

    return total_days

# print(num_of_days(m2, d2), num_of_days(m1, d1))
compare = num_of_days(m2, d2) - num_of_days(m1, d1)
# print(compare)
index = compare % 7

print(week[index])