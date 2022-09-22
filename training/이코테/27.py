# import bisect
#
# N, X = map(int, input().split())
# data = list(map(int, input().split()))
#
# left = bisect.bisect_left(data, X)
# right = bisect.bisect_right(data, X)
#
# print(-1 if left == right else right - left)


def binary_search_start(start, end):
    rest_val = 0
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == Target and (data[mid-1] == 0 or data[mid - 1] < Target):
            return mid

        if data[mid] < Target:
            start = mid + 1
        else:
            end = mid - 1
            rest_val = mid

    return rest_val


def binary_search_end(start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == Target and (mid == N-1 or data[mid + 1] > Target):
            return mid

        if data[mid] <= Target:
            start = mid + 1
        else:
            end = mid - 1


N, Target = map(int, input().split())
data = list(map(int, input().split()))

start = binary_search_start(0, len(data) - 1)
end = binary_search_end(0, len(data) - 1)
print(-1 if start == 0 else end - start + 1)