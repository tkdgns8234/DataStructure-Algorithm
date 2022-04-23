# union - find 알고리즘같은데
# 성공
# 아래 bfs, dfs 이용 풀이가 있는데
# 나중에 bfs, dfs로 다시 풀어보자
# 특히 dfs는 꼭 stack 형식으로 풀어보자 경험삼아 좋아보인다.

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                union_parent(i, j, parent)

    for i in range(n):
        find_parent(i, parent) # parent가 업데이트 되지 않는 문제

    return len(set(parent))

v = solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])
print(v)




# 다른 풀이
# dfs 를 이용한 풀이인데, 깊이 제한이 있어서 스택으로 대체하여 푼 코드다
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i+=1
    return answer

# 다른 코드
# bfs 이용 풀이
def solution(n, computers):
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer
