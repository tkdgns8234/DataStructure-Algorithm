# 하노이타워의 결과를 출력
def hanoi_tower(num, start, by, end):
    if num == 1:
        print(start, end) # 데이터가 하나만 남은 경우 -> 목적지로 그냥 이동하면 됨
    else:
        hanoi_tower(num-1, start, end, by) # 마지막 데이터를 남기고 모두 2 구역으로 이동
        print(start, end) # 마지막 데이터를 3 구역(목적지) 로 이동
        hanoi_tower(num - 1, by, start, end) # 2구역에있는 n-1개의 데이터를 c 구역으로 이동


n = int(input())
print(2**n-1) # 하노이타워의 모든 경우의수 -> 2^n -1
if n <= 20:
    hanoi_tower(n, 1, 2, 3)