# 10. 연산자 끼워넣기
# 백트래킹?
# n == 11 개면  연산자 모든 경우의수 10개
# 10개 중 10개 놓는 모든 경우의 수 10P10 /6 최소한 중복되는수
# 성공!

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split()))
op = list(map(int, input().rstrip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈

def btk(depth, total, index):
    global max_val, min_val

    if depth == n - 1:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                temp = total + num_list[index]
            if i == 1:
                temp = total - num_list[index]
            if i == 2:
                temp = total * num_list[index]
            if i == 3:
                if total < 0:
                    temp = -(abs(total) // num_list[index])
                else:
                    temp = total // num_list[index]
            btk(depth + 1, temp, index + 1)
            op[i] += 1


min_val = int(1e9)+1
max_val = int(-1e9)-1
btk(0, num_list[0], 1)
print(max_val)
print(min_val)
