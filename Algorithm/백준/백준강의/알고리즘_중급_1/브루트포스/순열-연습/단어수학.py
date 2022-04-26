# from itertools import permutations
#
# def add(dic):
#     ret_val = 0
#     for word in words:
#         temp = ''
#         for i in word:
#             temp += str(dic[i])
#         ret_val += int(temp)
#     return ret_val
#
# def solve():
#     word_list = set()
#     for word in words:
#         for i in word:
#             word_list.add(i)
#     word_list = list(word_list)
#     dic = dict()
#     max_val = 0
#     test = 0
#     for numbers in permutations([i for i in range(9, 9-len(word_list), -1)], len(word_list)):
#         for i in range(len(word_list)):
#             dic[word_list[i]] = numbers[i]
#         max_val = max(max_val, add(dic))
#         test += 1
#     print(max_val)
#
# n = int(input())
# words = [input() for _ in range(n)]
# solve()

# 일반적인 브루트 포스 알고리즘으로는 통과할 수 없다
# 이 문제는 그리디 알고리즘에 해당한다
# 그리디 알고리즘 중 꽤 까다로운 편에 속한다
# 참조: https://hongcoding.tistory.com/76

# 문제 해결 아이디어는 자릿수가 가장 큰 값부터 9--로 치환하는것

# 각 단어의 위치를 표현하는 숫자를 dictionary에 저장한다
# ex) ababa
# dic[a] = 10101
# dic[b] = 1010
# 딕셔너리의 value를 가장 큰 순서대로 나열하고
# 차례대로 9부터 0까지 곱하여 정답을 출력한다
from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

dic = defaultdict(int)
for word in words:
    temp = set(word)
    for t in temp:
        word_val = int(''.join(map(str, [1 if i == t else 0 for i in word])))
        dic[t] += word_val

ans_list = sorted([dic[key] for key in dic], reverse=True)
ans = sum([ans_list[i] * (9-i) for i in range(len(ans_list))])
print(ans)