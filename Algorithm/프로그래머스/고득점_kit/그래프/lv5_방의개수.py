# 그래프를 관찰해보면
# 싸이클이 존재하면 하나의 도형이 만들어진다.
# -> 동일한 위치에 다시 도착하면 무조건 도형인거같다
# -> 동일한 위치에 도착하는 갯수만 구하면 될거같은데?
# -> 따로 처리를 위한 배열이나 자료구조를 만들 필요도 없고, 좌표값으로 계산하면 될거같다

# 아쉽게도 틀렸다 (구현 원리는 맞았다 예외를 체크해야한다)

# 힌트 링크: https://programmers.co.kr/questions/14646
# -> 이미 그려진선인지도 확인해야한다
# -> 이미 그려진 선까지는 확인했는데
# 대각선도 체크해야한다.
move = [(-1, 0), (-1, 1), (0, 1),
        (1, 1), (1, 0),
        (1, -1), (0, -1), (-1, -1)
        ]

def solution(arrows):
    all = set([(0, 0)])
    now = set([(0, 0)])
    already_moved = set()

    point = (0, 0)
    answer = 0
    for i in arrows:
        point = (point[0] + move[i][0], point[1] + move[i][1])
        now.add(point)
        if point not in all:
            all.add(point)
        else:
            flag = False
            for i in now:
                if i not in already_moved:
                    flag = True
                    already_moved.add(i)
            if flag:
                answer+=1
            now = set([])

    return answer

v = solution([6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]	)
print(v)

# 다른 풀이
# https://bellog.tistory.com/147
# 방이 생성되는 경우는 아래와 같다
# - 방문한 노드가 이미 방문한 적이 있고,
# - 해당 노드로 들어온 경로는 처음 이동한 경우

import collections

def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)

    # visited : 노드 방문 체크
    # visited_dir : 노드 방문 경로 체크 ((A, B)는 A -> B 경로를 의미)
    visited = collections.defaultdict(int)
    visited_dir = collections.defaultdict(int)

    # arrows 따라 노드 좌표를 큐에 추가
    queue = collections.deque([now])
    for i in arrows:
        # 모래 시계 형태 예외를 처리하기 위해 해당 방향으로 2칸씩 추가한다.
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)

            now = next

    now = queue.popleft()
    visited[now] = 1

    while queue:
        next = queue.popleft()

        # 이미 방문한 노드(visited[x]==1)인 경우
        if visited[next] == 1:
            # 해당 경로로 처음 들어온 경우인 경우 answer++
            # 처음 들어온 경우에 방이 처음 생성되므로!
            if visited_dir[(now, next)] == 0:
                answer += 1
        # 처음 방문한 노드인 경우 방문 체크를 한다.
        else:
            visited[next] = 1

        # 해당 노드로 들어온 경로를 방문 체크해준다.
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer