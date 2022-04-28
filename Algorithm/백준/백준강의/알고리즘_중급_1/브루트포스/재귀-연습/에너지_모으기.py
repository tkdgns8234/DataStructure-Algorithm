def btk(arr, total):
    global max_val
    if len(arr) == 2:
        max_val = max(max_val, total)
        return

    for i in range(1, len(arr)-1):
        temp = arr[i]
        arr.pop(i)
        btk(arr, total + arr[i-1] * arr[i])
        arr.insert(i, temp)

# 백트래킹 유형
N = int(input())
W = list(map(int, input().split()))

max_val = -1
btk(W, 0)
print(max_val)