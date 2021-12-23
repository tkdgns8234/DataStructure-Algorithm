# stack 구현
# 괄호 맞추기 ()()(()
# list로 편하게 구현할 수 있음
# push, pop, top, len 함수 지원
# append, pop, top, len ->O(1) // 상수시간 소요되는 자료구조

class Stack:
    def __init__(self):
        self.list = list()

    def push(self, n):
        self.list.append(n)

    def pop(self):
        self.list.pop()

    def top(self):
        return self.list[-1]

    def __len__(self):
        return len(self.list)

# 괄호 맞추기
import sys

str = sys.stdin.readline().strip()
s = Stack()

try:
    for word in str:
        if word == '(':
            s.push('(')
        elif word == ')':
            s.pop()
        else:
            print("올바른 문자를 입력하세요")
    if len(s):
        print("괄호의 갯수가 일치하지 않습니다.")
    else:
        print("괄호의 갯수가 일치합니다.")
except IndexError:
    print("괄호의 갯수가 일치하지 않습니다.")
