# 일반 리스트로 문제를 해결하려 하는경우
# 삽입, 삭제에 O(N) 이 들기떄문에
# 링크드 리스트를 떠올렸으나, 파이썬이라 패스
# 두개의 스택을 사용하면 링크드 리스트와 동일한 O(N)시간복잡도로 해결할 수 있다.

s1 = list(input())
s2 = []

for _ in range(int(input())):
    oper = input().split()
    if oper[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif oper[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif oper[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(oper[1])

print(''.join(s1 + list(reversed(s2))))