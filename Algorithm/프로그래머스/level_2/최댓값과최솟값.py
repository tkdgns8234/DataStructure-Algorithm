def solution(s):
    s = sorted(map(int, s.split()))
    answer = f'{s[0]} {s[-1]}'
    return answer

v = solution("1  2 3 4")
print(v)