# 백트래킹으로 풀 수 있는거같은데

# bfs로 해보자

# visit을 3차원으로 해결하는경우 메모리 초과가 발생한다
# 각 수의 합으로 visit처리를 하면 될거같아 -> 합으로 처리하면 안된다. 항상 합은 일정해;
# visit 배열을 1500*1500*1500 으로 처리하면 메모리 초과 발생
# set으로 visit을 관리 -> 메모리 더 효율적이다
# visit배열은 최댓값을 고려해 크기를 1500, 1500, 1500
# 으로 해야하지만 1500,1500,1500 이 나오는 경우는 없기에 set 이 더 효율적

from collections import deque

def next(a, b):
    if a != b:
        big = a if a > b else b
        small = a if a < b else b
        return small+small, big-small
    else:
        return a, b

def bfs(a, b, c):
    q = deque([(a, b, c)])
    while q:
        a, b, c = q.popleft()
        if a==b==c:
            return 1
        if (a,b,c) not in visited:
            visited.add((a,b,c))
            q.append((*next(a, b), c))
            q.append((*next(a, c), b))
            q.append((*next(b, c), a))
    return 0

A, B, C = map(int, input().split())
visited = set()
v = bfs(A, B, C)
print(v)

# 다른 풀이 1
# 방문처리를 2개의 원소로만 했다.
# a,b,c의 합은 일정하다는 법칙을 기반으로
# 최댓값, 최솟값에대한 방문 처리를 하면
# visit은 1500*1500 크기로 방문 처리를 할 수 있다.
# 시간도 이게 훨씬 빠르다
from collections import deque
a,b,c = map(int, input().split())
visited = [[False]*1501 for _ in range(1501)]
tot = a+b+c
def dfs():
    global a,b,c
    q = deque()
    q.append([a,b])
    visited[a][b] = True
    while q:
        a,b = q.popleft()
        c = tot-a-b
        if a==b==c:
            return 1
        for na, nb in ((a,b),(a,c),(b,c)):
            if na < nb:
                nb -= na
                na += na
            elif na > nb:
                na -= nb
                nb += nb
            else: continue
            nc = tot-na-nb
            a = min(min(na,nb), nc)
            b = max(max(na, nb), nc)
            if not visited[a][b]:
                q.append((a,b))
                visited[a][b] = True
    return 0
if tot%3 != 0: print(0)
else:
    print(dfs())

# 다른 풀이2
# 딕셔너리를 사용, 코드는 내 코드와 매우 유사하다
# 이 코드의 좋은점: 세개의 요소 선택할 때 반복문을 활용, 좋은 아이디어다 잘 보자
from collections import deque, defaultdict
stones = list(map(int, input().split()))
visited = defaultdict(bool)
tot = sum(stones)
def dfs():
    q = deque([stones])
    visited[tuple(stones)] = True
    while q:
        a,b,c = q.popleft()
        if a==b==c:
            return 1
        for x,y in ((a,b),(a,c),(b,c)):
            if x == y: continue
            elif x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            z = tot-x-y
            if not visited[(x,y,z)] :
                visited[(x,y,z)] = True
                q.append([x,y,z])
    return 0
if tot%3 != 0: print(0)
else:
    print(dfs())
print(visited)
print(len(visited))