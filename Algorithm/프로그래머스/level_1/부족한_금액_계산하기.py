def solution(price, money, count):
    rs = 0
    for i in range(count):
        rs += price * (i+1)
    answer = 0 if 0 <= money - rs else abs(money -rs)
    return answer