# dp 테이블: dp[n][m] m노드를 루트노드로 갖는 서브트리의 우수마을의 합의 최댓값
# n-> 루트노드가 우수마을인 경우 = 0 아닌경우 1

# 루트노드가 우수마을인 경우 자식마을은 우수마을이 무조건 아니다
# 루트노드가 우수마을이 아닌경우 max(자식이 우수인경우, 아닌경우) <- 를 식으로 하면 자동으로 문제의 3번 조건을 만족

# 3번 조건때문에 어려웠다.. 사실 max 로 두개를 비교하면 결국엔 자동으로 맞춰지는거다. max값을 선택하는거니까.. 설명하긴 애매하다.
# 3번 조건: 선정되지 못한 마을에 경각심을 불러일으키기 위해서, '우수 마을'로 선정되지 못한 마을은 적어도 하나의 '우수 마을'과는 인접해 있어야 한다.

# 3번조건때문에 생각했던건데, 아래주석은 생각할 필요가 없었다.
# 루트노드가 우수마을 아닌경우, 자식노드가 2개 이상이면,,, 자식노드중 1개 이상은 우수마을
# 루트노드가 우수마을 아닌경우, 루트노드의 자식노드가 2개 이상이면서 자식노드가 우수마을이 아닌경우
# 해당 자식노드는 1개이상의 자식노드를 가져야함, 해당 노드의 자식노드중 1개이상은 무조건 우수마을

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

n = int(input())
w = [0] + list(map(int, input().split()))
s = [[] for i in range(n + 1)]
visit = [False for i in range(n + 1)]
dp = [[0] * 2 for i in range(n + 1)]

def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]

    for i in s[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0], dp[i][1])

for i in range(n - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

dfs(1)
print(max(dp[1][0], dp[1][1]))