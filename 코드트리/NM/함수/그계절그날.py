def is_possible(y, m, d):
    if 1 <= m <= 7:
        if m % 2:
            if 1 <= d <= 31:
                return True
            return False
        else:
            if y % 4 == 0 and m == 2:
                if 1 <= d <= 29:
                    return True
                else:
                    return False
            
            if 1 <= d <= 30:
                return True
            return False
                


    elif 8 <= m <= 12:
        if m % 2 == 0:
            if 1 <= d <= 31:
                return True
            return False

        else:
            if 1 <= d <= 30:
                return True
            return False
    else:    
        return False

def print_season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"


y, m, d = map(int, input().split())

if is_possible(y, m, d):
    print(print_season(m))

else:   
    print(-1)



# 정답 코드
y, m, d = map(int, input().split())

# 윤년 판단 함수 
def is_leap_year(y):
    # 4의 배수가 아니라면 윤년 확실히 아님
    if y % 4 != 0:
        return False
    
    # 4의 배수임을 가정 
    # 그중 100의 배수가 아니라면 윤년
    if y % 100 != 0:
        return True
    
    # 400의 배수라면 확실히 윤년
    if y % 400 == 0:
        return True
    
    # 100의 배수지만 400의 배수가 아님
    # 따라서 확실히 윤년이 아님
    return False



# 존재하는 날인지 판단
def is_exist_day(y, m, d):
    num_of_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    num_of_days[2] = 29 if is_leap_year(y) else 28
    return d <= num_of_days[m]

# 계절 판단 함수
def season():
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    else:
        print("Winter")


if is_exist_day(y, m, d):
    season()
else:
    print(-1)
