# 매우 어렵게 성공

import sys

N, M = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2

        temp = mid
        cnt = 1
        for i in data:
            temp -= i
            if temp < 0:
                temp = mid
                temp -= i
                cnt += 1
                if cnt > M:
                    break

        if cnt > M:
            start = mid + 1
        else:
            ans = min(ans, mid)
            end = mid - 1

ans = int(sys.maxsize)

binary_search(max(data), 10000*N)
print(ans)

# 더 좋은 코드
# import sys
# input=sys.stdin.readline
# from collections import deque
#
# n,m=map(int,input().split())
#
# lesson=list(map(int,input().split()))
# # print(lesson)
# l=max(lesson)
# r=sum(lesson)
# ans=sys.maxsize
# while l<=r:
#     mid=(l+r)//2
#     cnt=0
#     sum=0
#     for i in range(len(lesson)):
#         if sum+lesson[i]>mid:
#             cnt+=1
#             sum=0
#         sum+=lesson[i]
#     if sum:
#         cnt+=1
#
#     if cnt>m: # 블루레이 개수가 m보다 커 (각 크기가 작음)
#         l=mid+1
#     else:
#         ans=min(ans,mid)
#         r=mid-1
# print(ans)