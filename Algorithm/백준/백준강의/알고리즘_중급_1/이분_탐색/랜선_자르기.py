# 파라메트릭 서치 문제 최적화 문제를 결정문제로

def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2

        cnt = 0
        for l in line:
            cnt += (l//mid)

        if cnt < N:
            end = mid - 1
        else:
            ans = max(ans, mid)
            start = mid + 1



K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
max_len = max(line)

ans = 0
binary_search(1, max_len)
print(ans)