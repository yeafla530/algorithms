import sys
si = sys.stdin.readline

target_date = si().strip()

# 가능한 모든 날짜 받기
def get_date_formats():
    dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Y, M, D = 1950, 1, 1
    ret = []
    while Y < 2050:
        ret.append((f'{Y}{M:02d}{D:02d}', f'{Y}{M:02d}{D:02d}'))
        ret.append((f'{M:02d}{D:02d}{Y}', f'{Y}{M:02d}{D:02d}'))
        ret.append((f'{D:02d}{M:02d}{Y}', f'{Y}{M:02d}{D:02d}'))

        # day > month > year순으로 계산해주기
        D += 1
        if dates[M] < D:
            if Y % 4 == 0 and M == 2 and D == 28:
                pass

            else:
                M += 1
                D = 1

        if M > 12:
            M = 1
            Y += 1

    return ret

# 전체 날짜 받기
whole_dates = get_date_formats()
ans = None

for candidate_date in whole_dates:
    if all(t == c or t == '?' for t, c in zip(target_date, candidate_date[0])):
        if ans is None: # 처음으로 매칭된 순간
            ans = candidate_date[1]
        
        else: # 또다른 매칭이 가능한 것
            print('?')
            exit()

if ans is None:
    print('x')
else:
    print(ans)

