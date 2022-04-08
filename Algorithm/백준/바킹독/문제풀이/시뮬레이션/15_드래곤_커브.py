# 14. 드래곤 커브
# 1. 시작점
# 2. 시작방향
# 3. 세대
# 1. 시작점에서 시작 방향으로 선분1을 긋는다
# 다음 세대는 오른쪽으로 90도 회전한것을 꼭지점에 붙인 것
# 이전 꼭지점과 회전 후 꼭지점 위치를 맞추면 드래곤커브를 붙일 수 있다.
# 결과: 모든 꼭지점이 드래곤 커브인것의 갯수
# 100, 100 만 유효한 좌표
# 드래곤커브는 겹칠 수 있다
# x,y 좌표, 방향, 세대(해당세대까지 진화)
# 각각의 드래곤 좌표를 기억해야할거같은데

# 블로그 참조하자
# 아래 풀이는 잘못됐다
# 회전을 어떻게할지 고민했는데 회전이 아닌 규칙성을 찾아야했다

# 구현 문제는 아이디어가 가장 중요하구나
# 아이디어 => 직접 그려보면 규칙성이 보임
# 참조 https://kyun2da.github.io/2021/04/06/dragonCurve/
# 이건 다시 풀어보자..


# def upgrade(index): # 회전 + 꼭지점에 붙인 좌표 return
#     before_x, before_y = dragon_pos[index] # 꼭지점
#     after_x, after_y = 0, 0
#     temp = [[0] * 100 for _ in range(100)]
#     pos = []
#     for i in range(100):
#         for j in range(100):
#             if data[i][j] == index:
#                 pos.append((j, 100 - i - 1))
#                 # temp[j][100-i-1] = data[i][j]
#                 if i == before_x and j == before_y:
#                     after_x = j
#                     after_y = 100 - i - 1
#
#     x_gap = before_x - after_x
#     y_gap = before_y - after_y
#
# n = int(input())
# data = [[0] * 100 for _ in range(100)]
# dragon = []
# dragon_pos = []
# move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# for i in range(n):
#     y, x, d, g = map(int, input().split())
#     dragon.append((x, y, d, g))
#     data[x][y] = i
#     data[x+move[d][0]][y+move[d][1]] = i
#     dragon_pos.append((x+move[d][0], y+move[d][1])) #꼭지점
#
#
# for i in range(len(dragon)):
#     g = dragon[i][3]  # 세대
#     while g > 0:
#         g -= 1
#         dragon_pos[i] = (upgrade(i))
#
# all_pos = []
# for i in range(len(dragon_pos)):
