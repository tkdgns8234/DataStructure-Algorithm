# 대놓고 크루스칼 알고리즘 문제다
# 크루스칼도 그리디의 일종이지.
# 시간복잡도: 정렬시간
# 싸이클이 존재하지 않는 모든 노드가 연결된 신장트리의 최소거리
# 잘했다.
# 오랜만에 풀었는데 기억이 났어
# 단, union_parent 부분에서 살짝 틀렸었다
# 아래와 같이 풀이 했는데, b또는 a에대해서만 parent 노드를 바꾸면 안된다.
# 다른 거쳐가는 모든 노드의 parent 노드도 바껴야 하기 때문에 아래 본문 코드처럼 작성해야함

# def union_parent(parent, a, b):
#     p_a = find_parent(parent, a)
#     p_b = find_parent(parent, b)
#
#     if p_a < p_b:
#         parent[b] = p_a
#     else:
#         parent[a] = p_b

def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    answer = 0
    for cost in costs:
        a, b = cost[0], cost[1]
        if find_parent(parent, a) != find_parent(parent, b):
            answer += cost[2]
            union_parent(parent, a, b)

    return answer