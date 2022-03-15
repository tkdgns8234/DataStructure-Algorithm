# 구현유형인듯
# dict 를 사용하여 참조하는데 걸리는 시간복잡도를 최소화
# O(report*2 + 2rep)

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dic = dict()

    for r in set(report):
        _, b = r.split()
        dic[b] = dic.get(b, 0) + 1

    for r in set(report):
        a, b = r.split()
        if dic[b] >= k:
            answer[id_list.index(a)] += 1

    print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
