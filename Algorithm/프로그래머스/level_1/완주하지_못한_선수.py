def solution(participant, completion):
    answer = ''
    dic = {name : 0 for name in participant}
    for name in completion:
        dic[name] += 1
    for i in participant:
        dic[i] -= 1
    for i in participant:
        if dic[i] == -1 or dic[i] >= 1:
            answer = i
            break
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# # 좋은풀이 1
# # counter 라이브러리를 사용하면, dict 형태로 그 인수의 갯수를 return 하고, - + 집합 연산을 사용할 수 있다.
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(answer)
#     return list(answer.keys())[0]
#
# # 좋은풀이 2
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer