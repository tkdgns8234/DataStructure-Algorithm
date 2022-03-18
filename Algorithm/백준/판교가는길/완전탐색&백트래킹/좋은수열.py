
def confirm(arr):
    length = len(arr)
    for step in range(1, length//2 + 1):
        if arr[-step:] == arr[-(step*2): -step]:
            return False
        # for i in range(step, length-step+1):
        #     prev = arr[i-step:i]
        #     if arr[i:i+step] == prev:
        #         return False
    return True

def btk(depth, arr):
    if depth == N:
        print(int("".join(arr)))
        exit(0)

    for i in range(1, 4):
        arr.append(f"{i}")
        if confirm(arr): # 인접 동일수열이 아니면
            btk(depth + 1, arr)
            arr.pop()
        else:
            arr.pop()
            continue

N = int(input())
num_arr = []
btk(0, num_arr)