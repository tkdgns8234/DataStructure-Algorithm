# 아래 코드 90점짜리, 효율성 테스트 일부 만족 못한다

# 생각보다 쉬운데?
# bisect left, right 찾은 다음
# 단어 갯수 확인하면서 count
# ???word 인 경우 반대로 정렬해서 찾자
import bisect

def match_count(words, query):
    start = bisect.bisect_left(words, query.replace('?','a'))
    end = bisect.bisect_right(words, query.replace('?','z'))

    count = 0
    q_len = len(query)
    for i in range(start, end):
        if len(words[i]) == q_len:
            count += 1
    return count


def solution(words, queries):
    words = sorted(words)
    reverse_words = sorted(["".join(reversed(i)) for i in words])

    answer = []
    for query in queries:
        if query[0] == '?':
            c = match_count(reverse_words, "".join(reversed(query)))
        else:
            c = match_count(words, query)
        answer.append(c)
    return answer

v= solution(["froa","froaz","frozze"], ["fro??",'????ze'])
print(v)


# 이코테 풀이
# from bisect import bisect_left, bisect_right
#
# def count_by_range(array, left_val, right_val):
#     left_idx = bisect_left(array, left_val)
#     right_idx = bisect_right(array, right_val)
#     return right_idx - left_idx
#
# def solution(words, queries):
#     answer = [0] * len(queries)
#     asc_words = [[] for _ in range(100001)]
#     desc_words = [[] for _ in range(100001)]
#     # 단어 길이를 인덱스로하는 2차원 리스트에 단어 길이별로 담기
#     for word in words:
#         asc_words[len(word)].append(word)
#         desc_words[len(word)].append(word[::-1])
#
#     # 단어 길이별로 단어들 정렬
#     for i in range(100001):
#         asc_words[i].sort()
#         desc_words[i].sort()
#
#     # 쿼리하나씩 받아서 처리
#     for i in range(len(queries)):
#         q = queries[i]
#         if q[0] != '?':
#             answer[i] = count_by_range(asc_words[len(q)], q.replace('?', 'a'),
#                                        q.replace('?', 'z'))
#         else:
#             q = q[::-1]
#             answer[i] = count_by_range(desc_words[len(q)], q.replace('?', 'a'),
#                                        q.replace('?', 'z'))
#
#     return answer