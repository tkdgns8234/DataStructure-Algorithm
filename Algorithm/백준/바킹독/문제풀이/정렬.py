# 문제1. 역원소 정렬
# n, *nums = input().split()
# while len(nums) < int(n):
#     nums += input().split()
#
# for i in range(len(nums)):
#     nums[i] = int(nums[i][::-1])
#
# nums.sort()
# for i in nums:
#     print(i)

# 2. 단어 정렬
# n = int(input())
# data = []
# for _ in range(n):
#     data.append(str(input()))
# data = list(set(data))
#
# data.sort(key= lambda x: (len(x), x))
# for i in data:
#     print(i)

# 3. 빈도 정렬
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# dic = dict()
# for i in range(n):
#     num = data[i]
#     if num not in dic:
#         dic[num] = 1
#     else:
#         dic[num] += 1
# data.sort(reverse=True, key=lambda x: (dic[x], -list(dic.keys()).index(x)))
# print(" ".join(map(str, data)))

# 4 .먹을것인가 먹힐것인가
# bisect_left 처럼 처리해야함
# 중복인 경우 문제가 생기기 떄문에
# 참 좋은문제였다
# 일단 이런문제는 그냥 bisect 라이브러리 사용하면 정말 쉽게 풀 수 있다
# 그래도 그냥 구현해봤다
# bisect_left는  아래 코드의 if b[mid] >= target: 부분때문에 left가 된것이고
# if b[mid] > target: 처럼 등호가 사라지는경우 bisect_right 처럼 탐색된다
#
# import sys
#
# def bisect(start, end, target):
#     near = 0
#     while start <= end:
#         mid = (start + end)//2
#
#         # if b[mid] == target:
#         #     return mid
#
#         if b[mid] >= target:
#             end = mid - 1
#             near = mid
#         else:
#             start = mid + 1
#             near = mid + 1
#     return near
#
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().rstrip().split())
#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))
#     a.sort()
#     b.sort()
#     result = 0
#     for i in a:
#         result += bisect(0, len(b)-1, i)
#     print(result)
