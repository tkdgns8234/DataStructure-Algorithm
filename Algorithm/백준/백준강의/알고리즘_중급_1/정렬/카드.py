import sys
from collections import defaultdict

dict = defaultdict(int)
N = int(input())
for _ in range(N):
    num = int(input())
    dict[num] += 1

max_val = -sys.maxsize
ans = -1
for i in dict:
    if dict[i] > max_val:
        max_val = dict[i]
        ans = i
    elif dict[i] == max_val:
        ans = min(i, ans)
print(ans)