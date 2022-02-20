# 1. 제로
# k = int(input())
# stack = []
#
# for i in range(k):
#     num = int(input())
#     if num == 0:
#         stack.pop()
#     else:
#         stack.append(num)
#
# print(sum(stack))

# 2. 스택 수열
# n = int(input())
# stack = []
# now = 0
# rs = []
# for i in range(n):
#     target = int(input())
#
#     while now < target:
#         now += 1
#         stack.append(now)
#         rs.append("+")
#
#     if stack[-1] == target:
#         stack.pop()
#         rs.append("-")
#     else:
#         print("NO")
#         exit(0)
#
# print("\n".join(rs))

# 3. 탑
# 중복 for문 사용시 문제해결불가
# 스택으로 최적화 O(N)으로 문제해결
# n = int(input())
# tower = list(map(int, input().split()))
#
# stack = [(0, tower[0])]
# rs = [0]
#
# for i in range(1, n):
#     while stack:
#         if stack[-1][1] < tower[i]:
#             stack.pop()
#         else:
#             rs.append(stack[-1][0] + 1)
#             break
#     if not stack:
#         rs.append(0)
#     stack.append((i, tower[i]))
#
# print(" ".join(map(str, rs)))

# 4 옥상 정원 꾸미기
# 이것도 스택을 통한 최적화
# 스택엔 빌딩 높이의 최댓값을 저장해놓고
# 스택과 빌딩의 인덱스값을 비교해서 그 사이 빌딩의 갯수를 구하도록 구현
# 뒤쪽부터 관찰 가능한 높이에대해 확인
# n = int(input())
# buildings = [int(input()) for i in range(n)]
# stack = [(n-1, buildings[-1])] # index, val
#
# count = 0
# for i in range(n-2, -1, -1):
#     while stack:
#         if stack[-1][1] < buildings[i]: # 현재 스택에 담긴것보다 빌딩이 큰 경우 스택.pop후 빌딩 삽입, 거리 계산
#             stack.pop()
#         else:
#             break
#     if not stack: # 스택이 빈 경우 모두 관찰 가능
#         count += (n - i - 1)  # 현재 인덱스부터 오른쪽 끝까지 모두 관찰 가능
#     else:
#         count += (stack[-1][0] - i - 1) # 스택 인덱스 - 현재인덱스 로 두 빌딩 사이의 건물 수를 더함
#     stack.append((i, buildings[i]))
# print(count)