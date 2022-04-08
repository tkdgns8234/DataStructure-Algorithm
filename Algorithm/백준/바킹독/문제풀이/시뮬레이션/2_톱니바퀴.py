# 문제2. 톱니바퀴
# 잘 풀었는데 개선할점이 많다
# 1. deque를 여러개 만들 수 있다
# list 안에 deque들을 담는 형식으로
# 2. 톱니를 돌리는 dfs 함수를 개선할 수 있다
# 좌 확인, 우 확인 하는 함수를 만들면 돼
# 거기서 재귀호출
# 3. deque에서 rotate 라는 함수로 실제회전시킬 수 있다
# https://hapbbying.tistory.com/64
# 개선의 여지가 많다 다시 풀어보자.
import collections
import sys
input = sys.stdin.readline

# deque 로 구현하려니까 배열형태로 쓸 수 없으니 너무 복잡해진다
# list로 구현하자

def dfs(t_num, side):
    if visited[t_num]:
        return
    visited[t_num] = True

    l = [] # 호출해야할 톱니
    if t_num == 1 or t_num == 2:
        # 좌 우 확인
        # 좌
        if T[t_num-1][2] != T[t_num][6]:
            l.append(t_num-1)
        # 우
        if T[t_num+1][6] != T[t_num][2]:
            l.append(t_num+1)

    elif t_num == 0:
        # 우만 확인
        if T[t_num + 1][6] != T[t_num][2]:
            l.append(t_num + 1)
    elif t_num == 3:
        # 좌만 확인
        if T[t_num-1][2] != T[t_num][6]:
            l.append(t_num-1)
    # 회전 후 호출
    # 회전
    if side == 1: #시계
        v = T[t_num].pop()
        T[t_num].insert(0, v)
    else: #반시계
        v = T[t_num].pop(0)
        T[t_num].append(v)
    for num in l:
        dfs(num, -side)

# 0: N 1: S
T = [list(input().rstrip()) for _ in range(4)]
K = int(input()) # 회전 횟수
op = [list(map(int, input().rstrip().split())) for _ in range(K)]

# side 1: 시계방향 -1: 반시계방향
for t_num, side in op:
    visited = [False] * 4
    dfs(t_num-1, side)

score = 0
for i in range(4):
    if T[i][0] == '1':
        score += 2 ** i
print(score)