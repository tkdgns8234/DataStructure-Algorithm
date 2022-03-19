# 가장 가까운 물고기, 같다면 가장 왼쪽, 위 --> 왼쪽 위를 먼저 탐색하도록 move
# 움직일 수 없는 부분도 있기때문에 미리 물고기 위치 계산하는건 안되고
# bfs 하면서 직접 움직여야한다.
# 나머지는 맞는거 같은데, 왼쪽 위 부터 탐색하는 방식 자체가 잘못됐어,,
# 최소, 동일 거리에 잡아먹을 수 있는 물고기 모두 담고 정렬하는식으로 풀어나가야하네


import sys
input = sys.stdin.readline
from collections import deque

def point_validator(nx, ny, shark_level, visited):
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return False
    if data[nx][ny] > shark_level or visited[nx][ny]:
        return False
    return True

move_type = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(x, y):
    ans = 0
    shark_level = 2
    eat = 0

    while True:
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        q = deque([(x, y, ans)])

        fish = []
        flag = int(1e9)
        while q:
            x, y, second = q.popleft()
            if second > flag:
                break
            for move in move_type:
                nx, ny = move[0] + x, move[1] + y
                if point_validator(nx, ny, shark_level, visited):
                    if data[nx][ny] < shark_level and data[nx][ny] != 0:
                        flag = second
                        fish.append((nx, ny, second+1))
                    visited[nx][ny] = True
                    q.append((nx, ny, second + 1))

        if len(fish):
            fish.sort()
            x, y, second = fish[0]
            data[x][y] = 0
            ans = second
            eat += 1
            if shark_level == eat:
                eat = 0
                shark_level += 1
        else:
            return ans

N = int(input())
data = []
shark = (0, 0)
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 9: # baby shark
            shark = (i, j)
            temp[j] = 0
    data.append(temp)
print(bfs(*shark))
