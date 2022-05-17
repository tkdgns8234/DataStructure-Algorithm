# 파라메트릭 서치
def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2

        length = 0
        for w in wood[::-1]:
            l = w - mid
            if l > 0:
                length += l
                if length > M:
                    break
            else:
                break

        if length >= M:
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1


N, M = map(int, input().split())
wood = sorted(map(int, input().split()))
ans = 0
binary_search(0, wood[-1])
print(ans)