
N = int(input())
data = list(map(int, input().split()))

start = 0
end = N - 1

result = -1
while start <= end:
    mid = (start+end)//2

    if data[mid] == mid:
        result = mid
        break
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1


print(result)