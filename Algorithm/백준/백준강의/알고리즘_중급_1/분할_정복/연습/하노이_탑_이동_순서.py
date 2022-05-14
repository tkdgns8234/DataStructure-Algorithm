# https://youtu.be/FYCGV6F1NuY

# 1개일땐 1에서 3번 기둥으로 옮긴다
#  1, 2, 3 기둥이 있을 때 1개의 원반을 제외한 나머지 원반을 2번 기둥으로 옮긴다 (3을 보조로)
#  나머지 1번기둥을 3번기둥으로 옮긴다
# 나머지 2번 기둥을 1번기둥을 보조로 해서 3번기둥으로 옮긴다

# 코드
# def hanoi(원반갯수, 시작, 목표, 보조):
#    if 원반갯수 == 1:
#        print(시작 -> 목표)
#        return
#    hanoi(n-1, 시작, 보조, 목표)
#    print(시작 -> 목표)
#    hanoi(n-1, 보조, 목표, 시작)



# 사실 하노이탑 최소이동횟수: 2**n - 1

def hanoi(num, start, target, sub):
    global rs
    if num == 1:
        rs.append([start, target])
        return
    hanoi(num - 1, start, sub, target)
    rs.append([start, target])
    hanoi(num - 1, sub, target, start)
N = int(input())
rs = []
hanoi(N, 1, 3, 2)
print(len(rs))
for a, b in rs:
    print(a, b, sep=' ')
