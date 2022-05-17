import sys

input = sys.stdin.readline
N = int(input())
counting_sort = [0]*10001
for _ in range(N):
    num = int(input())
    counting_sort[num] += 1

for i in range(10001):
    n = counting_sort[i]
    for _ in range(n):
        print(i)




