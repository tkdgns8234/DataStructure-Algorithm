def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])

    return answer