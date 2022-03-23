# 문제 N과 M (1)
n, m = map(int, input().split())

arr = []

def dfs(i):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(0)