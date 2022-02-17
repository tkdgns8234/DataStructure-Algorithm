# 해시 자료구조는 키에 대응되는 값을 저장하는 자료구조
# 키 값을 적당히 배열의 인덱스로 설정하여 테이블로 데이터를 관리
# 해시함수: 임의의 길이의 데이터를 고정된 길이의 데이터로 대응시키는 함수
# 삽입, 삭제, 탐색 등의 연산이 모두 O(1)

# 서로 다른 키가 같은 값을 가지는 경우 충돌이 발생했다고 표현함
# 충돌 회피를 위해 아래 기법을 사용
# 1. chaining : 각 인덱스마다 연결리스트로 데이터들을 관리
# 중복된 값이 많을수록 느려지는 단점 연결리스트기떄문에 O(중복된 데이터의 수)
# 2. Open Addressing
# 충돌 발생 시, 인덱스값을 오른쪽으로 한칸씩 이동하는 방식
# 데이터 삭제 시, dummy 값(쓰레기값)을 추가 해 놓아야만한다
# Linear Probing
# 충돌 발생 시 , 한칸씩 이동
# Quadratic Probing
# 충돌 발생 시, 첫 위치를 기준으로 제곱수만큼 이동 1, 3, 9, ~
# double hashing
# 충돌 발생 시, 몇칸을 점프할지 새로운 해시함수로 계산

# 문제1 회사에 있는 사람
# 이분탐색을 이용해 풀 수 있지만 해시를 이용하면 정말 쉽다
# 파이썬은 딕셔너리라는 이름으로 해시가 구현되어있다
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = {}
# for _ in range(n):
#     name, status = input().split()
#     if status == 'enter':
#         data[name] = status
#     else:
#         if name in data:
#             del data[name]
#
# for i in sorted(data, reverse=True):
#     print(i)