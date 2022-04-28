# 아니 풀이 자체는 매우 쉽다
# 어떻게 완전탐색이 가능한지 시간복잡도를 잘 생각해야해
# 20 * 20의 보드를 탐색해야해서 절대 안될거라 생각했는데
# 다른 사람의 분석글을 보니
# 완전탐색의 경우 4^26 이고, 중복으로 안가는 경우도 있어서  더 줄어든다고 한다
# 4방향으로 이동 가능하고, 26개의 단어가 존재하므로 최대 26번 움직일 수 있다.
# -> 사실 이거 최대의 경우 10조야;
# 물론 최악의 경우는 안나오겠지만


# bfs 형태로 풀이
def bfs(x, y):
    global ans
    q = set([(x, y, data[x][y])])

    while q:
        x, y, words = q.pop() # set은 없지만 현재 순서가 상관없음
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



R, C = map(int, input().split())

data = [list(str(input())) for _ in range(R)]

move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, depth):
    global ans
    ans = max(ans, depth)

    for move in move_type:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < R and 0 <= ny < C:
            if data[nx][ny] not in arr:
                arr.add(data[nx][ny])
                dfs(nx, ny, depth + 1)
                arr.remove(data[nx][ny])


ans = 0
arr = set()
arr.add(data[0][0])
dfs(0, 0, 1)
print(ans)



r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)