# 실패했던 코드;;;(수정 함)
# 다시풀자
# 아이디어를 떠올리는건 쉬운데 생각보다 구현이 쉽지 않다; 큰 코 다쳤다
# 일반적으로 생각하고, 구현하자
# python 에서 list slicing 할 때 특이한 점을 발견했다
# a = '1234' a[:100000] 해도 index 에러가 발생하지 않는다
# '1234'출력 됨 (알아서 최대 크기로 맞춰준다.)

def solution(s):
    answer = len(s)
    for jump in range(1, len(s)//2+1):
        prev = s[0:jump]
        words = ''
        count = 1
        for i in range(jump, len(s), jump):
            if prev == s[i:i+jump]:
                count += 1
            else:
                words += str(count) + prev if count > 1 else prev
                count = 1
                prev = s[i:i+jump]
        words += str(count) + prev if count > 1 else prev
        answer = min(answer, len(words))
    return answer
# solution('aabbaccc')