# 2^50 으로 시간초과일줄알았는데
# 한 위치에서 하나씩 빠지니까
# 그보다 적은거같다

T = list(input())
S = list(input())

def dfs(start):
    if len(start) == len(T):
        if start == T:
            print(1)
            exit(0)
        return

    if start[0] == 'B':
        dfs(start[:0:-1])
    if start[-1] == 'A':
        dfs(start[:-1])

dfs(S)
print(0)