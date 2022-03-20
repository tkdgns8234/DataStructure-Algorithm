# dfs, bfs 형태 이지만 백트래킹 문제

# dfs는 시간초과떄문에 고생했었다  arr.add(data[nx][ny]), remove 위치 떄문

# R, C = map(int, input().split())
# data = [list(str(input())) for _ in range(R)]
# move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
# def dfs(x, y, depth):
#     global ans
#     ans = max(ans, depth)
#     for move in move_type:
#         nx, ny = x + move[0], y + move[1]
#         if 0 <= nx < R and 0 <= ny < C:
#             if data[nx][ny] not in arr:
#                 arr.add(data[nx][ny])
#                 dfs(nx, ny, depth + 1)
#                 arr.remove(data[nx][ny])
#
#
# ans = 0
# arr = set()
# arr.add(data[0][0])
# dfs(0, 0, 1)
# print(ans)


# 처음엔 아래 코드의 set 대신 deque 를 사용했는데 메모리 초과가 발생했다.

# bfs 형태로 풀이
def bfs(x, y):
    global ans
    q = set([(x, y, data[x][y])])

    while q:
        x, y, words = q.pop() # set은 순서가 없지만 순서가 상관없음
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] not in words:
                q.add((nx, ny, words + data[nx][ny]))
                ans = max(ans, len(words) + 1)


ans = 1
R, C = map(int, input().split())
data = [list(str(input())) for _ in range(R)]
move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bfs(0, 0)
print(ans)
