# 그리디 어렵구먼..
# 실패
# S를 T로 만드는게 아니라
# 거꾸로 생각하면 훨씬 쉽다
# T를 S로 만들 수 있는지 확인하면 된다.
# 1. 문자열의 뒤에서 A를 제거한다
# 2. 문자열의 뒤에서 B를 제거하고 뒤집는다.

# '문자열을 뒤집는다' 라는 표현을 A -> B   B->A 로 이해했다;
# 말 그대로 문자열을 앞/뒤로 뒤집는거엿어

S = list(input())
T = list(input())

for i in range(len(T)-len(S)):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        # T = ['A' if i == 'B' else 'B' for i in T]
        T.pop()
        T.reverse()

if T == S:
    print(1)
else:
    print(0)