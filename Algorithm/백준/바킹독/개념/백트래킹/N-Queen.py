# 문제6 n-Queen
n = int(input())
cnt = 0

# y축 겹치는지
issue1 = [False] * 100
# 우측 위쪽 대각선 겹치는지
issue2 = [False] * 100
# 좌측 위쪽 대각선 겹치는지
issue3 = [False] * 100

def dfs(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(n):
        if issue1[i] or issue2[cur+i] or issue3[cur-i+n-1]:
            continue
        issue1[i] = True
        issue2[cur+i] = True
        issue3[cur-i+n-1] = True
        dfs(cur + 1)
        issue1[i] = False
        issue2[cur + i] = False
        issue3[cur - i + n - 1] = False

dfs(0)
print(cnt)