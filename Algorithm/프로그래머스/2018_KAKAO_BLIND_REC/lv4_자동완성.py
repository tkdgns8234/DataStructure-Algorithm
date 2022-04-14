# 정렬된 기준으로 앞 뒤 단어만 비교하면 된다
# 로직은 아래와 같다
# 1. 정렬
# 2. 이전, 다음 단어 기준 비교
# 2.1 단어 하나씩 같은지 비교하고
# 모두 같으면 단어 len 만큼 확인 필요
# 틀린게 생기면 틀린 부분까지 확인 필요 (이전, 다음단어의 틀린 위치의 최댓값만큼 확인해야함)

def get_diff_point(word, compare_list):
    # 이전 또는 다음 단어와 일치하는 갯수 return
    point = 0
    for c in compare_list:
        temp = 0
        for j in range(len(word)):
            if j < len(c):
                if word[j] == c[j]:
                    temp += 1
                else:
                    break
        point = max(point, temp)
    return point

def solution(words):
    words.sort()
    answer = 0

    for i in range(len(words)):
        word = words[i]

        if i == 0:
            point = get_diff_point(word, [words[i+1]])
        elif i == len(words)-1:
            point = get_diff_point(word, [words[i-1]])
        else:
            point = get_diff_point(word, [words[i+1], words[i-1]])

        if point == len(word):
            answer += len(word)
        else:
            answer += (point + 1)

    return answer