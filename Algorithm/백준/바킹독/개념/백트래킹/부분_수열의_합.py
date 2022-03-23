# 문제7 부분 수열의 합
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def dfs(depth, sum):
    if depth == n:
        return 0
    # 맨 처음이 0인경우는 없음 숫자를 일단 하나를 넣어야지..
    # 그래서 더한 경우 m 과 같은지 확인한다
    if sum + arr[depth] == m:
        global cnt
        cnt += 1
    # 해당 숫자를 포함한 경우와 포함하지 않은 두가지 가지치기
    dfs(depth + 1, sum + arr[depth])
    dfs(depth + 1, sum)

dfs(0, 0)
print(cnt)