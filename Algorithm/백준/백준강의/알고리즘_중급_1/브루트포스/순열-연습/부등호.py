import sys
from itertools import permutations
k = int(input())
oper = input().split()

min_val = sys.maxsize
max_val = -1
for numbers in permutations([i for i in range(10)], k+1):
    flag = True
    for i in range(len(numbers)-1):
        if oper[i] == '<':
            if numbers[i] >= numbers[i+1]:
                flag = False
                break
        else:
            if numbers[i] <= numbers[i+1]:
                flag = False
                break
    if flag:
        min_val = min(min_val, int(''.join(map(str, numbers))))
        max_val = max(max_val, int(''.join(map(str, numbers))))

print(str(max_val).rjust(k+1,'0'))
print(str(min_val).rjust(k+1,'0'))


# 다른 풀이
# 백트래킹 방식
# 처음 값이 최솟값이고 가장 마지막 값이 최댓값인것
# string 또한 관계연산이 가능하네 아마 ascii 값 기준으로 계산하는거같은데
# 신선하다.
num = int(input())
op = input().split()
check = [False] * 10
mx , mn = "",""
def poss(i,j,k): # 부등호 조건이  만족할 때만 작동
    if k == ">":
        return i>j
    else:
        return i<j


def recu(cnt, s):
    global mx,mn
    if cnt > num: #맨처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
    for i in range(10): #재귀 함수
        if check[i] == False:
            if cnt == 0 or poss(s[-1],str(i),op[cnt-1]):
                check[i] = True
                recu(cnt+1,s+str(i))
                check[i] = False

recu(0,"")
print(mx)
print(mn)