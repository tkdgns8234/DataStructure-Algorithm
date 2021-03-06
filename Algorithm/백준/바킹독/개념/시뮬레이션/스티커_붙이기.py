# 문제2 스티커 붙이기
# 아래는 그냥 runtime 에실행해보면 다 잘 되는데
# 백준에서 수행시 시간초과
# 다시풀자
import copy
import sys
input = sys.stdin.readline
# 스티커 회전
def rotation(sticker, x, y):
    # 직사각형인 경우 x, y 크기 교체 필요
    temp = [[0] * x for _ in range(y)]
    s_position = []
    # 회전
    for i in range(x):
        for j in range(y):
            temp[j][x - i - 1] = sticker[i][j]
            if sticker[i][j] == 1:
                # 회전된 포지션 저장
                s_position.append((j, x - i - 1))

    return temp, s_position


def attach(sticker_position, startx, starty):
    temp = copy.deepcopy(note)
    result = True
    for s in sticker_position:
        nx = startx + s[0]
        ny = starty + s[1]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            result = False
            break
        if temp[nx][ny] == 1:
            result = False
            break
        # 조건을 모두 만족 하면 스티커 부분 대입
        temp[nx][ny] = 1

    return temp, result


n, m, k = map(int, input().split())
note = [[0] * m for i in range(n)]

for _ in range(k):
    sticker = []
    sticker_position = []
    sx, sy = map(int, input().split())
    for i in range(sx):
        data = list(map(int, input().split()))
        sticker.append(data)
        for j in range(len(data)):
            if data[j] == 1:
                # 스티커 좌표 더하기
                sticker_position.append((i, j))

    rotation_cnt = 0
    attached = False
    while not attached:
        if rotation_cnt == 4:
            break
        for i in range(n):
            for j in range(m):
                # 해당 칸에 붙이기
                rs_arr, attached = attach(sticker_position, i, j)
                # 붙인 경우 멈추기
                if attached:
                    break
            if attached:
                break

        if not attached:
            sticker, sticker_position = rotation(sticker, sx, sy)
            sx = len(sticker)
            sy = len(sticker[0])
            rotation_cnt += 1
        else:
            note = copy.deepcopy(rs_arr)
            break

# 스티커 붙은 칸의 수 출력
cnt = 0
for i in range(n):
    cnt += note[i].count(1)
print(cnt)

# 다시풀기
# 문제2 스티커 붙이기
# 키포인트
# 1 도형 회전 (직사각형까지 고려)
# 2 스티커를 붙일 수 있는지 확인하는 방법
# 3 스티커 크기가 계속 변하기때문에 스티커 크기를 구할 땐 항상 해당 배열의 크기를 직접 구하기

def rotation(sticker):
    x = len(sticker)
    y = len(sticker[0])

    temp = [[0] * x for _ in range(y)]  # 직사각형인 경우 x, y 크기 교체 필요
    for i in range(x):
        for j in range(y):
            temp[j][x - i - 1] = sticker[i][j]
    return temp


def check(start_x, start_y):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if note[start_x + i][start_y + j] + sticker[i][j] > 1:
                return False
    return True


def attach(start_x, start_y):
    global note
    # 스티커 붙이기
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                note[start_x + i][start_y + j] = sticker[i][j]


n, m, k = map(int, input().split())
note = [[0] * m for i in range(n)]

for _ in range(k):
    sticker = []
    sx, sy = map(int, input().split())
    for i in range(sx):
        sticker.append(list(map(int, input().split())))

    rotation_cnt = 0
    chk = False
    while rotation_cnt < 4:
        # 붙일 수 있는지 확인
        for i in range(n - len(sticker) + 1):
            for j in range(m - len(sticker[0]) + 1):
                if check(i, j):
                    attach(i, j)
                    chk = True
                    break
            if chk:
                break
        if chk:
            break
        else:
            rotation_cnt += 1
            sticker = rotation(sticker)

# 스티커 붙은 칸의 수 출력
cnt = 0
for i in range(n):
    cnt += note[i].count(1)
print(cnt)