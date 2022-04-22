# dp를 써야하나? 생각했는데
# 왼쪽부터 차례대로 왼쪽 or 오른쪽 reserve 인지확인하면서 하면 됨(그리디형식으로)
# 생각보다 오래걸렸다. 일단 제한사항 중 마지막 사항에대해 유의깊게 읽지 않아서였다.
# _reserve, _lost 를 구할때도 아래와 같이 짰었는데 이건 실패였네 뭐떄문이지?
# for i in lost:
#     if i in reserve:
#         reserve.remove(i)
#         lost.remove(i)
# for 문을 돌리는 list를 변경했기 때문에 문제가 발생했던것

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for i in sorted(_reserve):
        if i - 1 in _lost:
            _lost.remove(i - 1)
        elif i + 1 in _lost:
            _lost.remove(i + 1)
    answer = n - len(_lost)
    return answer