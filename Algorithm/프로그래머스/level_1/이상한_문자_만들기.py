def solution(s):
    arr = s.split(' ')
    arr = list(map(list, arr))
    for i, word in enumerate(arr):
        for j in range(len(word)):
            if j % 2 == 0:
                arr[i][j] = arr[i][j].upper()
            else:
                arr[i][j] = arr[i][j].lower()
    return ' '.join(map("".join, arr))

solution("try hello world")