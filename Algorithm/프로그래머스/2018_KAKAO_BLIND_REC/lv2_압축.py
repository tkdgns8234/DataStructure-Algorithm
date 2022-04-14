# 시뮬레이션 문제, 문제 그대로 작성했음
def solution(msg):
    answer = []
    msg = list(msg)
    dic = dict()
    dic_pos = 27 # 새로운 단어가 사전에 추가될 값

    # 길이가 1인 모든 단어 초기화
    for m in msg:
        idx = ord(m) - (ord('A') - 1)
        dic[m] = idx

    while True:
        # 2 사전에서 현재 입력과 일치하는 가장 긴 문자열을 찾는다.
        w = ''
        for i in range(1, len(msg)+1):
            key = "".join(msg[0:i])
            if dic.get(key, 'None') == 'None':
                break
            else:
                w = key
        # 3번 과정
        answer.append(dic[w])
        for _ in range(len(w)):
            msg.pop(0)
        # 4번 과정
        if msg:
            dic[w+msg[0]] = dic_pos
            dic_pos += 1
        else:
            break

    return answer


# 더 좋은 코드
# 개선된 점
# 1. dictionary 초기화 방법 기억하자
# 2. string 연산 잘 활용하자
# 3. dictionary.keys 활용

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer