# 연속합 문제의 연장선 같은데 아래는 연속합문제의 답
# n = int(input())
#
# arr = list(map(int, input().split()))
# dp = [0] * len(arr)
# dp[0] = arr[0]
#
# for i in range(1, len(arr)):
#     dp[i] = max(arr[i], dp[i-1] + arr[i])
#
# print(max(dp))


# 안되겠어 나중에 다시풀자

# https://baby-ohgu.tistory.com/24
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] * N
value = 0
prefix_sum = [0]
for i in range(N):
    arr[i] = int(input())
    value += arr[i]
    prefix_sum.append(value)
ans, tmp = 0, 0
for i in range(M - 1, N):
    tmp = min(tmp, prefix_sum[i - M + 1])
    ans = max(ans, prefix_sum[i + 1] - tmp)
print(ans)