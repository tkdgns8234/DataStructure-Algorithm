# 3. 토마토
# 문제의 키포인트 => 익은 토마토는 여러장소에 존재할 수 있음
# 처음 시작할 때 모든 익은 토마토의 위치를 큐에 넣으면 된다
# 그렇게 하지 않으면 시간복잡도가 n*m 이면 될게 (n*m) 제곱이 된다
# 그리고 구현도 힘들어진다.
# 시작할때부터 모두 익어있으면 0
# 토마토가 모두 익지는 못하는 상황이면 -1
from collections import deque
n, m, h = map(int, input().split())
data = [[[0] * m for i in range(n)] for _ in range(h)]

visited = [[[False] * m for i in range(n)] for _ in range(h)]
q = deque()

for k in range(h):
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            data[k][i][j] = tmp[j]
            if data[k][i][j] == 1:
                visited[k][i][j] = True
                q.append((k, i, j))

move_type =[(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
while q:
    z,x,y = q.popleft()
    for move in move_type:
        nz, nx, ny = z + move[0], x + move[1], y + move[2]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or nz < 0 or nz >= h:
            continue
        if not visited[nz][nx][ny] and data[nz][nx][ny] == 0:
            visited[nz][nx][ny] = True
            data[nz][nx][ny] = data[z][x][y] + 1
            q.append((nz,nx,ny))

result = 0
flag = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if data[k][i][j] == 0:
                flag = True
                break
            result = max(result, data[k][i][j])

if flag:
    print(-1)
else:
    print(result - 1)
