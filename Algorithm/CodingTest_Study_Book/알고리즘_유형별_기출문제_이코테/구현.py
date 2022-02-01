# Q07 럭키 스트레이트

# n = list(map(int, input()))
# print(n)
# half = len(n) // 2
#
# left = n[0:half]
# right = n[half:]
#
# if sum(left) == sum(right):
#     print('LUCKY')
# else:
#     print('READY')

# Q08 문자열 재정렬
# s = input()
# str_list = []
# result = 0
# for i in s:
#     if i.isalpha():
#         str_list.append(i)
#     else:
#         result += int(i)
#
# str_list.sort()
#
# if result != 0:
#     str_list.append(str(result))
#
# print(''.join(str_list))

# Q09 문자열 압축
# def solution(s):
#     answer = len(s)
#
#     for step in range(1, len(s)//2+1):
#         compressed = ""
#         prev = s[0:step]
#         count = 1
#
#         for j in range(step, len(s), step):
#             if prev == s[j:j+step]:
#                 count+=1
#             else:
#                 compressed += str(count) + prev if count>=2 else prev
#                 prev = s[j:j+step]
#                 count=1
#         compressed += str(count)+prev if count>=2 else prev
#         print(compressed)
#         answer = min(answer, len(compressed))
#     return answer
# s= input()
# print(solution(s))