# 이미 푼 문제
# 해결 방법만 떠올리고 skip
# ---- 해결 방법 ----
# combination 방식으로 출력
# 출력 시, 정렬 필요해보임 -> 자동으로 정렬되어서 값이 return 되는구나

# 백트래킹으로 출력해도 된다.
# 백트래킹의 경우
# 각 원소 visit 체크
# 반복문 start index 원소로 넘기는게 필요해보임
# ---- 해결 방법 ----

# 이전 풀이
def btk(depth, arr, start):
    global visited
    if depth == 6:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, K):
        if not visited[i]:
            visited[i] = True
            arr.append(S[i])
            btk(depth + 1, arr, i+1)
            arr.pop()
            visited[i] = False

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    K, S = temp[0], temp[1:]
    visited = [False] * (K+1)
    arr = []
    btk(0, arr,0)
    print()


# 다른 사람의 combination 이용 코드
from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    s = list(combinations(s, 6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()