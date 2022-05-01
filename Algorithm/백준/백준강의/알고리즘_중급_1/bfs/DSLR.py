# bfs + 시뮬레이션 유형인데
# 계속 메모리 초과가 발생한다
# q 의 갯수가 많아서인지, oper 의 길이때문인지
# visit 처리를 안했구나;;;;;
# 다시풀어보자

# from collections import deque
#
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     visited = [False] * 10001
#     q = deque()
#     q.append((A, ''))
#     while q:
#         now, oper = q.popleft()
#         if now == B:
#             print(oper)
#             break
#
#         #1. D 연산 수행
#         n_now = now*2 % 10000 if now*2 > 9999 else now*2
#         if not visited[n_now]:
#             q.append((n_now, oper+'D'))
#             visited[n_now] = True
#         #2. S연산 수행
#         n_now = 9999 if now == 0 else now - 1
#         if not visited[n_now]:
#             q.append((n_now, oper+'S'))
#             visited[n_now] = True
#         #3. L연산 수행
#         n_now = list(str(now).rjust(4, '0'))
#         temp = n_now.pop(0)
#         n_now.append(temp)
#         n_now = int(''.join(n_now))
#         if not visited[n_now]:
#             q.append((n_now, oper+'L'))
#             visited[n_now] = True
#         #4. R연산 수행
#         n_now = list(str(now).rjust(4, '0'))
#         temp = n_now.pop()
#         n_now.insert(0, temp)
#         n_now = int(''.join(n_now))
#         if not visited[n_now]:
#             q.append((n_now, oper+'R'))
#             visited[n_now] = True
#

# 1시간 넘게 소요됐다.
# 쉬운 문제인데 실수를 너무 많이했다..
# 2번내용은 문제 자체가 너무 애매하게 설명되어있는 느낌이야;
# 삽질
# 1. 실수로 visited 처리를 안해서 메모리 초과가 계속 났다.
# 2. 123의 경우 L 연산을 하면 123 1230이 된다.   앞에 0이 있는것처럼 처리해야한다
# 3. L, R을 처리할때 문자열로 치환해서 계산하는 경우 시간초과가 발생한다
# -> 수학 연산으로 풀이해야한다
# 4. D연산에서 실수했다.
# 전: n_now = now % 10000 if now*2 > 9999 else now*2
# 후: n_now = (now*2) % 10000 if now*2 > 9999 else now*2

from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10001
    q = deque()
    q.append((A, ''))
    while q:
        now, oper = q.popleft()
        if now == B:
            print(oper)
            break

        #1. D 연산 수행
        n_now = (now*2) % 10000 if now*2 > 9999 else now*2
        if not visited[n_now]:
            q.append((n_now, oper+'D'))
            visited[n_now] = True
        #2. S연산 수행
        n_now = 9999 if now == 0 else now - 1
        if not visited[n_now]:
            q.append((n_now, oper+'S'))
            visited[n_now] = True
        #3. L연산 수행
        n_now = ((now//1000) + (now%1000)*10)
        if not visited[n_now]:
            q.append((n_now, oper+'L'))
            visited[n_now] = True
        #4. R연산 수행
        n_now = ((now%10)*1000) + (now//10)
        if not visited[n_now]:
            q.append((n_now, oper+'R'))
            visited[n_now] = True