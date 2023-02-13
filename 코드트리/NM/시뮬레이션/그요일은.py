m1, d1, m2, d2 = map(int, input().split())
a = input()
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
seven = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def compare_days(m1, d1, m2, d2):
    s = 0
    if m2 == m1:
        s += d2 - d1
    else:
        s += days[m1] - d1
        s += d2

        for i in range(m1+1, m2):
            s += days[i]
        

    return s

s = compare_days(m1, d1, m2, d2)
a_idx = seven.index(a)

# print(a_idx)

print((s-a_idx) // 7 + 1)