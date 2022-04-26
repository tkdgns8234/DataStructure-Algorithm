# 이미 푼 문제
# 해결 방법만 떠올리고 skip
# ---- 해결 방법 ----
# combination으로 시복 충분해보이는데
# -> 맞음
# ---- 해결 방법 ----

# 이전 풀이
# 더하는경우, 더하지 않는경우로 dfs 돌렷네
# 이것도 2^20으로 시복 만족
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def dfs(depth, sum):
    if depth == n:
        return 0
    if sum + arr[depth] == m:
        global cnt
        cnt += 1

    dfs(depth + 1, sum + arr[depth])
    dfs(depth + 1, sum)

dfs(0, 0)
print(cnt)