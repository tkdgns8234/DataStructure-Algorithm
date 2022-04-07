# dfs, 백트래킹 유형으로 풀이
# 1. dfs로 십자 모양을 탐색할 수 없기때문에
# 데이터를 담으면서 담은 요소를 4방향으로 탐색
# 2. 중복된 결과가 존재할 수 있기 때문에
# index 순서를 오름차순으로 정렬한 후에 대입(set 자료형에) 및 확인

def btk(depth, S, Y):
    global count

    if Y >= 4:
        return
    if depth == 7:
        p = tuple(sorted(points)) #set 자료형에 list 가 들어갈 수 없으므로 tuple로 치환, 집합 자료형의 키는 해시값을 만드는 값으로 immutable 해야한다.
        if p not in visited:
            visited.add(p)
            count += 1
        return

    for p in points:
        x, y = p//5, p%5
        move_type = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in move_type:
            nx, ny = move[0] + x, move[1] + y
            n = nx*5+ny
            if 0 <= nx < 5 and 0 <= ny < 5:
                if n not in points:
                    points.append(n)
                    if data[nx][ny] == 'Y':
                        btk(depth + 1, S, Y + 1)
                    else:
                        btk(depth + 1, S + 1, Y)
                    points.pop()

data = [list(input()) for _ in range(5)]
points = []
visited = set()
count = 0
for i in range(5):
    for j in range(5):
        points.append(i*5+j)
        if data[i][j] == 'Y':
            btk(1, 0, 1)
        else:
            btk(1, 1, 0)
        points.pop()

print(count)


# 모든 조합 뽑은 후
# bfs 를 통해 모두 이어져있는지 확인하는 방식
# Y 가 4개 이상이면 안된다.

# 모든 조합을 뽑는 법: x를 뽑거나, 뽑지 않거나 두가지 경우 모두 탐색
import collections

def bfs():
    x, y = picked[0]
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    q = collections.deque([(x, y)])
    count = 1
    while q:
        x, y = q.popleft()
        move_type = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in move_type:
            nx, ny = x+move[0], y+move[1]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) in picked and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    q.append((nx, ny))
    return True if count == 7 else False

def btk(depth, index, Y):
    global answer, picked
    if Y >= 4:
        return
    if 25 - index < 7 - depth:
        return
    if depth == 7:
        if bfs():
            answer += 1
        return

    x, y = index//5, index%5
    picked.append((x, y))
    if data[x][y] == 'Y':
        btk(depth+1, index+1, Y+1)
    else:
        btk(depth+1, index+1, Y)
    picked.pop()
    btk(depth, index+1, Y)


data = [list(input()) for _ in range(5)]
answer = 0
picked = []
btk(0, 0, 0)
print(answer)


# 조합 라이브러리 이용

from collections import deque
from itertools import combinations
move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
data = [input() for i in range(5)]
comb = list(combinations([i for i in range(25)], 7))

def bfs():
    global rs
    for c in comb:
        y_count = 0
        for i in range(len(c)):
            val = c[i]
            x, y = val//5, val % 5
            if data[x][y] == 'Y':
                y_count += 1
        if y_count > 3:
            continue

        visited = [[False] * 5 for _ in range(5)]
        start = c[0]
        x, y = start // 5, start % 5
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        count = 1

        while q:
            x, y = q.popleft()
            if count == 7:
                rs += 1
                break
            for move in move_type:
                nx, ny = x+move[0], y+move[1]
                if not (0 <= nx < 5 and 0 <= ny < 5) or visited[nx][ny]:
                    continue
                if nx*5+ny in c:
                    count += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True

rs = 0
bfs()
print(rs)