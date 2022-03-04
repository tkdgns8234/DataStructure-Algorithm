# 1. 피보나치 함수
# 작은 문제의 반복, dp로 해결 가능
# dp 테이블 = i 번째 호출 시, 0과 1의 호출 횟수
# 점화식 dp[i][] = dp[i-1][] + dp[i-2][]
# dp = [[-1] * 2 for _ in range(41)]
# # 초깃값 설정
# dp[0][0] = 1
# dp[0][1] = 0
# dp[1][0] = 0
# dp[1][1] = 1
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     for i in range(2, n + 1):
#         if dp[i][0] == -1:
#             dp[i][0] = dp[i-1][0] + dp[i-2][0]
#             dp[i][1] = dp[i-1][1] + dp[i-2][1]
#     print(dp[n][0], dp[n][1])
#

# 2. 정수 삼각형
# 테이블 정의
# dp[i][j] i 번째에서  j를 선택했을 때 최댓값

# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = data[0][0]
#
# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0: # 첫번째 줄
#             dp[i][j] = dp[i-1][j] + data[i][j]
#         elif j == i: # 마지막 줄
#             dp[i][j] = dp[i-1][j-1] + data[i][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-1] + data[i][j], dp[i-1][j] + data[i][j])
#
# print(max(dp[n-1]))

# 3. 2*n 타일링 2
# n = int(input())
# dp = [0] * 1001
# dp[0], dp[1], dp[2] = 0, 1, 3
# for i in range(3, n + 1):
#     dp[i] = (dp[i-1] + (dp[i-2] * 2)) % 10007
# print(dp[n])

# 4. 이친수
# 해보면 피보나치와 동일한 결과가 나온다
# n = int(input())
# dp = [0] * 91
# dp[1], dp[2] = 1, 1
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])

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

# 풀이1
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

# 풀이2
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

# 7. 가장 긴 증가하는 부분 수열
# 이전 문제 경험으로인해 쉽게 풀었다.
# 나중에 다시 푸는게 좋을거같다

# n = int(input())
# data = list(map(int, input().split()))
# dp = [1] * n # 이전 원소들이 모두 작은경우 1
#
# for i in range(1, n):
#     for j in range(i):
#         if data[j] < data[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))

# 8. 파도반 수열
# dp = [-1] * 101
# dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     for i in range(6, n + 1):
#         if dp[i] == -1:
#             dp[i] = dp[i-5] + dp[i-1]
#     print(dp[n])

# 9. 퇴사