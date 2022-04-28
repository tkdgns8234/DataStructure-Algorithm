# comb 풀이
# 시간초과가 계속 발생해서 애먹었다;

from itertools import combinations
N, K = map(int, input().split())
words = [list(input()[4:-4]) for _ in range(N)]

if K < 5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)

p = ('a','c','n','i','t')
a_to_z = set([chr(i) for i in range(ord('a'), ord('z')+1)]) - set(p)


max_val = 0
for comb in combinations(a_to_z, K-5):
    comb = set(comb+p)
    cnt = 0
    for word in words:
        flag = True
        for i in word:
            if i not in comb:
                flag = False
                break
        if flag:
            cnt += 1
    max_val = max(max_val, cnt)
print(max_val)



# 백트래킹 풀이
# 내 풀이가 좀 더 직관적이고 쉬워보임

import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)
