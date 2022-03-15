def solution(lottos, win_nums):
    answer = [0, 0]
    zero_count = list(lottos).count(0)

    count = 0
    for i in win_nums:
        if i in lottos:
            count += 1

    rank = 7 - count # 7은 기준 번호
    answer[0] = 6 if rank - zero_count > 5 else rank - zero_count
    answer[1] = 6 if rank > 5 else rank
    return answer

# 좋은풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]