def solve(n, t, m):
    num = 0
    rs = ''
    while len(rs) < t*m:
        a = num
        temp = ''
        while True:
            a, b = divmod(a, n)
            if b >= 10:
                b = chr(55+b)
            temp = str(b) + temp
            if a == 0:
                rs += temp
                break
        num += 1
    return rs


def solution(n, t, m, p):
    answer = ''
    rs = solve(n, t, m)
    for i in range(p-1, t*m, m):
        answer += rs[i]
    return answer

print(solution(16, 16, 2, 2))

# print(ord('A')) 65