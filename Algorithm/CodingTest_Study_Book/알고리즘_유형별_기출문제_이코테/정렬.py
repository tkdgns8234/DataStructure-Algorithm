# Q23 국영수
# 시간복잡도 O(nlogn)을 이용하면 해결 가능하다

# n = int(input())
#
# data = []
# for _ in range(n):
#     data.append(list(input().split()))
#
# data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
#
# for i in data:
#     print(i[0])

# Q24 안테나
# n = int(input())
#
# data = []
# data.append(map(int, input().split()))
#
# data.sort()
#
# print(data[(n-1)//2])

# Q25 실패율 대입
# 다시풀자
# 너무 알고리즘에 얽매여서 구현하지 말자..
# 그냥 구현방식으로도 충분히 해결 가능 지금은 오히려 더 복잡해지고있는거같아

# def fail(index, f):
#     sum = 0
#     for i in range(index, len(f)):
#         sum += f[i][0]
#     # 해당 stage 를 클리어한 사람이 없는경우
#     if sum == 0:
#         return 0
#     return f[index][0] / sum
#     # 실패율 계산
#
# def solution(N, stages):
#     answer = []
#     f = [[0, i] for i in range(N + 2)]
#     # 실패율, 인덱스 번호
#
#     # 실패율을 위해 계수정렬 형태로 값 대입
#     for stage in stages:
#         f[stage][0] += 1
#
#     # 실패율 대입
#     for i in range(1, N + 1):
#         f[i][0] = fail(i, f)
#
#     f.sort(key=lambda x: (-x[0], x[1]))
#
#     for i in range(len(f)):
#         idx = f[i][1]
#         if 0 < idx <= N:
#             answer.append(idx)
#     return answer

# Q26 카드 정렬하기
# heap 자료구조로 풀 수 있음

# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))
#
# data.sort()
#
# sum = 0
# start = data[0]
# for i in range(1, n):
#     sum += start + data[i]
#     start = start + data[i]
#
# print(sum)
