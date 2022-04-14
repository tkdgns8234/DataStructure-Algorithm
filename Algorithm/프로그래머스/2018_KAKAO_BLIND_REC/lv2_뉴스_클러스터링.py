# 자카드 유사도 라는 알고리즘 문제인데
# 쉽게 보면 교집합과 합집합을 구하는 문제이다
# 여기서 중복된 숫자(문자)를 처리해야하는데
# 그걸 효율적으로 잘 처리하는 방법이 있다.
# 맨 아래 코드 참고

def make_set(s):
    s = s.upper()
    res = []
    for i in range(len(s)-1):
        val = s[i:i+2]
        if val.isalpha():
            res.append(val)
    return res

def solution(str1, str2):
    set1, set2 = make_set(str1), make_set(str2)
    dic1, dic2 = dict(), dict() # 집합의 갯수 count

    for i in set1:
        dic1[i] = dic1.get(i, 0) + 1
    for i in set2:
        dic2[i] = dic2.get(i, 0) + 1

    res_and = 0
    res_or = 0
    # 교집합
    for i in dic1:
        v1, v2 = dic1.get(i, 0), dic2.get(i, 0)
        if min(v1, v2) > 0:
            res_and += min(v1, v2)
    # 합집합
    for i in set(list(dic1.keys()) + list(dic2.keys())):
        v1, v2 = dic1.get(i, 0), dic2.get(i, 0)
        res_or += max(v1, v2)

    similar = 0
    if res_and == 0 and res_or == 0:
        similar = 1
    else:
        similar = (res_and / res_or)

    return int(similar * 65536)

print(solution('aa1+aa2', 'AAAA12'))


# 좋은 풀이..
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536