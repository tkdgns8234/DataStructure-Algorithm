# 실패
# 어렵다
# 이분탐색인건 알았는데
# 값을 어떻게 찾아가야할지 정하지 못했다

# 이분 탐색으로 모든 아이들이 탈 수 있는 가장 작은 시간(t)을 구하고
# 그 시간 직전 시간(t-1)으로 이동하여
# 직전 시간(t-1)의 탑승 수를 구하고

# 놀이기구마다 t 시간에 탑승한 경우
# 탑승객을 하나씩 증가시켜
# 마지막 사람이 탑승한 놀이기구를 찾는다
# 참고: https://jjangsungwon.tistory.com/96
# 나중에 다시 풀자;

import sys

N, M = map(int, input().split())
time = list(map(int, input().split()))
t = int(sys.maxsize)
if N < M:
    print(N)
else:
    start, end = 0, 60_000_000_000
    while start<=end:
        mid = (start+end)//2

        cnt = M
        for i in range(M):
            # 이부분, 0초일때도 탑승할것으로 칠건지, 아닌지 너무 애매하다고 생각했다.
            cnt += (mid // time[i])

        if cnt < N:
            start = mid + 1
        else:
            t = min(t, mid)
            end = mid - 1
    cnt = M
    for i in range(M):
        cnt += (t-1)//time[i]

    for i in range(M):
        if t % time[i] == 0:
            cnt += 1
        if cnt == N:
            print(i+1)
            break