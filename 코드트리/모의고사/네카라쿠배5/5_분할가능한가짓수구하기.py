import sys

sys.setrecursionlimit(100000)
MOD = 10007
# 0~9까지 숫자로 구성된 문자열 한개
# 1~32의 숫자들로 분할할 수 있는 방법 가짓수
# 방법의 가짓수를 10007로 나눈 값 출력

# 두가지
# 1. 한자리를 분할하고 나머지 문자열에 대해 분할방법 찾거나
# 2. 두자리를 분할하고 나머지 문자열에 대한 분할방법

# 조건
# 1. 0으로 시작하는 문자열은 분할 불가
# 2. 두자리를 분할했을 때 해당숫자가 32보다 작아야함

input_str = input()

def get_possible_partition(start):
    if start == len(input_str):
        # print()
        return 1
    
    if input_str[start] == '0':
        return 0
    
    # 한글자만 분할했을 때 가능한 가짓수
    # 시작 문자가 '0'이 아닌 경우 1~9중 하나이기 때문에 반드시 분할가능
    # print(input_str[start], end=" ")
    single_num = get_possible_partition(start + 1)

    # 두글자만 분할했을 때 가능한 가짓수 
    # 32까지 숫자만 주어졌기 때문에 부분문자열의 앞 두 글자를 숫자로 바꿨을 때
    # 32보다 작은 경우에만 탐색을 해줌
    double_num = 0
    if start + 1 < len(input_str) and int(input_str[start:start+2]) <= 32:
        # print(input_str[start:start+2], end=" ")
        double_num = get_possible_partition(start+2)
    
    return (single_num + double_num) & MOD



answer = get_possible_partition(0)
print(answer)

###################### 
# DP Tabulation 풀이
MOD = 10007

input_str = input()
# DP[i] = 문자열의 시작부터 i번째까지 해당하는 부분 문자열을 분할할 수 있는 가짓수
# 1. i번째 문제가 0이 아닌 경우 : D[i-1]의 분할 방법에 i번째 문자를 추가로 분할할 수 있기 때문에 D[i-1]가지 방법 모두 활용
# 2. i번째 문자를 합친 숫자가 10이상 32이하인 경우 : D[i-2]의 분할 방법에 i-1, i번째 문자를 추가로 분할할 수 있기 때문에 D[i-2]가지 방법 모두 사용가능

# D[i] = D[i-1] + D[i-2]
# D[i-1] : i번째 문자가 0아닌 경우
# D[i-2] : i-1, i번째 문자를 합친 숫자가 10이상 32이하인 경우

# DP 정의를 맞춰주기 위해서 input[0]에 dummy 문자를 넣어줍니다.
input_str = "#" + input_str

dp = [0] * len(input_str)

# 초기조건 1
# 0번째 자리까지 결정 가능한 서로 다른 가짓수는 1가지 
dp[0] = 1

# 초기조건2
# 한글자를 분할 가능하기 위해서는 0이 아니면 됨
if input_str == '0':
    dp[1] = 0
else:
    dp[1] = 1

for i in range(2, len(input_str)):
    print(dp)
    if input_str[i] != '0':
        dp[i] = (dp[i] + dp[i-1]) % MOD
    
    double_num = int(input_str[i-1:i+1])
    if 10 <= double_num <= 32:
        dp[i] = (dp[i] + dp[i-2]) % MOD
    

print(dp[len(input_str)-1])