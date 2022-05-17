# 버블정렬 수행 시,
# swap 하지 않아도 되는 loop
# 앞에 큰 수가 있는 개수의 최댓값 + 1? 인거같은데

# 실패
# import sys
#
# sys.setrecursionlimit(int(1e5))
#
# def merge_sort(start, end):
#     global max_val
#     if start < end:
#         mid = (start+end)//2
#         merge_sort(start, mid)
#         merge_sort(mid+1, end)
#
#         l, r = start, mid+1
#         temp = []
#         while l <= mid and r <= end:
#             if data[l] < data[r]:
#                 temp.append(data[l])
#                 l += 1
#             else:
#                 temp.append(data[r])
#                 max_val = max(mid-l+1, max_val)
#                 r += 1
#
#         if l <= mid:
#             temp += data[l:mid+1]
#         if r <= end:
#             temp += data[r:end+1]
#
#         for i in range(len(temp)):
#             data[start+i] = temp[i]
#     return
#
# N = int(input())
# data = [int(input()) for _ in range(N)]
# max_val = 0
# merge_sort(0, N-1)
#
# print(max_val+1)


# 풀이 참조, 재풀이
# 시간 초과를 막기위해 규칙성을 찾아야 한다
# 버블정렬 수행 시, 왼쪽으로 원소가 한칸씩 밀린다.
# 각 요소가 한 싸이클에 최대 한칸씩 왼쪽으로 밀리므로
# 정렬 전, 후를 비교해서 최대로 왼쪽으로 밀린 수 + 1 을 출력한다.
import sys

input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    num = int(input())
    data.append([i, num])

data.sort(key=lambda x:x[1])

max_diff = -1
for idx, data in enumerate(data):
    diff = data[0] - idx
    max_diff = max(diff, max_diff)
print(max_diff+1)