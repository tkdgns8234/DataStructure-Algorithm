def solution(brown, yellow):
    target = brown + yellow
    row, col = 0, 0
    for i in range(3, target+1):
        if target % i == 0:
            tmp_r, temp_c = target//i, i
            max_yellow = (tmp_r -2) * (temp_c -2)
            if yellow == max_yellow:
                row, col = tmp_r, temp_c

    return sorted([row, col], reverse=True)

# yellow 의 크기는 (가로 -2) * (세로 -2) 이다
# 외곽선을 제외한 모든 부분은 yellow
