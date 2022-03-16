def solution(dartResult):
    l = []
    multiple = ['S','D','T']
    num = ''
    for i, word in enumerate(dartResult):
        if str(word).isnumeric():
            num += word
            if str(dartResult[i + 1]).isnumeric():
                continue
            else:
                l.append(int(num))
                num = ''
        elif word in multiple:
            l[-1] = l[-1] ** (multiple.index(word) + 1)
        elif word == '*':
            l[-1] *= 2
            if len(l) > 1:
                l[-2] *= 2
        elif word == '#':
            l[-1] = -l[-1]
    answer = sum(l)
    return answer

print(solution('1D2S#10S'))