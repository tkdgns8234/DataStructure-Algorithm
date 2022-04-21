# default dict 사용버전
from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    for i in completion:
        dic[i] += 1
    for i in participant:
        dic[i] -= 1
        if dic[i] < 0:
            return i

# default dict 사용x
def solution(participant, completion):
    dic = dict()
    for i in completion:
        dic[i] = dic.get(i, 0) + 1
    for j in participant:
        dic[j] = dic.get(j, 0) - 1
        if dic[j] < 0:
            return j