# 문제5 n과 m (5)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = []

def dfs():
    if len(temp) == m:
        print(" ".join(map(str, temp)))
    for i in range(len(arr)):
        if arr[i] not in temp:
            temp.append(arr[i])
            dfs()
            temp.pop()
dfs()