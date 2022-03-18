# sorted 는 list로 변환 후 정렬하기때문에 sort 와다르게 문자열도 바로 정렬이 가능하다
# key=lambda x:ord(x) 사용할 필요 없다. 자동으로 ord 식으로 정렬됨

def solution(s):
    return "".join(sorted(s, reverse=True))
