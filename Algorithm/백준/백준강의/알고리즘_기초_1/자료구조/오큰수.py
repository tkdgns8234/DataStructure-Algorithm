# 최대 nlogn
# 정렬불가, 이진탐색 불가, 투포인터? 불가
# 자료구조? stack queue dict

# 알고리즘 분류 = 스택인걸 보고 해설이 떠올랐다.. 반성하자
# 시복 반복 2N, data 초기화 N =>3N 정도

stack = []
N = int(input())
data = list(map(int, input().split()))
data = [(i, data[i]) for i in range(len(data))]
answer = [-1]*N

stack.append(data[0])
for i in range(1, len(data)):
    while stack and stack[-1][1] < data[i][1]:
        pos = stack[-1][0]
        stack.pop()
        answer[pos] = data[i][1]
    stack.append(data[i])

print(' '.join(map(str, answer)))


# 더 좋은 방법
# stack에 index를 넣고, 기존 배열 A를 사용
# 시복 2N
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)