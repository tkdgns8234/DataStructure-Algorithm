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
#     else:
#         d[0][0]

# 다시풀기
# 바킹독 풀이 참고
# 일, 월을 월에 100 곱한 형식으로 표현하는게 포인트!!!!
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