# 문제 3. 주사위 굴리기
# 풀어봤던 문제야,, 틀리지말자
# 주사위를 어떻게 처리할지 또 떠오르지 않았어,, 블로그 살짝 참고 다시풀이
# 주사위를 1차원배열로 표현

import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().rstrip().split())
data = [list(map(int, input().rstrip().split())) for i in range(n)]
sides = list(map(int, input().rstrip().split()))
# 1차원 배열로 주사위 표현
# 위, 북, 동, 서, 남, 아래
dice = [None] + [0 for i in range(6)]

move_type = [None, (0, 1), (0,-1), (-1, 0), (1,0)]

for side in sides:
    nx, ny = x+move_type[side][0], y+move_type[side][1]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    if side == 1: # 동
        dice[3],dice[1],dice[4],dice[6] = dice[1],dice[4],dice[6],dice[3]
    if side == 2:  # 서
        dice[4],dice[6],dice[3],dice[1] = dice[1],dice[4],dice[6],dice[3]
    if side == 3:  # 북
        dice[1],dice[2],dice[6],dice[5] = dice[5],dice[1],dice[2],dice[6]
    if side == 4:  # 남
        dice[2],dice[1],dice[5],dice[6] = dice[6],dice[2],dice[1],dice[5]

    # 이동한 칸에 쓰인 수가 0이면
    if data[nx][ny] == 0:
        data[nx][ny] = dice[6]
    else:
        dice[6] = data[nx][ny]
        data[nx][ny] = 0
    print(dice[1])
    x, y = nx, ny
