# 문제 5 아기 상어
# 와,, 이거 bfs 특성을 잘 이해하고 있으면 좀 더 간단하게 풀 수 있어
# 어려워서 문제 푸는 중 블로그를 한 번 봤다.
# 계속 참고하면서 했어.. 연습 계속 해야겠다
# flag 를 통해 물고기를 찾은 경우, 찾은 시간까지는 탐색을 모두 완료시켜서
# 물고기를 전부 담고, 문제에서 요구하는 물고기 먼저먹는 순서대로 먹은 후 다시 bfs를 돌리는 형식
# 그리고 bfs 할 때 함수 말고 while 문으로 바로 돌리는게 코드가 더 깔끔하다

from collections import deque
def bfs(start, space):
    # 최단거리의 먹이 위치 찾고 먹으면서 초 세기, 상어 크기 키우기
    sx, sy = start
    shark_size = 2
    eat = 0
    move_num = 0

    while True:
        q = deque()
        q.append((sx, sy, 0))
        visited = [[False] * n for _ in range(n)]
        visited[sx][sy] = True
        flag = int(1e9)
        fish = []
        while q:
            x, y, second = q.popleft()
            if second > flag:
                break
            for move in move_type:
                nx, ny = x + move[0], y + move[1]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if shark_size < space[nx][ny] or visited[nx][ny]:
                    continue

                if shark_size > space[nx][ny] != 0:
                    flag = second
                    fish.append((nx, ny, second + 1))
                q.append((nx, ny, second + 1))
                visited[nx][ny] = True

        if len(fish) > 0:
            fish.sort()
            x, y, second = fish[0]
            move_num += second
            eat += 1
            space[x][y] = 0
            if eat == shark_size:
                shark_size += 1
                eat = 0
            sx, sy = x, y
        else:
            print(move_num)
            break

n = int(input())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            start = (i, j)

move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bfs(start, space)