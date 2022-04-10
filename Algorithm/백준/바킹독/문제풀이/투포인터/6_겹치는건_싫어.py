# 6. 겹치는 건 싫어
N, K = map(int, input().split())
data = list(map(int, input().split()))

dic = dict()

end = 0
ans = 0
for start in range(N):
    while end < N:
        if dic.get(data[end], 0) < K:
            dic[data[end]] = dic.get(data[end], 0) + 1
            end += 1
        else:
            break
    ans = max(ans, end - start)
    dic[data[start]] = dic.get(data[start], 0) - 1

print(ans)
