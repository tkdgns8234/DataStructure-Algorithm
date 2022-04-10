# 16. 팰린드롬?
# 다시풀자
# dp 왜이렇게 어렵지
# 일단. 브루트포스는 매우 높아보임

# 문제의 핵심
# 팰린드롬을 확인 할 때 바깥쪽 양 끝부터
# 범위를 1칸씩 줄여가며 팰린드롬인지 계속 확인하는 과정을 거침
# -> 작은 문제의 반복 -> dp

# 문자열 갯수
# 1개 -> 팰린드롬
# 2개 -> 같으면 팰린드롬
# 3개 이상 -> i, j 일때 i == j 이고 i+1, j-1 이 팰린드롬이면 팰린드롬
# 블로그 참조했다. 다시풀자
import sys

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
dp = [[False] * 2000 for _ in range(2000)]

# 1개
for i in range(N):
    dp[i][i] = True
# 2개
for i in range(N-1):
    if data[i] == data[i+1]:
        dp[i][i+1] = True
# 3개 이상
for i in range(2, N):
    for j in range(N-i):
        if data[j] == data[j + i]:
            if dp[j+1][j+i-1]:
                dp[j][j+i] = True

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(1 if dp[S-1][E-1] else 0)