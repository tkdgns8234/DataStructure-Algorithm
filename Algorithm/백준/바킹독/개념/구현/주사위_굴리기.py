# 문제 1. 주사위 굴리기
# 복잡하게 생각하면 끝도없이 복잡해지는 문제다.
# 키워드는 주사위를 1차원 배열공간에 임의로 설정 해 놓는것
# 방향: index   ex) 바닥: 0 동: 1 서: 2 ....

n, m, x, y, k = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

# 주사위 인덱스
# 바닥 동 서 남 북 윗면
# 0   1  2 3 4  5
j = [0 for i in range(6)]

# 동 서 남 북
move_type = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

# x,y 는 현재 지도상 위치
for move in moves:
    nx = x + move_type[move][0]
    ny = y + move_type[move][1]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    if move == 1: # 동쪽
        j[0], j[1], j[2], j[5] = j[1], j[5], j[0], j[2]
    elif move == 2: # 서쪽
        j[0], j[1], j[2], j[5] = j[2], j[0], j[5], j[1]
    elif move == 3: # 남쪽
        j[0], j[3], j[4], j[5] = j[3], j[5], j[0], j[4]
    elif move == 4: # 북쪽
        j[0], j[3], j[4], j[5] = j[4], j[0], j[5], j[3]

    if data[nx][ny] == 0:
        data[nx][ny] = j[0]
    else:
        j[0] = data[nx][ny]
        data[nx][ny] = 0

    x, y = nx, ny
    print(j[5])