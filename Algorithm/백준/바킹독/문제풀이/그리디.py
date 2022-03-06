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