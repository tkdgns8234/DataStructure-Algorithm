# 6.로봇청소기
# 성공! 너무 잘했다 ㅎ
# # 북 동 남 서
move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 현재 방향에서 왼쪽방향 반환
def re_direction(direction):
    return (direction-1) % 4
    # 북 동 남 서
    # if direction == 0:
    #     return 3
    # elif direction == 1:
    #     return 0
    # elif direction == 2:
    #     return 1
    # elif direction == 3:
    #     return 2


def clean(x, y, d, depth):
    global count
    # c
    if depth == 4:
        # 후진
        back_x, back_y = x-move_type[d][0], y-move_type[d][1]
        if data[back_x][back_y] == 1:
            print(count + 1)
            exit()
        clean(back_x, back_y, d, 0)

    # 1. 현재위치 청소
    visited[x][y] = 1
    # 2. 현재위치에서 현재 방향기준 왼쪽방향 탐색
    rd = re_direction(d)
    nx = x + move_type[rd][0]
    ny = y + move_type[rd][1]

    # a
    if point_validation(nx, ny):
        visited[nx][ny] = 1
        count += 1
        clean(nx, ny, rd, 0)
    # b
    else:
        clean(x, y, rd, depth + 1)

def point_validation(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if visited[x][y] == 1:
        return False
    if data[x][y] == 1:
        return False
    return True

n, m = map(int, input().split())
x, y, d = map(int, input().split())
# 빈칸:0 벽:1
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for i in range(n)]
count = 0
clean(x, y, d, 0)
print(count + 1)