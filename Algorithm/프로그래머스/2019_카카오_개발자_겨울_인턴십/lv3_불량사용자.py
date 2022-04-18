# 불량 사용자 목록에 매칭되는 불량 사용자를 찾고
# 중복으로 뽑는 경우를 제외한 모든 경우를 출력한다

# def is_matched(uid, bid):
#     if len(uid) != len(bid): return False
#     result = True
#     for i, word in enumerate(bid):
#         if bid[i] == '*':
#             continue
#         else:
#             if bid[i] != uid[i]:
#                 result = False
#     return result
#
# def btk(ban_list, depth, l, answer):
#     if depth == len(ban_list):
#         answer.add(tuple(sorted(l)))
#         return
#     for bid in ban_list[depth]:
#         if bid not in l:
#             l.append(bid)
#             btk(ban_list, depth+1, l, answer)
#             l.remove(bid)
#
# def solution(user_id, banned_id):
#     ban_list = [[] for _ in range(len(banned_id))]
#     for idx, ban in enumerate(banned_id):
#         for uid in user_id:
#             if is_matched(uid, ban):
#                 ban_list[idx].append(uid)
#
#     answer = set()
#     btk(ban_list, 0, [], answer)
#     print(answer)
#     return len(answer)
#
# v = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"])
# print(v)
#
#
# # 백트래킹이 아니라 product를 사용한 더 쉬운 풀이
# # 나머지 로직은 동일하다
# from itertools import product
#
#
# def is_matched(uid, bid):
#     if len(uid) != len(bid): return False
#     result = True
#     for i, word in enumerate(bid):
#         if bid[i] == '*':
#             continue
#         else:
#             if bid[i] != uid[i]:
#                 result = False
#     return result
#
# def solution(user_id, banned_id):
#     ban_list = [[] for _ in range(len(banned_id))]
#     for idx, ban in enumerate(banned_id):
#         for uid in user_id:
#             if is_matched(uid, ban):
#                 ban_list[idx].append(uid)
#
#     answer = set()
#     ban_list = list(product(*ban_list))
#     for r in ban_list:
#         if len(set(r)) == len(banned_id):
#             answer.add("".join(sorted(set(r))))
#     return len(answer)
#
# v = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"])
# print(v)