# 문제를 좀 더 자세히 읽었더라면 힌트를 얻었을 지도 모른다.
# 내부의 공기를 처리할 방법이 떠오르지 않아 블로그를 참조하였다.
# h
# 이것도 bfs의 특성을 이해하고 잘 활용하는 문제다

# 문제를 잘 보면 모눈종이의 맨 가장자리에는 치즈를 놓지 않는다고 하였다.
# 이를통해 가장자리에서부터 무언가 해 볼 수 있다는 이야기인데
# 가장자리부터 bfs를 돌려, 치즈가 아닌 공간을 -1 로 만든다.
# 물론 치즈인 공간은 큐에 넣지 않아야 한다. 이렇게 되면 치즈 사이에 있는 공간은
# -1 로 변하지 않고 외부 공간만 -1 로 변하게 된다.

# 로직
# 1. 외부 공간을 -1 로 만드는 bfs 1개 생성
# 2. 각 면이 -1 두개이상과 마주하는 치즈를 녹이는 main 로직 생성
# 3. 모두 녹았는지 확인하는 로직 생성

# bfs로 가장자리 확인하는법: 0을 만나면 큐에 넣고 1을 만나면 가장자리를 의미하는 숫자로 설정
# 가장자리는 q에 넣지 않는다. (현재 문제와 유사한 2326 문제 참조)

from collections import deque

move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def out_side():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and paper[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    paper[nx][ny] = -1 # 외부의 공기는 -1 로 만든다.

def check():
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1: # 치즈가 존재함
                return True
    return False

#세로, 가로
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while check():
    out_side()
    melt = []
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:
                count = 0
                for move in move_type:
                    ni, nj = move[0] + i, move[1] + j
                    if 0 <= ni < N and 0 <= nj < M:
                        if paper[ni][nj] == -1:
                            count += 1
                if count >= 2:
                    melt.append((i, j))
    for a, b in melt:
        paper[a][b] = 0
    ans += 1

print(ans)