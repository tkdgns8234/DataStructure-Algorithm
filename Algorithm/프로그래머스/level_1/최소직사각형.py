def solution(sizes):
    return max(map(max, sizes)) * max(map(min, sizes))