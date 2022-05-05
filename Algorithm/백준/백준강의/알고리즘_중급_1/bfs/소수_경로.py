# 각 자릿수를 모두 0~9 숫자로 치환 후 큐에 삽입
# 단, 맨 앞 자리는 1~9 사이의 숫자로 치환
# 방문처리도 해야함 set 으로 하는게 좋아보인다.
# 소수 판별함수 만들고
# 동일 숫자면 stop
# 만들 수 없으면 stop
# 시간 효율을 위해 소수도 미리 만들어놓자
from collections import deque

def get_prime_number():
    ret_val = [False, False] + [True] * (10000-2)
    for i in range(2, 10000):
        if ret_val[i] == True:
            for j in range(i*2, 10000, i):
                ret_val[j] = False
    return ret_val


def bfs(start, target):
    visited = set([start])
    q = deque([[start, 0]])
    while q:
        now, dist = q.popleft()
        if now == target:
            return dist
        for i in range(4):
            for j in range(10):
                # 첫 번째 자리가 0인경우 skip
                if i == 0 and j == 0:
                    continue
                next = list(now)
                next[i] = str(j)
                next = ''.join(next)
                if next not in visited and p_num_list[int(next)]:
                    visited.add(next)
                    q.append((next, dist + 1))
    return -1

T = int(input())
for _ in range(T):
    start, target = input().split()
    p_num_list = get_prime_number()
    rs = bfs(start, target)
    if rs == -1:
        print('Impossible')
    else:
        print(rs)