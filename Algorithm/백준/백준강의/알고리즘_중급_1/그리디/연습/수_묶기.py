# 이전에 풀었던 문제였기에 쉽게 풀 수 있었다.
# 양수인경우 큰수끼리 곱해야하고
# 음수인경우 작은수끼리 곱해야 최댓값이 나온다
# 0인경우 양수와곱하면 크기가 작아지므로 음수에 포함시킨다.
# 1인경우 더하는게 가장 크므로 1의 갯수를 따로 저장해둔다
N = int(input())
minus = []
plus = []
one_cnt = 0
for _ in range(N):
    num = int(input())
    if num <= 0:
        minus.append(num)
    elif num == 1:
        one_cnt += 1
    else:
        plus.append(num)
minus.sort()
plus.sort(reverse=True)

def solve(arr):
    sum_ = 0
    for i in range(0, len(arr), 2):
        if len(arr)-1 == i:
            sum_ += arr[i]
        else:
            sum_ += (arr[i]*arr[i+1])
    return sum_

m_sum = solve(minus)
p_sum = solve(plus)
print(m_sum+p_sum+one_cnt)