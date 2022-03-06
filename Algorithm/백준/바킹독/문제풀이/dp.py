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
# dp 테이블 정의를 앞에서부터 세우려고하면 세워지지 않는다
# 뒤에서부터 계산해보자
# 블로그 참조했음, 다시풀자
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# dp = [0] * (n + 1)
# for i in range(n-1, -1, -1):
#     if data[i][0] + i > n:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]])
#
# print(dp[0])

# 10. 퇴사2
# 위와 동일한 문제, 다른 풀이가 있네?
# 시간복잡도는 O(n)으로 동일해보이는데 한번 해보자
# 그리 좋은풀이같지가 않아 직관적이지 않고 어려워 위 풀이가 훨씬 더 좋아보여
# n = int(input())
# dp = [0] * (n+1)
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# m  = 0
# for i in range(n):
#     m = max(m, dp[i])
#     if i + data[i][0] > n:
#         continue
#     else:
#         dp[i+data[i][0]] = max(dp[i+data[i][0]], data[i][1] + m)
#
# print(max(dp))


# 11. 쉬운 계단 수
# 실패
# 블로그참조
# 여러 dp 문제가 2차원배열의 점화관계 해결되는경우가 있다
# 수의 마지막 자리 수의 갯수를 2차원배열형태로 나타내보면 규칙을 찾을 수 있다.
# 다시 풀어보자


# 12. LCS
# 이것도 2차원배열형태로 나타낸 후 점화식도출이 가능하네,,
# 나타내도 점화식 찾는게 쉽지는 않아보이긴한다
# 다시풀자
# 아래 블로그의 2번 풀이는 환상적이다
# 1번풀이도 관찰해보자
# https://myjamong.tistory.com/317

# 13. 제곱수의 합
# 실패, 난리네,,
# 아이디어만 떠올리면 할만한 문제였다
# 다시풀자

# 14. 동전
# 실패
# 어디서 많이 본 문제같더라니 냅색(배낭) 알고리즘으로 불리우는 유형의 문제였다
# 각 단위별로 만들수 있는 모든 경우의수를 차근차근 더해나가는 방식
# 다시풀자

# 15. 가장 큰 정사각형
# 모든 부분을 확인하려면 최악의경우 1000*1000^2 가 소요되니
# dp로 풀어야한다는 생각을 떠올려야한다
# 다시풀자

# 16. 팰린드롬?
# 다시풀자
# dp 왜이렇게 어렵지
# 일단. 브루트포스는 매우 높아보임
# dp는 On^2
# 안쪽부터 바깥쪽으로 뻗어나가면서
# 한칸 안쪽이 팰린드롬이면 바깥쪽이 같으면 팰린드롬으로 인지하는
# dp 기법

# 17. 돌 게임
# 다시
# 비슷한 문제의 좋은 설명 https://dailymapins.tistory.com/111

# 18. 암호코드
# 다시
# 블로그 https://jyeonnyang2.tistory.com/55
# 자꾸 dp에서 아이디어가 전혀 떠오르지 않는 이유가 뭘까
# 테이블을 명확히 정의한 후
# 예제를 정확히 써내려가면서
# 예제에대한 규칙성을 찾아내는게 dp다 규칙성을 찾는데 집중해봐
# 어떤원리로 어떤 숫자가 추가되는지 원리를 파악하는과정이야
