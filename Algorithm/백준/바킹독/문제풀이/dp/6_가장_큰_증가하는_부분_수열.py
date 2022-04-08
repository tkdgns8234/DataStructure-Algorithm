# 6. 가장 큰 증가 부분 수열
# 아래에서 멈춤
# n = int(input())
# data = list(map(int, input().split()))
# dp = [0] * 1000
# dp[0] = data[0]
#
# for i in range(1, len(data)):
#     if data[i-1] < data[i]:
#         dp[i] = dp[i-1] + data[i]
#     else:
#         dp[i] = data[i]
# print(dp)
# print(max(dp))

# 아래 풀이1,2 방법은 dp i 를 무조건포함하는오름차순의 최댓값으로 구한듯
# else문도 주의깊게 보자
# 이거 쉽지 않은데?
# 나중에 다시풀어보자

# # 풀이1
# n=int(input())
# array=list(map(int, input().split()))
#
# d=[1]*n
# d[0]=array[0]
# for i in range(1,n):
#   for j in range(i):
#     if array[j]<array[i]:
#       d[i]=max(d[i], d[j]+array[i])
#     else:
#       d[i]=max(d[i], array[i])
#
# print(d)
# print(max(d))
#
# # 풀이2
# n = int(input())
# lst = list(map(int, input().split()))
#
# dp = [x for x in lst]
#
# for i in range(n):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + lst[i])
#
# print(dp)
# print(max(dp))



# 다시 풀기
N = int(input())
data = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = data[1]

for i in range(2, N+1):
    dp[i] = max(dp[k] for k in range(i-1, -1, -1) if data[i] > data[k]) + data[i]

print(max(dp))