# 우선 처음 접하는 트리 유형 문제라 답을 보고도 해석하는데 시간이 오래걸렸다.
# 정점의 갯수가 1,000,000 이므로 dp + tree 를 활용한 문제
# 아래 두 조건을 생각하면서 구현하면 되는문제
# 부모노드가 얼리어답터인 경우 자식노드는 얼리어답터가 아니거나 얼리어답터인 경우의 최솟값이다
# 부모노드가 얼리어답터가 아닌 경우 자식노드는 무조건 얼리어답터다

# dp 테이블: dp[0,1][n] n 노드를 root 노드로 갖는 서브트리의 얼리어답터 최소 갯수
# 0은 해당 노드가 얼리어답터가 아닌 경우
# 1은 해당 노드가 얼리어답터
# 점화식
# dp[0][n] = dp[1][n-1]
# dp[1][n] = max(dp[0][n-1], dp[1][n-1])


# 이 문제의 특징이 있다.
# root 노드가 어떤노드인지 알려주지 않는다는것.
# 그림엔 1이 루트노드인것처럼 표현되어있지만 다른 노드가 루트노드일 수 있다.
# 이에, 1을 루트노드인것처럼 처리하기 위해
# 양방향으로 간선을 놓고 visited를 처리하는 방법을 잘 살펴보자
#         2
#      1        3
#   4     5
# 위 형태여도 간선을 양방향으로 생성하고, visited를 처리한다면 2,3은 1의 자식노드가 된것처럼 처리할 수 있다.
import sys

sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
# 0은 해당 노드가 얼리어답터가 아닌 경우
# 1은 해당 노드가 얼리어답터
dp = [[0] * (N + 1) for _ in range(2)]


def solve(num):
    visited[num] = True
    dp[0][num] = 0
    dp[1][num] = 1

    for i in graph[num]:
        if not visited[i]:
            solve(i)
            dp[0][num] += dp[1][i]
            dp[1][num] += min(dp[1][i], dp[0][i])


solve(1)
print(min(dp[0][1], dp[1][1]))