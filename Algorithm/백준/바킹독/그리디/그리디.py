# 그리디: 가장 최적의 답을 근시안적으로 택하는 알고리즘
# 코테 시, 그리디 풀이법에 확신이 있다면 풀어보고 틀리면 바로 넘어간다
# (풀이자체가 틀린건지 구현이 틀린건지 구분이 쉽지않음)
# 확신이 없다면 마지막에 푼다 30~40분 남기고

# 문제1 동전0
# 한방에 성공! 각 동전이 배수 형태로 존재하기 때문에 그리디로 해결 가능
# dp 로 해결하려는경우 O(nk)로 10억이 훨씬넘어가서 풀 수 없다
# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
#
# count = 0
# while True:
#     if k == 0:
#         break
#     for c in coins[::-1]:
#         if k // c > 0:
#             count += k // c
#             k = k % c
#             break
#
# print(count)

# 문제2 회의실 배정
# 0부터 기준 시간을 설정하고 기준시간 이후의 시간 중 가장 빨리끝나는 회의를 계속 찾으면 최대의 회의를 잡을 수 있다
# 기준시간은 회의가 추가될때마다 회의의 끝시간으로 update 한다
# 정렬 시 끝시간만 정렬하는게 아니라 시작시간도 정렬해야한다
# 2,2 1,2 일 경우가 존재하기 때문
# 튜플로 정렬 시, 여러기준으로 정렬 가능

# n = int(input())
# meeting = [list(map(int, input().split())) for i in range(n)]
# meeting.sort(key=lambda x: (x[1], x[0]))
#
# pivot = 0
# count = 0
# for m in meeting:
#     if pivot <= m[0]:
#         count += 1
#         pivot = m[1]
# print(count)

# 문제3 로프
# 한번에 맞아버렸다..
# 잘 모르겠을 땐 직접 그림을 그리면서 해결하는게 아주 큰 도움이 된다
# 루프의 크기를 오름차순으로 정렬한 후
# 작은 수 부터 본인의 무게 * (자기보다 큰 수의 갯수) 를 계속 계산한다
# => 최대 중량 계산가능
# 시간복잡도도 충분

# n = int(input())
# data = [int(input()) for _ in range(n)]
#
# data.sort()
# result = []
#
# for i in range(n):
#     result.append(data[i] * (n - i))
#
# result.sort()
# print(result[n-1])

# 문제4 보물
# 큰 설명이 필요없어보인다
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# a.sort(reverse=True)
# b.sort()
#
# result = 0
# for i in range(n):
#     result += a[i] * b[i]
# print(result)

# 문제5 평범한 배낭
# 그리디로 풀 수 있을거같지만 여러 반증을통해 그렇지 않다는걸 깨닳을 수 있다
# 이문제는 유명한 dp 유형의 문제이다
# 0-1 knapsack 문제로 분류된다 (물건을 분할할 수 없는경우)
# 상당히 어려운 문제다 풀이 패턴을 파악하고있어야만 나중에 비슷한 유형을 풀 수 있을것 같다
# 1. dp 테이블 정의
# dp[i][j] i: 물건의 종류 j = 가치 // 물건의 종류마다 가치에 해당하는 최댓값을 계속 업데이트 한다

# n, k = map(int, input().split())
# dp = [[0] * (k + 1) for i in range(n + 1)]
#
# object = [(0, 0)]
# for i in range(n):
#     data = list(map(int, input().split()))
#     object.append((data))
#
# for i in range(1, n + 1):
#     weight, value = object[i]
#     for j in range(1, k + 1):
#         if weight > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
# print(dp[n][k])
# 반대로 쪼갤 수 있는 knapsack 알고리즘의 경우
# 그리디로 해결 가능하다
# 가치가 제일높은애들을 최대한 담고 공간이 부족하면
# 하나를 쪼개서 부분적으로 넣고 끝낸다
# 굳이 풀이를 하진 않겠다

# 문제6 휴게소 세우기
# ---------------------------------- 전혀 틀린 풀이.. greedy는 절대 성립이 안됨
# 이진 탐색으로 풀어야함
# 이진탐색으로 다시풀자

# def find_max_dist():
#     global rest_store
#     rest_store.sort()
#     length = len(rest_store)
#
#     #초깃값 설정
#     position1 = rest_store[0]
#     position2 = rest_store[1]
#     max_val = position2 - position1
#
#     for i in range(length - 1):
#         if max_val < rest_store[i + 1] - rest_store[i]:
#             max_val = rest_store[i + 1] - rest_store[i]
#             position1 = rest_store[i]
#             position2 = rest_store[i + 1]
#
#     # 마지막 rest store와 고속도로간의 거리 차이도 계산
#     if max_val < distance - rest_store[length-1]:
#         max_val = distance - rest_store[length-1]
#         position1 = rest_store[length-1]
#         position2 = distance
#
#     return max_val, position1, position2
#
#
# n, m, distance = map(int, input().split())
# rest_store = list(map(int, input().split()))
# added_dist = []
#
# for i in range(m):
#     max_val, store1, store2 = find_max_dist()
#
#     if (store1 + store2) % 2 > 0:
#         exist = False
#         val = 1
#         for s in added_dist:
#             if s[0] <= store1 and store2 >= s[1]:
#                 exist = True
#                 if s[2] == 1:
#                     val = -1
#                     s[2] = -1
#                 elif s[2] == -1:
#                     val = 1
#                     s[2] = 1
#
#         if not exist:
#             added_dist.append([store1, store2, 1])
#         rest_store.append((store1 + store2) // 2 + val)
#     else:
#         rest_store.append((store1 + store2) // 2)
#
# print(find_max_dist()[0])
#
# ---------------------------------- 전혀 틀린 풀이.. greedy는 절대 성립이 안됨