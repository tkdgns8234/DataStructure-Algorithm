# set로 풀고싶네 ㅋㅋㅋㅋ 일단 이진탐색 연습이니 이진탐색으로 풀자
import sys

input = sys.stdin.readline
N = int(input())
data1 = list(map(int, input().split()))
M = int(input())
data2 = list(map(int, input().split()))

data1.sort()


def solve(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if data1[mid] == target:
        return 1
    elif data1[mid] > target:
        return solve(start, mid - 1, target)
    else:
        return solve(mid + 1, end, target)


for i in data2:
    print(solve(0, N-1, i),sep=' ')
