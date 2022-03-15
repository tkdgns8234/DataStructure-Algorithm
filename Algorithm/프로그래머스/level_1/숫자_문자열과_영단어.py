def solution(s):
    answer = s
    num_list = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
    for i, num in enumerate(num_list):
        answer = answer.replace(num, str(i))

    return int(answer)

# 다른 코드 참고해서 enummerate 로 변경했다.
