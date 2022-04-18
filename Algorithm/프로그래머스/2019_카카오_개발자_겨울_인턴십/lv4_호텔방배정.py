# 이진 탐색으로 들어갈 수 있는 위치중 가장 왼쪽 위치를 찾는다
# set 에 들어가있는 위치를 다 넣자
# 실패
# 다시풀자
# def find_room(start, end, closed_room):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if mid in closed_room:
#
#
# def solution(k, room_number):
#     closed_room = set()
#     answer = []
#     for need in room_number:
#         if need not in closed_room:
#             answer.append(need)
#         else:
#             number = find_room(need+1, k, closed_room)
#             answer.append(number)
#
#     return answer

# 좋은 풀이
# 테크 풀이
# https://tech.kakao.com/2020/04/01/2019-internship-test/
# 하기 코드 블로그
# https://mungto.tistory.com/202
# Lv4 2019 겨울 인턴십
# 호텔 방 배정

# def solution(k, room_number):
#     answer = []
#     # 체크용 딕셔너리
#     room = {}
#     # 손님을 받으며 체크하자
#     for num in room_number:
#         # 딕셔너리에 확인 0이라면 배정이 안됬고, 다른값이 있다면 이미 배정되었다.
#         number = room.get(num, 0)
#         if number:
#             # 임시변수에 방번호를 넣어준다,
#             temp = [num]
#             # 반복문을 돌면서 빈방이 나올때까지 체크
#             while True:
#                 index = number
#                 # 이동했던 위치를 이용하여 다시 이동
#                 number = room.get(number, 0)
#                 # 방이 비어있다면 방을 할당
#                 if not number:
#                     # 정답에 추가해주고
#                     answer.append(index)
#                     # 딕셔너리에 값을 등록하고
#                     room[index] = index + 1
#                     # 이전에 거쳤던 방들도 바꿔준다.
#                     for i in temp:
#                         room[i] = index + 1
#                     break
#                 temp.append(number)
#         # 배정이 안되어있다면 결과추가하고 방배정 되었다고 딕셔너리에 표시
#         else:
#             answer.append(num)
#             room[num] = num + 1
#     return answer

# 다시 푼 버전
# def solution(k, room_number):
#     dic = dict()
#
#     answer = []
#     for num in room_number:
#         idx = dic.get(num, 0)
#         if idx == 0:
#             answer.append(num)
#             dic[num] = num+1
#         else:
#             temp = []
#             while True:
#                 temp.append(idx)
#                 v = dic.get(idx, 0)
#                 if v == 0:
#                     answer.append(idx)
#                     for i in temp:
#                         dic[i] = idx + 1
#                     break
#                 idx = v
#     return answer
#
# v = solution(10, [1,3,4,1,3,1]	)
# print(v)

# 다른 풀이
# def solution(k, room_number):
#     room_dic = {}
#     ret = []
#     for i in room_number:
#         n = i
#         visit = [n]
#         while n in room_dic:
#             n = room_dic[n]
#             visit.append(n)
#         ret.append(n)
#         for j in visit:
#             room_dic[j] = n+1
#     return ret
# v = solution(10, [1,3,4,1,3,1]	)
# print(v)