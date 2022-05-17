N = int(input())
data = list(map(int, input().split()))
# swap 횟수 출력
def merge_sort(arr):
    global swap_cnt
    # 재귀 탈출
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            swap_cnt += (len(left)-l)
            merged.append(right[r])
            r += 1
    merged+=left[l:]
    merged+=right[r:]
    return merged



swap_cnt = 0
merge_sort(data)
print(swap_cnt)


# 메모리 사용을 적게하는 코드
N = int(input())
data = list(map(int, input().split()))

def merge_sort(start, end):
    global swap_cnt
    # start < end 인 경우는 원소가 2개 이상인 경우
    # 원소가 1개로 나눠진 경우는 swap이 필요 없음 (1개인경우 start == end)
    if start < end:
        mid = (start + end)//2
        merge_sort(start, mid)
        merge_sort(mid+1, end)

        left = start
        right = mid+1

        merged = []
        while left <= mid and right <= end:
            if data[left] <= data[right]:
                merged.append(data[left])
                left += 1
            else:
                swap_cnt += (mid-left+1)
                merged.append(data[right])
                right += 1
        if left <= mid:
            merged += data[left:mid+1]
        if right <= end:
            merged += data[right:end+1]

        for i in range(len(merged)):
            data[start+i] = merged[i]


swap_cnt = 0
merge_sort(0, N-1)
print(swap_cnt)