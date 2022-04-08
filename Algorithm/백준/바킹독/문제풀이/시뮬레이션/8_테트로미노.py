# 7. 테트로미노
# ㅗ 모양 제외하고 나머지 모든 모양은 dfs로 4 칸 이동했을때의 모양이다
# 각 모든지점에서 dfs를 4번 수행하고 최댓값을 구한 후
# ㅗ 모양에대해서는 따로 처리한다 => rotate 함수 필요해보임
# 배치를 어떻게해야할지 감이안오는데?
# 해당 문제를 2가지 방식으로 풀자
# 1. ㅗ 스티커를 직접 붙이는걸 하나 추가한 방식
# 2. dfs에서 모든걸 해결하는 방식

# 1. ㅗ 스티커 하나 붙이는 방식
# dfs 4개 수행 후 (당연히 모든 시작점에서 해야겠지)
# 스티커를 붙이는 경우와 dfs 돌리는경우 두가지 모두 학습했다 성공
# 2번방식으로 다시풀자
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# ans = 0
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def dfs(x, y, depth, total):
#     global ans
#     if depth == 3:
#         ans = max(ans, total)
#         return
#
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             dfs(nx, ny, depth + 1, total + data[nx][ny])
#             visited[nx][ny] = 0
#
#
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = 1
#         dfs(i, j, 0, data[i][j])
#         visited[i][j] = 0
#
# # ㅗ 에대한 처리
# # 스티커 붙이기 형식
# def attatch(x, y, arr):
#     total = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j] == 1:
#                 total += data[x+i][y+j]
#     return total
#
# def rotation(arr):
#     temp = [[0] * len(arr) for _ in range(len(arr[0]))]
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             temp[j][len(arr)-i-1] = arr[i][j]
#     return temp
#
# sticker = [[0, 1, 0], [1, 1, 1]]
# count = 0
# while count < 4:
#     count += 1
#     sticker = rotation(sticker)
#     for i in range(n-len(sticker)+1):
#         for j in range(m-len(sticker[0])+1):
#             ans = max(ans, attatch(i, j, sticker))
#
# print(ans)

# 테트로미노 2. dfs에서 모든걸 해결하는 방식
# 최적화까지 생각하자 오래걸리는듯 싶다
# 시간복잡도: O nm * 4^5
# 공간복잡도: Onm
# dfs 백트래킹 돌릴 때 최적화 (가지치기가 정말 중요하다)
#
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for i in range(n)]
# ans = 0
#
# move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# def dfs(depth, x, y, total):
#     global ans
#     # 가지치기 하면 시간이 극적으로 줄어들어! 1000ms -> 200ms 까지 줄어듬
#     if ans >= total + (max_val * (3-depth)):
#         return
#     if depth == 3:
#         ans = max(ans, total)
#         return
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m :
#             continue
#         if not visited[nx][ny]:
#             if depth == 1:
#                 # 다음 위치를 간것처럼 처리 후 현재 좌표 그대로 이동
#                 visited[nx][ny] = True
#                 dfs(depth + 1, x, y, data[nx][ny] + total)
#                 visited[nx][ny] = False
#             visited[nx][ny] = True
#             dfs(depth + 1, nx, ny, data[nx][ny]+total)
#             visited[nx][ny] = False
#
# max_val = max(map(max, data))
# for i in range(n):
#     for j in range(m):
#         visited[i][j] = True
#         dfs(0, i, j, data[i][j])
#         visited[i][j] = False
#
# print(ans)
