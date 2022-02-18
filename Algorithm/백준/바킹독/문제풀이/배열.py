# 1. 숫자의 개수
# num_cnt = [0] * 10
#
# rs = 1
# for _ in range(3):
#     rs *= int(input())
#
# while rs > 0:
#     position = rs % 10
#     num_cnt[position] += 1
#     rs //= 10
#
# for i in num_cnt:
#     print(i)

# 2. 방 번호
# import math
# arr = [0] * 10
# n = int(input())
#
# while n > 0:
#     index = n % 10
#     arr[index] += 1
#     n //= 10
#
# max_val = 0
# val_69 = 0
# for i in range(len(arr)):
#     if i == 6 or i == 9:
#         val_69 += arr[i]
#         continue
#     max_val = max(max_val, arr[i])
#
# val_69 = math.ceil(val_69/2)
# if max_val > val_69:
#     print(max_val)
# else:
#     print(val_69)

#3. 두 수의 합
# arr = [0] * 200_000_1
# n = int(input())
# data = list(map(int, input().split()))
# x = int(input())
#
# for i in data:
#     arr[i] += 1
#
# cnt = 0
# for i in data:
#         if x > i and arr[x-i] != 0:
#             cnt += 1
# print(cnt//2)

