from collections import deque

start, target = map(int, input().split())
visited = set()
q = deque([[start, []]])
OPERATION = ['*','+','-','/']
while q:
    now, oper = q.popleft()
    if now == target:
        if not oper:
            print(0)
        else:
            print(''.join(oper))
        exit(0)
    for i in range(4):
        if i == 0:
            next = now*now
        if i == 1:
            next = now + now
        if i == 2:
            next = now - now
        if i == 3:
            if now == 0:
                next = 0
            else:
                next = now / now

        if next not in visited and int(1e9)+1 > next > 0:
            visited.add(next)
            q.append((next, oper+[OPERATION[i]]))
print(-1)
