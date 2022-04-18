# 각 stinrg 을 replace 로 바꾸는 방법
# (예제용)
# 1. list comprehension 이용
# s = [i.replace('{', '') for i in str(s).split(',{') ]
# 2. map + lambda 함수 이용
# s = sorted(map(lambda x: x.replace("{", '') s.split(',{')), key=lambda x: len(x))

# 문자열 문제에 약하네,,
# 아래 코드 보지 말고
# 나중에 다시풀자

# 일단 집합(set)으로 풀이하면 순서를 보장할 수 없기때문에 집합으로 풀이하면 안된다
# 자르는 방법을 잘 정의한다 << 잘 정의해놓지 않으면 어려워진다..




# 입력값인 s 값 중 길이가 짧은것부터
# 차례대로 result에 대입하면 된다 (result에 존재하지 않으면)
# -> s의 각 원소별로 나눠야한다
# -> 앞, 뒤 {{, }} 를 제거하고
# -> },{ 를 기준으로 split 한다
# 각 원소를 차례대로 result에 대입

# def solution(s):
#     s = s[2:-2] # 양쪽 끝 괄호 자르기
#     s = s.split('},{')
#     s.sort(key=len)
#
#     answer = []
#     for i in s:
#         v = i.split(',')
#         for j in v:
#             if j not in answer:
#                 answer.append(int(j))
#
#     return answer