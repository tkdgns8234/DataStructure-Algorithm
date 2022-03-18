def solution(s):
    s = str(s).lower()
    return True if list(s).count('p') == list(s).count('y') else False