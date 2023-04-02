# 식의 결과를 최대로
s = input()
alpha = []




def calc():
    stack = []
    num = 0
    idx = 0
    for x in range(len(s)):
        if s[x].isalpha():
            idx = ord(s[x]) - ord('a')
            if x == 0:
                num = alpha[idx]

            else:
                p = stack.pop()
                num2 = int(alpha[idx])
                if p == "+":
                    num += num2
                elif p == "-":
                    num -= num2
                else:
                    num *= num2

        else:
            stack.append(s[x])


    return num 



ans = 0
def choose(cnt):
    global ans
    if cnt == 6:
        ans = max(ans, calc())
        return
    
    for i in range(1, 5):
        alpha.append(i)
        choose(cnt+1)
        alpha.pop()


choose(0)

print(ans)