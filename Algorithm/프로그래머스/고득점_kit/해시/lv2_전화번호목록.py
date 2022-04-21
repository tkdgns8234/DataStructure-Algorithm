# 카카오 Blind 기출문제에서 유사한 유형이 있었다.
# 완전탐색(브루트포스) 유형으로 해결 할 경우 O(n^2)시간이 소요되어 시간초과가 발생한다
# nlogn 으로 해결해도 시간 내에 가능한데, 해당 풀이는 떠오르지 않았다
# 전화번호부의 모든 전화번호들을 앞에서부터 1~전화번호 길이 갯수만큼 매번 자르면서
# dictionary에 미리 저장한다 (미리 계산해놓는 prefixsum 과 유사한 방식으로 구현)
# -> dictioanry에 해당 값이 2개 이상 존재하는지 확인(자기자신포함)
# 메모리 20mb로 그렇게 크지 않다

from collections import defaultdict
def solution(phone_book):
    dic = defaultdict(int)
    for number in phone_book:
        for i in range(len(number)):
            key = number[:i+1]
            dic[key] += 1

    for number in phone_book:
        if dic[number] > 1:
            return False
    return True

# 다른 해시 풀이
# 메모리는 훨씬 덜 잡아먹는다
# 이게 좀 더 정석적이네
# dict와 브루트포스를 적절히 섞은 문제 풀이 방법
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


# 다른 풀이
# 와.... 감탄이 나오네
# 정렬 후 앞, 뒤 원소를 차례대로 계산하는데 zip, startswith을 이용

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
