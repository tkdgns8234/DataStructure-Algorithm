# 8. 텀 프로젝트
# 실패 dfs 정말 어렵다.. 재귀형식
# import sys
# input = sys.stdin.readline
# def dfs(start, index, count):
#     global visited
#     if start != index and visited[index]:
#         return 0
#     if count != 0 and start == index:
#         return count
#     visited[index] = True
#     return dfs(start, data[index], count + 1)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     data = [None] + list(map(int, input().split()))
#     visited = [False] * (n + 1)
#     ans = 0
#
#     for i in range(1, len(data)):
#         if not visited[i]:
#             ans += dfs(i, i, 0)
#     print(ans)


# 아래는 참고한 dfs 소스
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(x):
    global ans
    vis[x] = True
    cycle.append(x)
    num = arr[x]

    if vis[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)
    print(n - len(ans))