# 1. N과 M (1)
# n, m = map(int, input().split())
# data = [i for i in range(1, n + 1)]
# visited = [False] * (n+1)
# arr = []
#
# def btk(depth):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in data:
#         if not visited[i]:
#             visited[i] = True
#             arr.append(i)
#             btk(depth + 1)
#             arr.pop()
#             visited[i] = False
#
# btk(0)

# 2. n 과 m 2
# n, m = map(int, input().split())
# data = [i for i in range(1, n + 1)]
# arr = []
#
# def btk(depth, start):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(start, len(data)):
#         v = data[i]
#         if v not in arr:
#             arr.append(v)
#             btk(depth + 1, v)
#             arr.pop()
#
# btk(0, 0)

# 3. n 과 m 3
# n, m = map(int, input().split())
# data = [i for i in range(1, n+1)]
# arr = []
#
# def btk(depth):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in data:
#         arr.append(i)
#         btk(depth + 1)
#         arr.pop()
#
# btk(0)

# 4. n 과 m 4
# n, m = map(int, input().split())
# data = [i for i in range(1, n+1)]
# arr = []
#
# def btk(depth, start):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(start, n + 1):
#         arr.append(i)
#         btk(depth + 1, i)
#         arr.pop()
#
# btk(0, 1)

# 5. n 과 m 5
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
#
# def btk(depth):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in data:
#         if i not in arr:
#             arr.append(i)
#             btk(depth + 1)
#             arr.pop()
#
# btk(0)

# 6. n 과 m 6
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
#
# def btk(depth, start):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#
#     for i in range(start, n):
#         v = data[i]
#         if v not in arr:
#             arr.append(v)
#             btk(depth + 1, i)
#             arr.pop()
#
# btk(0, 0)

# 7. n과 m 7
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
#
# def btk(depth):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#
#     for i in data:
#         arr.append(i)
#         btk(depth + 1)
#         arr.pop()
#
# btk(0)

#8 n 과 m 8
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
#
# def btk(depth, start):
#     if depth == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(start, len(data)):
#         v = data[i]
#         arr.append(v)
#         btk(depth + 1, i)
#         arr.pop()
#
# btk(0, 0)

#9 n 과 m 9
# 아래 코드는 블로그 참조, 다시풀기
# N, M = map(int, input().split())
# L = list(map(int, input().split()))
#
# L.sort()
# visited = [False] * N
# out = []
#
# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     overlap = 0
#     for i in range(N):
#         if not visited[i] and overlap != L[i]:
#             visited[i] = True
#             out.append(L[i])
#             overlap = L[i]
#             solve(depth+1, N, M)
#             visited[i] = False
#             out.pop()
#
# solve(0, N, M)

# 10. n 과 m 10
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
# visited = [False] * n
#
# def btk(depth, start):
#     if depth == m:
#         print(' '.join(map(str, arr)))
#         return
#     before_val = -1
#     for i in range(start, n):
#         if not visited[i] and before_val != data[i]:
#             visited[i] = True
#             arr.append(data[i])
#             before_val = data[i]
#             btk(depth + 1, i)
#             arr.pop()
#             visited[i] = False
# btk(0, 0)

# 11. n 과 m 11
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# arr = []
#
# def btk(depth):
#     if depth == m:
#         print(' '.join(map(str, arr)))
#         return
#     before_val = -1
#     for i in range(n):
#         if before_val != data[i]:
#             arr.append(data[i])
#             before_val = data[i]
#             btk(depth + 1)
#             arr.pop()
# btk(0)


# 12 로또
# import sys
# input = sys.stdin.readline
#
# def btk(depth, start):
#     if depth == 6:
#         print(' '.join(map(str, arr)))
#         return
#     for i in range(start, data[0] + 1):
#         if not visited[i]:
#             visited[i] = True
#             arr.append(data[i])
#             btk(depth + 1, i)
#             arr.pop()
#             visited[i] = False
#
# while True:
#     data = list(map(int, input().split()))
#     if len(data) == 1:
#         break
#     arr = []
#     visited = [False] * (data[0] + 1)
#     btk(0, 1)
#     print()

# 13. 소문난 칠공주
# 그저 백트래킹으로만 구현하는것은 불가능하네.
# 문제 힌트에 두번째를 보면
# 3,1 위치까지 갔다가 돌아오는것을 어떻게 계산하리까..
# 십자가 모양을 dfs 또는 bfs 로 구현할 수 없네
# 모든 조합을 구하는 방법이 맞아보인다
# 아래는 틀린 방법 다시 해보자

# test = []
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def btk(depth, x, y):
#     global count
#     if depth == 7:
#         count += 1
#         return
#     for move in move_type:
#         nx, ny = move[0] + x, move[1] + y
#         if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
#             continue
#         if princess.count('Y') == 3 and data[nx][ny] == 'Y':
#             continue
#         if not visited[nx][ny]:
#             visited[nx][ny] = True
#             test.append((nx, ny))
#             princess.append(data[nx][ny])
#             btk(depth + 1, nx, ny)
#             princess.pop()
#             test.pop()
#             visited[nx][ny] = False
#
#
#
# data = []
# for _ in range(5):
#     data.append(list(input()))
# visited = [[False] * 5 for _ in range(5)]
#
# princess = []
# count = 0
# for i in range(5):
#     for j in range(5):
#         visited[i][j] = True
#         princess.append(data[i][j])
#         btk(1, i, j)
#         visited[i][j] = False
#         princess.pop()
# print(count)


# 조합 라이브러리를 사용하면 훨씬 쉬울거같은데 dfs로 조합을 찾는게 아니라
# from sys import stdin
#
# input = stdin.readline
#
# dr = (-1, 1, 0, 0)
# dc = (0, 0, -1, 1)
#
#
# def check(num):
#     global available
#     r = num // 5
#     c = num % 5
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
#             continue
#         nextNum = nr * 5 + nc  # 다음 숫자
#         if nextNum in p:  # p에 있다면 방문표시, 재귀로 다음 숫자 넘겨 재검사
#             visited[nr][nc] = 1
#             available += 1
#             check(nextNum)
#
#
# # (depth, Y의 갯수, 사용할 숫자 인덱스)
# def dfs(depth, ycnt, idx):
#     global result, available, visited
#     if ycnt > 3 or 25 - idx < 7 - depth:  # 가지치기
#         return
#
#     if depth == 7:  # depth가 7에 도달하면 연결 여부 검사
#         available = 1  # 연결된 좌표 갯수
#         visited = [[0] * 5 for _ in range(5)]
#         sr, sc = p[0] // 5, p[0] % 5  # 5*5 맵 좌표로 변환
#         visited[sr][sc] = 1  # 시작 위치 표시
#         check(p[0])  # 연결된 좌표인지 확인
#         if available == 7:  # 7개 좌표가 연결됐다면 +1
#             result += 1
#         return
#
#     # 5*5 맵 좌표로 변환
#     r = idx // 5
#     c = idx % 5
#
#     if A[r][c] == "Y":  # "Y"이면 ycnt +1
#         p.append(idx)
#         dfs(depth + 1, ycnt + 1, idx + 1)
#         p.pop()
#     else:  # "S"이면 그냥 넘기기
#         p.append(idx)
#         dfs(depth + 1, ycnt, idx + 1)
#         p.pop()
#     dfs(depth, ycnt, idx + 1)  # 꼭 필요한 코드. 사용하지 않고, 그냥 인덱스만 넘긴다!
#
#
# # main
# A = [input().rstrip() for _ in range(5)]
# result = 0
# p = []
# dfs(0, 0, 0)
# print(result)


# 모든 경우의수를 itertools 를 이용해 짜보자
# 성공!
# 백트래킹 연습해야하니, 백트래킹을 이용해서도 시도해보자

# from collections import deque
# from itertools import combinations
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# data = [input() for i in range(5)]
# comb = list(combinations([i for i in range(25)], 7))

# def bfs():
#     global rs
#     for c in comb:
#         y_count = 0
#         for i in range(len(c)):
#             val = c[i]
#             x, y = val//5, val % 5
#             if data[x][y] == 'Y':
#                 y_count += 1
#         if y_count > 3:
#             continue

#         visited = [[False] * 5 for _ in range(5)]
#         start = c[0]
#         x, y = start // 5, start % 5
#         q = deque()
#         q.append((x, y))
#         visited[x][y] = True
#         count = 1

#         while q:
#             x, y = q.popleft()
#             if count == 7:
#                 rs += 1
#                 break
#             for move in move_type:
#                 nx, ny = x+move[0], y+move[1]
#                 if not (0 <= nx < 5 and 0 <= ny < 5) or visited[nx][ny]:
#                     continue
#                 if nx*5+ny in c:
#                     count += 1
#                     q.append((nx, ny))
#                     visited[nx][ny] = True

# rs = 0
# bfs()
# print(rs)

# 백트래킹 이용 소문난 칠공주
# 모든 조합을 구한 뒤
# 구한 조합이 1. Y 갯수가 4개이상인지 <- 조건걸었음
# 2. 모두 붙어있는지 확인 만 하면 됨
# -> bfs 로 하자
# 성공
#
# import sys
# input = sys.stdin.readline
# from collections import deque
# move_type = [(-1, 0), (1, 0),(0, 1),(0, -1)]
#
# def bfs():
#     visited = [[False] * 5 for i in range(5)]
#     index = arr[0]
#     x, y = index//5, index % 5
#     q = deque()
#     q.append((x, y))
#     count = 1
#     visited[x][y] = True
#     while q:
#         x, y = q.popleft()
#         for move in move_type:
#             nx, ny = x + move[0], y + move[1]
#             if not (0 <= nx < 5 and 0 <= ny < 5) or visited[nx][ny]:
#                 continue
#             if nx*5+ny in arr:
#                 visited[nx][ny] = True
#                 q.append((nx,ny))
#                 count += 1
#
#     if count == 7:
#         return True
#     else:
#         return False
#
#
# def btk(depth, y_count, index):
#     global result
#     if y_count > 3 or 25 - index < 7 - depth: # 이게 왜 24가 아니라 25지? 아 아직 arr에 아무것도 안들어온상태구나 0이어도 depth 도 마찬가지
#         return
#     if depth == 7: # 모두 붙어있는지 확인
#         if bfs():
#             result += 1
#         return
#
#     x = index // 5
#     y = index % 5
#
#     if data[x][y] == 'Y':
#         arr.append(index)
#         btk(depth + 1, y_count + 1, index + 1)
#         arr.pop()
#     else:
#         arr.append(index)
#         btk(depth + 1, y_count, index + 1)
#         arr.pop()
#     btk(depth, y_count, index + 1)
#
#
#
# data = [input().rstrip() for i in range(5)]
# arr = [] # index 대입
# result = 0
# btk(0, 0, 0)
# print(result)

# 14. 계란으로 계란치기
# 푸는데 시간이 걸렸지만 스스로 해냈다
# 너무 잘했다 ^_^ 시간복잡도도 잘 나와
# import sys
# input = sys.stdin.readline
# def btk(depth, arr):
#     global max_val
#     if depth == n:
#         c = 0
#         for i in range(n):
#             if arr[i][0] <= 0:
#                 c += 1
#         max_val = max(c, max_val)
#         return
#
#     armor, weight = arr[depth][0], arr[depth][1]
#     if armor < 0:
#         btk(depth + 1, arr)  # 집은 계란이 꺠졌으면 다음 계란으로 넘어간다
#         return
#
#     hit = False
#     for i in range(n):
#         if i == depth or arr[i][0] <= 0:
#             continue  # 자기 자신은 치지 않는다, 타겟의 내구도가 0 보다 크면
#         hit = True
#         armor_i, weight_i = arr[i][0], arr[i][1]
#         # 치기
#         arr[depth][0] = armor - weight_i
#         arr[i][0] = armor_i - weight
#         btk(depth + 1, arr)
#         # 복구
#         arr[depth][0] = armor
#         arr[i][0] = armor_i
#
#     if not hit: #나머지가 다 깨졌으면 치지 않고 넘어간다
#         btk(depth + 1, arr)
#
#
# n = int(input())
# data = []  # 내구도 / 무게
# for _ in range(n):
#     temp = list(map(int, input().rstrip().split()))
#     data.append([temp[0], temp[1]])
#
# max_val = 0
# btk(0, data)
# print(max_val)