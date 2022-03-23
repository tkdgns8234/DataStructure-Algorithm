# 문제3 n 과 m (3)
n, m = map(int, input().split())

arr = []

def dfs(i):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

dfs(0)