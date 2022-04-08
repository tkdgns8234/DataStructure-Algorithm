# 12. 스타트와 링크
# 시간복잡도 20C10 * 10 -> 간신히 될거같은데
# 블로그 참조, 다시풀기
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]
data_total = sum(map(sum, data))

def btk(comb, depth, total):
    global result

    if depth == n//2:
        result = min(result, abs(total - abs(data_total - total)))
        return

    for k in range(n//2):
        if k == depth:
            continue
        total = total + data[comb[depth]][comb[k]]
    btk(comb, depth + 1, total)


result = int(1e9)
for comb in combinations(range(n), n//2):
    btk(comb, 0, 0)
    if result == 0:
        print(result)
        break
print(result)


# 블로그참조
# 정말 쉽구나..
# 다시풀자
# 궁금하니 bfs 풀이도 한번 보자
# from itertools import combinations as c
#
# n = int(input())
# array = [i for i in range(n)]
# matrix = []
# for _ in range(n):
#     matrix.append((list(map(int, input().split()))))
# result = int(1e9)
# for r1 in c(array, n//2):
#     start, link = 0, 0
#     r2 = list(set(array) - set(r1))
#     for r in c(r1, 2):
#         start += matrix[r[0]][r[1]]
#         start += matrix[r[1]][r[0]]
#     for r in c(r2, 2):
#         link += matrix[r[0]][r[1]]
#         link += matrix[r[1]][r[0]]
#     result = min(result, abs(start-link))
# print(result)
