MOD = 4
DIGIT_NUM = 10
# 자릿수가 A ~ B인 수 중 각 자리 숫자의 합이 4의 배수가 되는 수의 개수를 세는 프로그램을 작성해보세요.
# 예를 들어 수 75는 각 자리 숫자의 합이 7 + 5 = 12 이므로 그 합이 4의 배수가 되는 수입니다.
a, b = map(int, input().split())
ans = 0

def find_num(num_of_digits, sum_val):
    global ans

    if a <= num_of_digits <= b and sum_val % MOD == 0:
        ans += 1

    if num_of_digits == b:
        return
    
    # 0~9까지
    for i in range(DIGIT_NUM):
        if num_of_digits == 0 and i == 0:
            continue

        find_num(num_of_digits+1, sum_val+i) 

find_num(0, 0)

print(ans)