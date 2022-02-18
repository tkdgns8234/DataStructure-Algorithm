# 링크드 리스트를 직접구현할수도 있지만 더 간단한 방법이 있다
# 키포인트 = 커서를 기준으로 좌 우 리스트를 두 개 두는것 append pop 연산이 상수시간에 계산되기때문에 그걸 이용
# n = int(input())
#
# for _ in range(n):
#     pwd = list(input())
#     left = []
#     right = []
#     for i in pwd:
#         if i == '-':
#             if len(left):
#                 left.pop()
#         elif i == '>':
#             if len(right):
#                 left.append(right.pop())
#         elif i == '<':
#             if len(left):
#                 right.append(left.pop())
#         else:
#             left.append(i)
#
#     print("".join(left + list(reversed(right))))

# 문제2 요세푸스 문제
# 와 이거 생각보다 어려워서 당황했다
# 풀다말았어...
# 아래 코드는 일반적인 풀이
# !!!!양방향 큐 자료구조 이용하면 정말 쉽게 풀 수 있네!!!
# 맨 앞 원소를 m번째만큼 pop해서 append 하면 끝
# 풀이 링크 https://hongcoding.tistory.com/41

# n, m = map(int, input().split())
# data = [i for i in range(1, n + 1)]
# rs = []
# num = 0
# for i in range(n):
#     num += (m - 1)
#     if num >= len(data):
#         num = num % len(data)
#     rs.append(data.pop(num))
# print("<", ", ".join(map(str, rs)), ">", sep="")

