import sys

input = sys.stdin.readline
l = list()
N = int(input())
for _ in range(N):
    oper = input().split()
    if len(oper) == 2:
        if oper[0] == 'push':
            l.append(int(oper[1]))
    else:
        if oper[0] == 'top':
            if l:
                print(l[-1])
            else:
                print(-1)
        elif oper[0] == 'size':
            print(len(l))
        elif oper[0] == 'empty':
            if l:
                print(0)
            else:
                print(1)
        elif oper[0] == 'pop':
            if l:
                print(l.pop())
            else:
                print(-1)
