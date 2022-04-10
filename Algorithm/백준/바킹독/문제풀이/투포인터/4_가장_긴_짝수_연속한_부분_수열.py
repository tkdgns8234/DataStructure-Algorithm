# 4. 가장 긴 짝수 연속한 부분 수열
N, M = map(int, input().split())
data = list(map(int, input().split()))

pass_ = M
end = -1
ans = 0

for start in range(N):
    while end < N - 1:
        if data[end + 1] % 2 == 0:
            end += 1
        else:
            if pass_ > 0:
                end += 1
                pass_ -= 1
            else:
                break
    ans = max(ans, (end - start + 1) - (M-pass_))
    if data[start] % 2 != 0:
        pass_ += 1

print(ans)
