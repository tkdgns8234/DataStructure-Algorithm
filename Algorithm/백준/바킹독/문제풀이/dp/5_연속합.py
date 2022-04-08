# 5. 연속합
# dp말고 다른 풀이가 떠올랐어
# -1 기준으로 끝나는게 아니었어. 틀린풀이
# 블로그 참조해봤다 규칙성을 찾는게 쉽지 않은문제였다
# 나중에 다시 풀자
# num = int(input())
# data = list(map(int, input().split()))
#
# result = []
# data.append(-1)
#
# start = 0
# for i in range(num):
#     if i > 0 and data[i] < 0:
#         result.append(sum(data[start:i]))
#         start = i + 1
#
# print(max(result))

# 블로그 참조
# 지속적으로 합을 더하다가, 더한 합이 현재 index의 수보다 작으면 값을 현재 index 값으로 갱신하는 방식
# n = int(input())
#
# arr = list(map(int, input().split()))
# dp = [0] * len(arr)
# dp[0] = arr[0]
#
# for i in range(1, len(arr)):
#     dp[i] = max(arr[i], dp[i-1] + arr[i])
#
# print(dp)
# print(max(dp))
#
#
# 다시 풀기
N = int(input())
data = list(map(int, input().split()))
dp = [0] * 100_001
dp[0] = data[0]
ans = dp[0]

for i in range(1, N):
    dp[i] = max(data[i], dp[i-1] + data[i])
    ans = max(ans, dp[i])

print(ans)