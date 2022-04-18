# 시뮬
def solution(new_id):
    answer = ''
    # 1단계
    temp = str(new_id).lower()
    # 2단계
    for word in temp:
        if word.islower() or word.isnumeric() \
                or word == '-' or word == '_' or word == '.':
            answer += word
    # 3단계
    temp = ''
    count = 0
    for i in answer:
        if i == '.':
            count += 1
        else:
            if count >= 1:
                temp += '.'
                count = 0
            temp += i
    answer = temp
    # 4단계
    answer = answer.strip('.')
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = answer.strip('.')
    # 7단계
    while len(answer) < 3:
        answer += answer[len(answer)-1]

    return answer