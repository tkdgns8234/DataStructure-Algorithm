# 1. ATM
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0
# sum = 0
# for i in data:
#     sum += i
#     result += sum
#
#
# print(result)

# 2. 공주님의 정원
# 시작날짜 기준으로 개화길이정렬
# 1년내내 개화해야하는 조건만족 + 긴것 선택
# 아래까지 풀었는데 코드가 너무 더러워;
# 일, 월을 날짜로 바꾸는게 계산이 편해질듯

# month_day = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
# # 개화기간 return
# def flower_date(sm, sd, em, ed):
#     days = 0
#     for i in range(sm, em + 1):
#         days += month_day[i]
#     days += (ed-sd)
#     return -days  # 역순정렬을 위해 - 붙여서 return
#
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# data.sort(key=lambda x: (x[0],x[1],flower_date(x[0],x[1],x[2],x[3])))
# result = 0
#
# start_month = 3
# start_day = 1
#
# for d in data:
#     if d[0][0] == start_month and d[0][1] == start_day:
#         continue
#     else
#         d[0][0]

# 다시풀기
# 바킹독 풀이 참고
# 일, 월을 월에 100 곱한 형식으로 표현
# n = int(input())
# date = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     start = data[0]*100 + data[1]
#     end = data[2]*100 + data[3]
#     date.append((start, end)) #(시작, 끝)
#
# date.sort()
#
#
# index = 0
# count = 0
# start = 301
#
# # 시작날짜를 만족하는, 가장 긴 것을 선택, 반복
# while start < 1201:
#     next_start = start
#     for i in range(n):
#         if date[i][0] <= start and date[i][1] > next_start:
#             next_start = date[i][1]
#     if next_start == start:
#         print(0)
#         exit(0)
#     count+=1
#     start = next_start
# print(count)

# 3. 잃어버린 괄호
# 실패 원리는 알았는데 코딩을 못하겠네 ㅠ 너~~~무 길고 지저분해
# 아래 진행 중 멈춘코드
# 아래 정답코드 있음
# 다시풀자
# from collections import deque
# S = list(input())
#
# # - 가 나오면 다시 - 가 나오기 전까지 괄호 추가
# flag = False
# for i in range(len(S)):
#     if S[i] == '-':
#         if not flag:
#             S.insert(i+1, '(')
#             flag = True
#         else:
#             S.insert(i, ')')
#             flag = False
#     if i == len(S)-1 and flag: # 마지막인데 - 가 나오지 않은경우 ) 추가
#         S.append(')')
#
# temp = 0
# flag = False
# oper = deque()
# result = 0
# num = ''
# for i in S:
#     if i == '-':
#         oper.append(int(num))
#         oper.append(i)
#         num = ''
#     elif i == '+':
#         if flag:
#             temp += int(num)
#             num = ''
#         else:
#             oper.append(int(num))
#             oper.append(i)
#             num = ''
#     elif i == '(':
#         flag = True
#     elif i == ')':
#         flag = False
#         oper.append(temp)
#         temp = 0
#     else:
#         num += i
# # 마지막 num 추가
# oper.append(int(num))
#
# print(oper)

# 정답 코드
# 다시풀자
# arr = input().split('-')
# s = 0
# for i in arr[0].split('+'):
#     s += int(i)
# for i in arr[1:]:
#     for j in i.split('+'):
#         s -= int(j)
# print(s)

# 4. 주식
# 가장 큰 값을 찾고 그 앞에있는 값들을 모두 산 후 큰값인 날에 판다
# list 가 0 이될떄까지 반복한다
# -> 시간복잡도 안될거같은데
# O(n) 또는 Log(n) 시간내에 해결하지 않으면 불가하다

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     data = list(map(int, input().split()))
#
#     result = 0
#     m = int(-1e9)
#     for i in range(len(data)-1, -1, -1):
#         if m > data[i]:
#             result += m - data[i]
#         else:
#             m = data[i]
#     print(result)

# 5. 수 묶기
# 입력으로 들어온 값을 오름차순 정렬
# 값이 1보다 큰 경우 묶는것처럼 계산
# 아래 코드 작성하는데,, 코드가 너무 복잡해졌다
# 가독성 + 간단히 짜는 연습 계속 하자
# 다시풀자
# 매번 문제 해결 방법을 정확히 정의하고 풀어야하는것인가?
# 해당 문제는 수 묶기 규칙을 모두 찾은 후 코딩하면 더 좋은 구조로 짤 수 있을거같다
# 양수, 음수, 0인경우 모두 확인해서
# 묶는 방법을 정의하고 개선 해 나가는방법

# n = int(input())
# data = []
# for _ in range(n):
#     data.append(int(input()))
#
# data.sort()
# result = 0
# i = len(data)-1
# while i >= 0:
#     if i == 0:        # 홀수인 경우 and 한 개 남은 경우
#         result += data[i]
#         break
#     else:
#         if data[i-1] > 1: # 왼쪽에 있는 값이 1보다 큰 경우 곱셈
#             result += data[i]*data[i-1]
#             i -= 2
#         else:
#             if data[i] == 0:
#                 if i % 2 == 0 and i >= 1 and data[i-1] == 0: # 홀수 개가 남았고 0이 더있으면
#                     i -= 1
#                     continue
#                 else:
#                     result += data[i]*data[i-1]
#                     i -= 2
#             else: # -인경우
#                 result += data[i]
#
# print(result)

# 묶는 방법을 처음에 정확하게 정해놓지 않으면
# 시행착오를 계속 겪게되고 코드도 복잡해진다
# 묶는 방법 (묶었을 때 최대가 되는 방법)
# 0 -> 음수로 처리 -> 이게 이 문제의 포인트 중 하나다
# 1 -> 무조건 더하는게 좋다
# 양수 -> 높은 값 끼리 곱셈
# 음수 -> 낮은 값 끼리 곱셈

# n = int(input())
# positive = []
# negative = []
# one = []
# for _ in range(n):
#     num = int(input())
#     if num == 1:
#         one.append(num)
#     elif num > 1:
#         positive.append(num)
#     else:
#         negative.append(num)
#
# positive.sort(reverse=True)
# negative.sort()
#
# result = 0
# if len(positive) % 2 == 0: #짝수 갯수인 경우
#     for i in range(0, len(positive)-1, 2):
#         result += positive[i]*positive[i+1]
# else:
#     for i in range(0, len(positive)-2, 2):
#         result += positive[i]*positive[i+1]
#     result += positive[len(positive)-1]
#
# if len(negative) % 2 == 0: #짝수 갯수인 경우
#     for i in range(0, len(negative)-1, 2):
#         result += negative[i]*negative[i+1]
# else:
#     for i in range(0, len(negative)-2, 2):
#         result += negative[i]*negative[i+1]
#     result += negative[len(negative)-1]
# result += len(one)
# print(result)

# 6. 선 긋기
# O(n) 이하의 시간복잡도로 해결해야함
# 데이터를 정렬한 후
# 시작점 끝점 기준으로 시작점이 이전끝점보다 안쪽에 존재하는 경우
# 이전 데이터의 끝점을 갱신
# 아닌경우
# 신규대입
# 정렬 상태이기떄문에 n^2 시간소요되지않음
# 시간이 rstrip, sort에 따라 천지차이네?
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)] # rstrip() 을 추가하면 시간 700~800ms 더 소요
# data.sort(key=lambda x: x[0])  # data.sort() 시, 시간 1000ms 더 소요, 정렬하고자하는 데이터가 크기 때문 2개 정렬 시 O(nlogn+nlogn)
#
# result = 0
# before_start, before_end = data[0][0], data[0][1]
# for i in range(1, n):
#     start = data[i][0]
#     end = data[i][1]
#
#     if start <= before_end < end:
#         before_end = end
#
#     elif before_end < start:
#         result += before_end - before_start
#         before_end = end
#         before_start = start
#
# # 한번의 계산은 더 해야한다
# result += before_end - before_start
#
# print(result)

# 7. 멀티탭 스케줄링
# 사용 횟수가 많은것을 마지막에 빼는 방식이 최선인것처럼 보이는데
# 사용 횟수가 많은것을 뺀다 라는 개념 자체가 잘못됐다
# 멀티탭에 동일한 제품이 있는경우 or 자리가 있는경우 or 자리가 없는 경우로 로직 구현
# 자리가 없는 경우 가 어려웠음
# 1. 이후에 꽃을일이 없는 제품을 뺀다
# 2. 가장 나중에 꽃는 제품을 찾는다
# 다시풀자
# 아래는 틀린 풀이

# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# data = list(map(int, input().split()))
#
# cnt = [0] * (K+1)
# for i in data:
#     cnt[i] += 1
#
# ans = 0
# adapted = []
# for i in range(len(data)):
#     if len(adapted) < N:
#         adapted.append(data[i])
#     elif data[i] not in adapted:
#         val = 0
#         count = int(1e9)
#         for k in adapted:
#             if count > cnt[k]:
#                 count = cnt[k]
#                 val = k
#
#         adapted.remove(val)
#         adapted.append(data[i])
#         cnt[val] -= 1
#         ans += 1
#     else:
#         cnt[data[i]] -= 1
#
# print(ans)