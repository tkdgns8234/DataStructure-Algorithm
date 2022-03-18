# if len(s) == 4 and len(s) == 6 in 연산으로 줄인것도 참신하다.
def solution(s):
    return str(s).isdigit() and len(s) in (4,6)