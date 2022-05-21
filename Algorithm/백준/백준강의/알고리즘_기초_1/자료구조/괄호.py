T = int(input())

for _ in range(T):
    stack = []
    flag = False
    data = input()
    for i in data:
        if i == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                flag = True
                break
    if stack or flag:
        print('NO')
    else:
        print('YES')