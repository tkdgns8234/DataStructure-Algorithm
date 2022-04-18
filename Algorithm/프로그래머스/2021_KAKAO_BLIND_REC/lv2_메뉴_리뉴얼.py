# 너무 오래걸렸다..
# 문제를 이해하는데 너무 오래걸렸어
# 코드 자체도 생각이 정리되지 않은 상태에서 접근하니
# 지저분하고, 다른 사람에 비해 특이하게 짰다

# 각 단품메뉴를 course 배열 갯수만큼 골랐을 때
# 최대로 선택받은 메뉴를 출력하는 문제다
# 코드도 너무 길어
# 아래 코드 부분 개선했다.
# rs = [v for c, v in menu if c >= 2 and c == menu[0][0]]

# 아래 좋은 풀이 있으니 보자

from itertools import combinations
def order_count(menu, orders):
    c = 0
    for order in orders:
        flag = True
        for m in menu:
            if not m in order:
                flag = False
        if flag:
            c += 1
    return c


def solution(orders, course):
    course_menus = [set() for _ in range(11)]

    for order in orders:
        for i in course:
            for menu in list(combinations(order, i)):
                menu = "".join(sorted(menu))
                count = order_count(menu, orders)
                course_menus[i].add((count, menu))

    answer = []
    for menu in course_menus:
        if len(menu) == 0:
            continue
        # 수량이 많은순 정렬
        menu = sorted(menu, key=lambda x: x[0], reverse=True)
        rs = [v for c, v in menu if c >= 2 and c == menu[0][0]]
        answer += rs

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))


# 좋은 코드
# 위 코드 풀면서 딕셔너리로 풀어야겠다는 생각을 하긴 했다
# 물론 set 로 넘어갔지만;
# 딕셔너리로 풀 때, collections 라이브러리의 counter 를 잘 사용하면 좋다는걸 알고있자

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


# 좋은 코드
# import collections
# import itertools
#
# def solution(orders, course):
#     result = []
#
#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)
#
#         most_ordered = collections.Counter(order_combinations).most_common()
#         print('m=',most_ordered)
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
#
#     return [ ''.join(v) for v in sorted(result) ]
#
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))