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
def solution(s):
    result = []
    for i in range(2, len(s)):
        start = 0
        for j in s[start::2]:
            pass



    answer = 0
    return answer