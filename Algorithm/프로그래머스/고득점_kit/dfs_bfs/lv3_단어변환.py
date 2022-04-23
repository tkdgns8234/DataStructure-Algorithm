# 원큐에 성공!
# bfs 이용 풀이
from collections import deque

def str_diff(a, b):
    ret = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ret += 1
    return ret

def solution(begin, target, words):
    visited = [False] * len(words)
    q = deque([(begin, 0)])

    answer = 0
    while q:
        now, dist = q.popleft()
        if now == target:
            answer = dist
            break
        for i in range(len(words)):
            if not visited[i]:
                if str_diff(now, words[i]) == 1:
                    visited[i] = True
                    q.append((words[i], dist+1))
    return answer

v = solution("hit", "cog",	["hot", "dot", "dog", "lot", "log"])
print(v)



# 다른 풀이
# dict 와 yield를 이용한 풀이
# 참신하네
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)