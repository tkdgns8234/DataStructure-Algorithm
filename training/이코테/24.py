N = int(input())
data = map(int, input().split())


def binary_search(start, end):
    global result
    mid = (start + end) // 2

    dist = 0
    for d in data:
        dist += abs(d - mid)

    result = min(result, dist)


result = 0
binary_search(0, 100_000)
