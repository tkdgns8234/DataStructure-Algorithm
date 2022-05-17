# 계수 정렬
N = int(input())
arr = [0]*(2_000_001)
for _ in range(N):
    num = int(input())
    arr[num+1000000] = 1

for i in range(len(arr)):
    if arr[i]:
        print(i-1000000)



# 퀵 정렬
# 파이썬스럽게 풀어봤는데 메모리 초과 발생..
# inplace 방식으로 풀이해야겠다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


N = int(input())
data = []
for i in range(N):
    num = int(input())
    data.append(num)
rs = quick_sort(data)
for i in rs:
    print(i)



import sys

sys.setrecursionlimit(int(10000))
# 퀵 정렬 inplace sort 방식
# 거의 정렬된 경우 O(n^2) 소요되서 시간초과가 발생하나보다. 여기까지

def quick_sort(start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1

        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[right], data[left] = data[left], data[right]

    quick_sort(start, right-1)
    quick_sort(right+1, end)



N = int(input())
data = []
for i in range(N):
    num = int(input())
    data.append(num)
quick_sort(0, N-1)
for i in data:
    print(i)