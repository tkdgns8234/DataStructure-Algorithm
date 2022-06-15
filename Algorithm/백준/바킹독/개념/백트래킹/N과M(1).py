# # 문제 N과 M (1)
# n, m = map(int, input().split())
#
# arr = []
#
# def dfs(i):
#     if len(arr) == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(1, n + 1):
#         if i not in arr:
#             arr.append(i)
#             dfs(i)
#             arr.pop()
#
# dfs(0)


from itertools import permutations
n, m = map(int, input().split())
comb = sorted(permutations([i for i in range(1, n+1)], m))
for case in comb:
    print(*case, sep=" ")

def btk(depth):
    if depth == m:
        print(*arr, sep=" ")
        return

    for i in range(1, n+1):
        if visit[i]:
            continue

        visit[i] = True
        arr.append(i)
        btk(depth + 1)
        arr.pop()
        visit[i] = False

n, m = map(int, input().split())
visit = [False] * (n+1)
arr = []
btk(0)