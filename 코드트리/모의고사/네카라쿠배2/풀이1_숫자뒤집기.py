# 1, 2번같은 문제는 라이브코딩에서 나오는 난이도

##### 1. 문자열 풀이
# 거꾸로 for문돌면서 0이 아닌 순간 최초로 잡아서 출력
# 남은 부분은 쭉 print 하면됨 


##### 2. for문으로 수학적으로 풀기
num = int(input())

answer = 0
# 0을 없애주는 효과가 있음
while num > 0:
    # 나머지를 통해 거꾸로 출력
    answer = answer * 10 + num % 10
    num //= 10

print(answer)
