# 최대, 최소를 만족하면서 이동할 수 있는 경우를 구함
# bfs로 이동
# bfs 중복처리가 애매하네
# TC는 다 맞는데 실패;

# from collections import deque
#
#
# def bfs(diff):
#     visited = [[0] * N for _ in range(N)]
#     q = deque([[0, board[0][0], board[0][0], 0, 0]])
#     visited[0][0] = 4
#     while q:
#         max_diff, min_val, max_val, x, y = q.popleft()
#         if x == N-1 and y == N-1:
#             return True
#         min_val, max_val = min(min_val, board[x][y]), max(max_val, board[x][y])
#
#         for move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#             nx, ny = x+move[0], y+move[1]
#             if 0<=nx<N and 0<=ny<N and visited[nx][ny] < 4:
#                 if max_val - board[nx][ny] <= diff and board[nx][ny] - min_val <= diff:
#                     visited[nx][ny] += 1
#                     n_min_val, n_max_val = min(min_val, board[nx][ny]), max(max_val, board[nx][ny])
#                     n_max_diff = max(n_max_val-n_min_val, max_diff)
#                     q.append([n_max_diff, n_min_val, n_max_val, nx, ny])
#     return False
#
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# ans = int(1e9)
# l, r = 0, 200
# while l <= r:
#     mid = (l+r)//2
#     if mid == 2 or mid == 4:
#         pass
#     rs = bfs(mid)
#
#     if rs:
#         ans = min(ans, mid)
#         r = mid - 1
#     else:
#         l = mid + 1
#
# print(ans)

# 개선 (실패)
# !!!! visit 처리를 최솟값을 기준으로 한다  <- 왜 최솟값 기준일까 diff 기준이어도 될거같은데
# 시간초과 발생
# import heapq
# from collections import deque
#
# def bfs(diff):
#     visited = [[[False] * 201 for _ in range(N)] for _ in range(N)]
#     q = []
#     heapq.heappush(q, [0, board[0][0], board[0][0], 0, 0])
#     visited[0][0][0] = True
#     while q:
#         max_diff, min_val, max_val, x, y = heapq.heappop(q)
#         if x == N-1 and y == N-1:
#             return True
#
#         for move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#             nx, ny = x+move[0], y+move[1]
#
#             if 0<=nx<N and 0<=ny<N:
#                 n_min_val, n_max_val = min(min_val, board[nx][ny]), max(max_val, board[nx][ny])
#                 n_diff = n_max_val-n_min_val
#                 if not visited[nx][ny][n_min_val]:
#                     if n_diff <= diff:
#                         visited[nx][ny][n_min_val] = True
#                         heapq.heappush(q, [n_diff, n_min_val, n_max_val, nx, ny])
#     return False
#
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# ans = 200
# l, r = 0, 200
# while l <= r:
#     mid = (l+r)//2
#     if mid <= 7:
#         pass
#     rs = bfs(mid)
#
#     if rs:
#         ans = min(ans, mid)
#         r = mid - 1
#     else:
#         l = mid + 1
#
# print(ans)


# 정답 코드
# 시간효율은 떨어지지만 내가 짜려는 방식과 유사한 코드
# heap의 성질을 이용해서 가장 diff가 짧은곳을 먼저 방문하도록
# 방문처리가 좀 애매하긴 하다 일단, 최솟값, 최댓값 둘 중 하나로 설정하면 통과 된다.
#
# import sys, heapq
# n = int(sys.stdin.readline())
# table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# check = [[[False] * 201 for _ in range(n)]for _ in range(n)]
# def bfs():
#     q = []
#     heapq.heappush(q, (0, table[0][0], table[0][0], 0, 0))
#     while q:
#         diff, temp_max, temp_min, x, y = heapq.heappop(q)
#         if x == n - 1 and y == n - 1:
#             return diff
#         if check[x][y][temp_min]:
#             continue
#         check[x][y][temp_min] = True
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 new_max = max(temp_max, table[nx][ny])
#                 new_min = min(temp_min, table[nx][ny])
#                 if check[nx][ny][temp_min] == False:
#                     heapq.heappush(q, (new_max - new_min, new_max, new_min, nx, ny))
#
# print(bfs())


# 정답 코드
# from collections import deque


# def bfs(m):
#     for k in range(mn, mx - m + 1):
#         clear()
#         makeMap(k, m)
#         if vis[0][0] == 1 or vis[n - 1][n - 1] == 1:
#             continue
#         q = deque([[0, 0]])
#         while q:
#             x, y = q.popleft()
#             if x == n - 1 and y == n - 1:
#                 return True
#             for p in range(4):
#                 xi, yi = x + dx[p], y + dy[p]
#                 if 0 <= xi < n and 0 <= yi < n and vis[xi][yi] == 0:
#                     vis[xi][yi] = 1
#                     q.append([xi, yi])
#     return False
#
#
# def clear():
#     for x in range(n):
#         for y in range(n):
#             vis[x][y] = 0
#
#
# def makeMap(k, m):
#     for x in range(n):
#         for y in range(n):
#             if arr[x][y] < k:
#                 vis[x][y] = 1
#             elif k <= arr[x][y] <= k + m:
#                 vis[x][y] = 0
#             else:
#                 vis[x][y] = 1
#
#
# n = int(input())
# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# vis = [[0] * n for i in range(n)]
# arr = [list(map(int, input().split())) for _ in range(n)]
# mx = 0
# mn = 200
# for i in range(n):
#     for j in range(n):
#         t = arr[i][j]
#         mx = max(t, mx)
#         mn = min(t, mn)
#
# l, r = 0, mx - mn
# while l <= r:
#     m = (l + r) // 2
#     if bfs(m):
#         r = m - 1
#     else:
#         l = m + 1
# print(l)


# 재풀이
# 힙 이용 풀이, 투 포인터 풀이, 이진탐색 풀이


# 이진탐색 풀이
# -> 사실 이건 시간복잡도를 통과할지 계산도 정확히 안됨
# log(200)*N^2 * ?
# ? 는 모든 특정범위

from collections import deque


def bfs(start, end):
    if not start <= data[0][0] <= end:
        return

    check = [[False]*N for _ in range(N)]
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return True
        for move in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            nx, ny = move[0]+x,move[1]+y
            if 0<=nx<N and 0<=ny<N and not check[nx][ny]:
                if start<=data[nx][ny]<=end:
                    check[nx][ny] = True
                    q.append((nx, ny))
    return False

N = int(input())
data = []
mx, mn = 0, 200
for _ in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)
    for j in temp:
        mx = max(mx, j)
        mn = min(mn, j)

ans = 200
start, end = 0, mx
while start <= end:
    mid = (start+end)//2
    for i in range(0, mx+1):
        rs = bfs(i, i+mid)
        if rs:
            break

    if rs:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1
print(ans)




# 투 포인터 풀이
# 이게 시간복잡도 계산, 직관적인 문제 풀이 면에서 훨씬 좋은 풀이방법같다
# 시복: 범위를 투포인터로 탐색(N) * bfs(N^2)  => N^3
from collections import deque

def bfs(start, end):
    if not start <= data[0][0] <= end:
        return False
    visited = [[False]*N for _ in range(N)]
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return True
        for move in [(-1, 0), (1, 0), (0, 1), (0 ,-1)]:
            nx, ny = move[0]+x, move[1]+y
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if start <= data[nx][ny] <= end:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
r = 0
for l in range(201):
    while r <= 200:
        if bfs(l, r):
            ans = min(ans, r-l)
            break
        else:
            r += 1

print(ans)




# 투포인터 다른 방식
from collections import deque

def bfs(start, end):
    if not start <= data[0][0] <= end:
        return False
    visited = [[False]*N for _ in range(N)]
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return True
        for move in [(-1, 0), (1, 0), (0, 1), (0 ,-1)]:
            nx, ny = move[0]+x, move[1]+y
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if start <= data[nx][ny] <= end:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
l, r = 0, 0
while l <= 200 and r <= 200:
    if bfs(l, r):
        ans = min(ans, r-l)
        l += 1
    else:
        r += 1

print(ans)
