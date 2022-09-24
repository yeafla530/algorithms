def solution(n, m, x, y, r, c, k):
    y, x = x, y
    dh = y-r
    dw = x-c
    d = abs(dh)+abs(dw)
    if (d-1) % 2 == k % 2 or d > k:
        return 'impossible'
    ans = list()
    cur_y = y
    cur_x = x

    while d != k:
        if cur_y < n:
            ans.append('d')
            cur_y += 1
        elif cur_x > 1:
            ans.append('l')
            cur_x -= 1
        elif cur_x < m:
            ans.append('r')
            cur_x += 1
        elif cur_y < 1:
            ans.append('u')
            cur_y -= 1
        dh = cur_y-r
        dw = cur_x-c
        d = abs(dh)+abs(dw)
        k -= 1

    while k > 0:
        if cur_y < r:
            ans.append('d')
            cur_y += 1
        elif cur_x > c:
            ans.append('l')
            cur_x -= 1
        elif cur_x < c:
            ans.append('r')
            cur_x += 1
        elif cur_y > r:
            ans.append('u')
            cur_y -= 1
        k -= 1
    return ''.join(ans)


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))