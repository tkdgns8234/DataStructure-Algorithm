# 큐: FIFO 형식의 순차 자료구조
#          stack     queue
# insert   push     enqueue
# delete   pop      dequeue

# 큐의경우, list, front_index 선언 필요

# dequeue 를 할때 pop으로 리스트 맨 앞의 요소를 삭제하지 않는 이유
# 맨 앞의 list 요소 삭제시, O(n)만큼의 시간 소요 (한칸씩 이동 필요)
# -> index를 두어 front 부분을 지칭하고, 삭제된것처럼 사용  O(1)만큼의 시간 소요 (빠름)

# -> deque 라는 collections 라이브러리 모듈로 큐를 만들어보자
'''
from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.popleft()
dq.popleft()
dq.popleft()

print(dq)
'''

# 그냥 list랑 first_index 만들어서 O(1) 형태로 시간소요되게 (pop을 하지 않음)
'''
class Cqueue:
    def __init__(self):
        self.data = list()
        self.front_index = 0

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        x = self.data[self.front_index]
        self.front_index += 1
        return x

    def show(self):
        for i in range(self.front_index, len(self.data)):
            print(self.data[i])

q = Cqueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.show()
'''
"""
# 보너스 요세푸스 문제
# 입력 (7,3)
import sys

N, K = map(int, sys.stdin.readline().strip().split())

arr = []
nums = [i for i in range(1, N+1)]

del_index = 0
for i in range(N):
    del_index += (K - 1)
    if del_index >= len(nums):
        del_index = del_index % len(nums)

    arr.append(str(nums.pop(del_index)))

print("<", ", ".join(arr), ">", end="")
# 어려웠던점
# 1. join은 문자열을 다루는거기떄문에 list 넣을때 숫자(int) 형이면 안됨
# 2. index % 연산
"""

